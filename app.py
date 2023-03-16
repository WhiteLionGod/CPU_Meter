import sys
import os
from flask import Flask, render_template
import psutil
import flaskwebgui
from flaskwebgui import FlaskUI

sys.stdout = sys.stderr = open(os.devnull, 'w')

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

gui = flaskwebgui.FlaskUI(app)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/api/cpu")
def api():
    return str(psutil.cpu_percent(interval=0.1))

if __name__ == "__main__":
    #app.run(debug=True)
#If you want to view the code on github pages, remove  the coment from the code above and comment the code bellow.
    FlaskUI(app=app, server="flask").run()
