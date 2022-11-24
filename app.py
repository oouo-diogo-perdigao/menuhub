from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
	return render_template("index.html", title="MenuHub", body="Hello World")

@app.route('/menu/<int:id>')
def menu(id):
	return render_template("index.html", title="Menu", body="menu id: " + str(id))
