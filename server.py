

from flask import Flask, render_template

app = Flask(__name__)


# webserver routes
@app.route('/')
def index():

    return render_template("index.html")


# Run the server
@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)
    
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=2137)
