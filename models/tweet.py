from . import ModelMixin
from . import db


class Tweet(db.Model, ModelMixin):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.String())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        super(Tweet, self).__init__()
        self.content = form.get('content', '')
