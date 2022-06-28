from flask import Blueprint
import pybo.naverapi as nv
from flask import request

bp = Blueprint('naver',__name__,url_prefix='/naver')

@bp.route('/webtoon')
def webtoon():
    return {'result' : result}
