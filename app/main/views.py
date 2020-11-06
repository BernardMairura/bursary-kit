from flask import render_template,request,redirect,url_for,abort
from . import main
# from .forms import 
from ..models import User,Question
from flask_login import login_required,current_user
from .. import db
from flask.views import View,MethodView




#Views
@main.route('/')
def index():

    return render_template('home.html')



@main.route('ask/')
def ask():

    return render_template('ask.html')



@main.route('answer/')
def ask():

    return render_template('answer.html')