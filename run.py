import os
import json
from pathlib import Path
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", _pagetitle="Thorin & Company")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", _pagetitle="About", _company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form.get("name"))
        print(request.form["email"])
    return render_template("contact.html", _pagetitle="Contact Us")


@app.route("/careers")
def careers():
    return render_template("careers.html", _pagetitle="Careers")


@app.route("/notes")
def notes():
    return render_template("notes.html", _pagetitle="Notes")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True,
    )
