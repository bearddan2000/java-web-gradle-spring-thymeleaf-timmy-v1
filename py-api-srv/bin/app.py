from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.get('/')
def get_all():
    lst = [
        'current', 
        'historical'
    ]
    return {"count": len(lst), "links": lst}

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)