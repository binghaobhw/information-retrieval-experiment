# -*- coding: utf-8 -*-
import os

# application settings
MONGO_URL = 'mongodb://localhost:27017/local'
CWS_MODEL_PATH = '/downloads/cws.model'

# Generate a random secret key
SECRET_KEY = os.urandom(24)
CSRF_ENABLED = True
