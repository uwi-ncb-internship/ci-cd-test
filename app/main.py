"""
Main App Routes
"""
from flask import Blueprint, render_template, session

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Main application route."""
    session['username'] = 'ylynfatt'
    return render_template('main/index.html')

@main_bp.route('/about')
def about():
    """About page route."""
    return 'About this application'

@main_bp.route('/contact')
def about():
    """Contact page route."""
    return 'Contact Page'
