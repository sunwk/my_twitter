import hashlib
import os

from . import ModelMixin
from . import db


def sha1_hashed(s):
    encoding = 'utf-8'
    return hashlib.sha1(s.encode(encoding)).hexdigest()


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    role = db.Column(db.Integer, default=2)
    signature = db.Column(db.String())
    visit = db.Column(db.Integer)
    sex = db.Column(db.String())

    def __init__(self, form):
        super(User, self).__init__()
        if form is not None:
            self.visit = int(0)
            self.username = form.get('username', '')
            self.password = sha1_hashed(form.get('password', ''))
            self.signature = form.get('signature', '')
            self.sex = form.get('sex', '')

    def visitors_add(self):
        self.visit += 1

    def is_admin(self):
        return self.role == 1

    def valid(self):
        is_username = len(self.username) >= 3
        is_password = len(self.password) >= 3
        return is_username and is_password

    def validate(self, user):
        username_equals = self.username == user.username
        password_equals = self.password == user.password
        if isinstance(user, User):
            return username_equals and password_equals
        else:
            return False



# class User(db.Model, ModelMixin):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String())
#
#     def __init__(self, form):
#         super(User, self).__init__()
#         self.username = form.get('username', '')
#
#     # 验证注册用户的合法性的
#     def valid(self):
#         valid_username = User.query.filter_by(username=self.username).first() == None
#         valid_username_len = len(self.username) >= 6
#         valid_password_len = len(self.password) >= 6
#         valid_captcha = self.captcha == '3'
#         msgs = []
#         if not valid_username:
#             message = '用户名已经存在'
#             msgs.append(message)
#         elif not valid_username_len:
#             message = '用户名长度必须大于等于 6'
#             msgs.append(message)
#         elif not valid_password_len:
#             message = '密码长度必须大于等于 6'
#             msgs.append(message)
#         elif not valid_captcha:
#             message = '验证码必须输入 3'
#             msgs.append(message)
#         status = valid_username and valid_username_len and valid_password_len and valid_captcha
#         return status, msgs
