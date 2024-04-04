from flask import request, redirect, render_template, Blueprint, url_for

from blueprints.people.models import Person
from app import db

people = Blueprint('people', __name__, template_folder='templates')

@people.route('/')
def index():
	all_people = Person.query.all()
	return render_template(template_name_or_list = 'people/index.html', people=all_people)

@people.route('/create', methods=['GET', 'POST'])
def create():
	if request.method == 'GET':
		return render_template(template_name_or_list = 'people/create.html')
	elif request.method == 'POST':
		name = request.form.get('name')
		age = request.form.get('age')
		job = request.form.get('job')
		person = Person(name=name, job=job, age=age)
		db.session.add(person)
		db.session.commit()
		return redirect(url_for('people.index'))