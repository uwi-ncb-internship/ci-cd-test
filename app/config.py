"""
Configuration
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    """ Config class which will contain all configuration variables for application """
    SECRET_KEY=os.environ.get('SECRET_KEY')
