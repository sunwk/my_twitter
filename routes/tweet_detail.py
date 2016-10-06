from routes import *

main = Blueprint('tweet', __name__)


@main.route('/<int:tweet_id>')
def tweet_view(tweet_id):
    u = current_user()
    return render_template('tweet_detail.html', user=u)