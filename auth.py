import json
from pytools.pytools import pas
from pytools.pytools import base64decode
import os


config=json.loads(base64decode(os.environ['config']))
url=config['server']+':'+config['port']
pas(url,os.environ['password'])
