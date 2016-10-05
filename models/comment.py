from . import ModelMixin
from . import db
from . import timestamp


class Comment(db.Model, ModelMixin):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.String())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tweet_id = db.Column(db.Integer, db.ForeignKey('tweets.id'))

    def __init__(self, form):
        super(Comment, self).__init__()
        self.content = form.get('content', '')
        self.created_time = timestamp()
