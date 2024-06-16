from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"

debug = DebugToolbarExtension(app)


@app.route("/")
def home_questions():

    """Ask questions in the home page form"""

    prompts = story.prompts
    return render_template("home_questions.html", prompts=prompts)


@app.route("/story")
def show_story():

    """Display generated story."""

    text = story.generate(request.args)
    return render_template("story.html", text=text)