from flask import request, redirect, render_template, Blueprint, url_for


core = Blueprint('core', __name__, template_folder='templates')

@core.route('/')
def index():
	return render_template(template_name_or_list = 'core/index.html')

