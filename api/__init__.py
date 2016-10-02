from flask import request
from flask import url_for
from flask import session
from flask import Blueprint
from flask import jsonify

from functools import wraps

from models.user import User

import time

main = Blueprint('api', __name__)


# 通过 session 来获取当前登录的用户
def current_user():
    # print('session, debug', session.permanent)
    username = session.get('username', '')
    u = User.query.filter_by(username=username).first()
    return u


def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        if current_user() is None:
            r = {
                'success': False,
                'message': '未登录',
            }
            return jsonify(r)
        return f(*args, **kwargs)
    return function


def log(*args):
    t = time.time()
    tt = time.strftime(r'%Y/%m/%d %H:%M:%S', time.localtime(t))
    print(tt, *args)
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write('{} : {}\n'.format(tt, *args))
        f.close()

