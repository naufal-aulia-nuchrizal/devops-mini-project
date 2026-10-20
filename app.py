from flask import Flask
import redis

app = Flask(__name__)


cache = redis.Redis(host='redis-db', port=6379)

def get_hit_count(r_client=cache):
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            

@app.route('/')
def hello():
    count = get_hit_count()
    return f"<h1> Halo! situs ini telah dikunjungi {count} kali. </h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)