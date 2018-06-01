from flask import Flask
from werkzeug.utils import secure_filename
from flask import request
from flask_cors import *
import os

base_path = os.path.dirname(os.path.realpath(__file__))
upload_path = os.path.join(base_path, 'upload')
if not os.path.exists(upload_path):
  os.makedirs(upload_path)

app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/')
def hello_world():
  return 'Hello Flask!'


@app.route('/user/<username>')
def show_user_profile(username):
  # show the user profile for that user
  return 'User %s' % username




@app.route('/upload', methods=['POST'])
def upload_file():
  f = request.files['file']
  file_name = os.path.join(upload_path, f.filename)
  f.save(file_name)
  return 'success!'
if __name__ == '__main__':
  app.run()
