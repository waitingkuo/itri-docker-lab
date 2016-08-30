from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route("/")
def hello():
    redis.incr('hits')
    return "Hello World! I have been seen %s times." % redis.get('hits')

app.run(host="0.0.0.0", port=5000)
