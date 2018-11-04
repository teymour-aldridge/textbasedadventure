from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from textbasedadventure.auth import login_required
from textbasedadventure.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    db = get_db()
    stories = db.execute(
        'SELECT s.id, title, body, created, author_id, username'
        ' FROM story s JOIN user u ON s.author_id = u.id'
        ' ORDER BY created DESC '
    ).fetchall()
    return render_template('stories/index.html', stories=stories)
