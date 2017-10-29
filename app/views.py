"""Does stuff."""

import random
import string
from flask import render_template, request, redirect, jsonify
from app import app

sessions = {}

session_key_length = 5
secret_key_length = 20
time_delay = 3000 # milliseconds

def create_session(music_url):
    """Create a session."""
    letters = string.ascii_uppercase
    session_key = ''.join(random.choice(letters) for i in range(session_key_length))
    secret_key = ''.join(random.choice(letters) for i in range(secret_key_length))
    sessions[session_key] = [music_url, secret_key, None] # store URL, time
    return session_key, secret_key

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    """Home page."""
    return render_template('index.html')

@app.route('/host/<path:music_url>', methods=['GET'])
@app.route('/host/<session_key>/<secret_key>/<time>', methods=['POST'])
def host(music_url='', session_key='', secret_key='', time=''):
    """Host page."""

    # Generate new session
    if request.method == 'GET':
        print('Received host GET request to create new session.')
        session_key, secret_key = create_session(music_url)
        print('Creating session {} for url {}.'.format(session_key, music_url))
        return render_template('host.html', music_url=music_url,
                               session_key=session_key, secret_key=secret_key,
                               time_delay=time_delay)

    # If authenticated, start time
    if request.method == 'POST':
        if session_key in sessions and sessions[session_key][1] == secret_key:
            print('Received host POST request to time new session.')
            sessions[session_key][2] = time
            return jsonify(time=sessions[session_key][2])
        else:
            print('Received invalid host POST request to time new session.')
            return jsonify("")

@app.route('/client/<session_key>', methods=['GET', 'POST'])
def client(session_key):
    """Client page."""

    # If extant, join new session
    if request.method == 'GET':
        print('Received request to join session {}'.format(session_key))
        if session_key in sessions:
            music_url = sessions[session_key][0]
            return render_template('client.html', music_url=music_url,
                                   session_key=session_key, time_delay=time_delay)
        else:
            return redirect('/index')

    # If extant, get session information
    if request.method == 'POST':
        print('Received request for time information on session {}.'.format(session_key))
        if session_key in sessions:
            music_url = sessions[session_key][0]
            time = sessions[session_key][2]
            return jsonify(music_url=music_url, time=time)
        else:
            return redirect('/index')
