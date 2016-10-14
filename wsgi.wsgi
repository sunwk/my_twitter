#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
import app

sys.path.insert(0, abspath(dirname(__file__)))

application = app.configured_app()




# gunicorn appcorn:app
# nohup gunicorn -b '0.0.0.0:80' appcorn:app &