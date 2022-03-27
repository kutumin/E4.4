import time
import urllib.request
import redis
from flask import Flask
from flask import render_template

imgURL = 123  
app = Flask(__name__, static_url_path='/static')
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

@app.route("/test")
def test():
    return render_template('home.html')
