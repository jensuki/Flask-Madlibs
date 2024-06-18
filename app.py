from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"

debug = DebugToolbarExtension(app)

@app.route("/")
def select_story():
    """Allow user to select a story template."""
    return render_template("select_story.html", stories=stories)

@app.route("/questions")
def home_questions():
    """Ask questions in the home page form."""
    story_id = request.args.get("story_id")
    story = stories[story_id]
    prompts = story.prompts
    return render_template("home_questions.html", story_id=story_id, prompts=prompts,title=story.title)

@app.route("/story")
def show_story():
    """Display generated story."""
    story_id = request.args.get("story_id")
    story = stories[story_id]
    text = story.generate(request.args)
    return render_template("story.html", text=text, title=story.title)
