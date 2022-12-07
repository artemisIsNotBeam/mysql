from flask import Flask
import commands

app = Flask(__name__)


thing = commands.makeConnection()
cursor = thing[0]
db = thing[1]
# make your vars

commands.createDB(cursor)
commands.createTable(cursor)

@app.route('/')
def index():
    return "<h1>HIIII<h1>"

def bob():
	

app.run(host='0.0.0.0', port=81)
