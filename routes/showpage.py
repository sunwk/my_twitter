from routes import *


main = Blueprint('showpage', __name__)


@main.route('/')
def show_view():
    return render_template('showpage.html')