from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session
from flask import url_for
from flask import abort
from flask import flash

from models.user import User
from models.tweet import Tweet
from models.concern import Follow

import time


def log(*args):
    t = time.time()
    tt = time.strftime(r'%Y/%m/%d %H:%M:%S', time.localtime(t))
#    print(tt, *args)
#    with open('log.txt', 'a') as f:
#        f.write('{} : {}\n'.format(tt, *args))
#        f.close()


def current_user():
    # cid = request.cookies.get('cookie_id', '')
    # user = cookie_dict.get(cid, None)
    user_id = session.get('user_id', '')
    user = User.query.filter_by(id=user_id).first()
    return user



# from functools import wraps
# def admin_required(f):
#     @wraps(f)
#     def function(*args, **kwargs):
#         # your code
#         print('admin required')
#         if request.args.get('uid') != '1':
#             print('not admin')
#             abort(404)
#         return f(*args, **kwargs)
#     return function
