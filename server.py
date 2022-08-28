

from flask import Flask, render_template

app = Flask(__name__)


# webserver routes
@app.route('/')
def index():

    return render_template("index.html")

# Run the server
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

