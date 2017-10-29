"""Does stuff."""

import random
import string
from flask import render_template, request, redirect
from app import app

sessions = {}

def create_session(music_url):
    """Create a session."""
    key_length = 5
    letters = string.ascii_uppercase
    key = ''.join(random.choice(letters) for i in range(key_length))
    secret_key = ''.join(random.choice(letters) for i in range(key_length))
    sessions[key] = [music_url, secret_key, None] # store URL, time
    print('Creating session {} for url {}.'.format(key, music_url))
    return key, secret_key

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    """Home page."""
    return render_template('index.html', message='')

@app.route('/host', methods=['GET', 'POST'])
def host():
    """Hosting music."""
    if request.method == 'POST':
        data = request.get_json().get('data', '')
        print(data)
        key = request.get_json().get('key', '')
        secret_key = request.get_json().get('secret_key', '')
        #key = request.form['key'])
        #secret_key = request.form['secret_key']
        print('Incorrect authentication with key {} and secret {}'.format(key, secret_key))
        if key in sessions and sessions[key] == secret_key: # good request
            print('Test')
            sessions[key][2] = 10
            print('starting session {}'.format(key))
            return render_template('host.html', key=key, secret_key=secret_key)
        else:
            print('Incorrect authentication with key {} and secret {}'.format(key, secret_key))
            return redirect('/index')
    else:
        music_url = request.args.get('music_url')
        key, secret_key = create_session(music_url)
        print('Created new session {} for url {}'.format(key, music_url))
        return render_template('host.html', key=key, secret_key=secret_key)

@app.route('/client', methods=['GET', 'POST'])
def client():
    """Playing music."""
    if request.method == 'POST':
        pass # give either nothing or time until play
    else:
        session_code = request.args.get('session_code')
        if session_code in sessions:
            print('Joining session {}.'.format(session_code))
            return render_template('client.html', title='Client')
        else:
            print('No session with code {}.'.format(session_code))
            return render_template('index.html')

