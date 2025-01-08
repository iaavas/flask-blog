import requests
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask import Blueprint, request, jsonify, render_template
from app.models import BlogPost, db
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import BlogPost
page_bp = Blueprint('page', __name__)


API_URL = "http://127.0.0.1:5000/api"


@page_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)  # Current page
    per_page = 5

    response = requests.get(
        f"{API_URL}/blogs", params={"page": page, "per_page": per_page})
    data = response.json()

    blogs = data['blogs']
    total_pages = data['total_pages']
    current_page = data['current_page']

    return render_template('index.html', blogs=blogs, page=current_page, total_pages=total_pages)


@page_bp.route('/blog/<int:blog_id>')
def single_blog(blog_id):

    response = requests.get(f"{API_URL}/blogs/{blog_id}")
    blog = response.json()
    print(blog)
    return render_template('blog.html', blog=blog)


@page_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = {
            'email': request.form['email'],
            'password': request.form['password']
        }
        response = requests.post(f"{API_URL}/login", json=data)
        if response.status_code == 200:

            session['user'] = response.json()
            return redirect(url_for('page.index'))
        else:
            flash('Invalid credentials, please try again.', category='error')
    return render_template('login.html')


@page_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = {
            'username': request.form['username'],
            'email': request.form['email'],
            'password': request.form['password']
        }
        print(data)

        response = requests.post(f"{API_URL}/register", json=data)
        print(response)
        if response.status_code == 201:
            flash('Registration successful, please login.', category='success')
            return redirect(url_for('page.login'))
        else:

            flash(response.json()['error'], category='error')
    return render_template('register.html')


@page_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', category='success')
    return redirect(url_for('page.index'))
