from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():

    return "hello world of gunicorn"

#Flask development block
if __name__ == "__main__":
    
    # Only used for local development
    app.run(host="0.0.0.0", port=3000, debug=True)