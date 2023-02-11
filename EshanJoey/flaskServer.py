from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    # type in hosts IP
    app.run(host='10.1.233.255', port=8000, debug=False)
