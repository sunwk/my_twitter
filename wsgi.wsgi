#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
from my_twitter import app

sys.path.insert(0, abspath(dirname(__file__)))
print(abspath(dirname(__file__)))
print(sys.path)

application = app.configured_app()




# gunicorn appcorn:app
# nohup gunicorn -b '0.0.0.0:80' appcorn:app &