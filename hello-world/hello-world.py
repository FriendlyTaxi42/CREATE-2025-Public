from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Activity 4.1: basis Hello World Web app
@app.route("/")
def home():
    return "<h1> Hello World!!!!! </h1>"

# Activity 4.2: Use routes, using routes to edit format
@app.route("/user/<name>")
def hello_with_name(name):
    return f"<h1> Hello, {name}!!!!!! </h1>"


# Activity 4.3 Introduce --debug to allow refresh on change 

# Activity 4.4: rendering HTML templates
@app.route("/time/<name>")
def render_file(name):
    current_time = datetime.now()
    return render_template("index.html", name=name, current_time=current_time)

# Activity 4.5: 

if __name__ == '__main__':
    app.run(debug=True)
