from flask import request, redirect, render_template, Blueprint, url_for

from blueprints.todos.models import Todo
from app import db

todos = Blueprint('todos', __name__, template_folder='templates')

@todos.route('/')
def index():
	all_todos = Todo.query.all()
	return render_template(template_name_or_list = 'todos/index.html', todos=all_todos)

@todos.route('/create', methods=['GET', 'POST'])
def create():
	if request.method == 'GET':
		return render_template(template_name_or_list = 'todos/create.html')
	elif request.method == 'POST':
		name = request.form.get('name')
		done = True if 'done' in request.form.keys() else False
		description = request.form.get('description')
		todo = Todo(name=name, done=done, description=description)
		db.session.add(todo)
		db.session.commit()
		return redirect(url_for('todos.index'))

