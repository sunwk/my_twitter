from . import ModelMixin
from . import db
from . import timestamp


class Tweet(db.Model, ModelMixin):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.String())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='tweet')

    def __init__(self, form):
        super(Tweet, self).__init__()
        self.content = form.get('content', '')
        self.created_time = timestamp()
        self.user_id = form.get('user_id', '')
