from . import ModelMixin
from . import db
from . import timestamp


class Follow(db.Model, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer)
    followee_id = db.Column(db.Integer)
    time = db.Column(db.String())

    def __init__(self):
        super(Follow, self).__init__()
        self.followee_id = None
        self.follower_id = None
        self.time = timestamp()

