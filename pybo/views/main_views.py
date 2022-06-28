from flask import Blueprint, render_template, url_for
import testdb
from pybo.models import Question
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('question.questionlist'))

@bp.route('/hello')
def hello_pybo():
    return 'hello, pybo'

@bp.route('/dbtest')
def dbtest():
    testdb.test()
    return '성공'

