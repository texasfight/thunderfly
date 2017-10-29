"""Does stuff."""

from flask import render_template, request
from app import app

sessions = {}

def create_key(music_url):
    """Create a session key."""
    return 'keyfor{}'.format(music_url)

def create_session(music_url):
    """Create a session."""
    key = create_key(music_url)
    sessions[key] = music_url
    print('Creating session {} for url {}.'.format(key, music_url))
    return key

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    """Home page."""
    return render_template('index.html', title='Home')

@app.route('/host', methods=['GET'])
def host():
    """Hosting music."""
    music_url = request.args.get('music_url')
    print(music_url)
    return render_template('host.html', title='Host')

@app.route('/client', methods=['GET'])
def client():
    """Playing music."""
    session_code = request.args.get('session_code')
    print(session_code)
    return render_template('client.html', title='Client')
