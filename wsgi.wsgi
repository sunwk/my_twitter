#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname

sys.path.insert(0, abspath(dirname(__file__)))
print(abspath(dirname(__file__)))
print(sys.path)

from my_twitter import app

application = app.configured_app()




# gunicorn appcorn:app
# nohup gunicorn -b '0.0.0.0:80' appcorn:app &