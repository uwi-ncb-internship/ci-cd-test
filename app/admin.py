"""
Admin Routes
"""
from flask import Blueprint, render_template #, session

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def admin_dashboard():
    """Admin dashboard route."""
    admin_username = 'ylynfatt' #session['username']

    return render_template('admin/dashboard.html', username=admin_username)

@admin_bp.route('/users')
def admin_users():
    """Admin users route."""
    return 'test'
