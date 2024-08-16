from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/<name>")
# @app.route("/index/")
def index(name):
    request_gender = requests.get(url=f"https://api.genderize.io?name={name}")
    gender = request_gender.json()["gender"]

    request_age = requests.get(url=f"https://api.agify.io?name={name}")
    age = request_age.json()["age"]

    return render_template("app.html", name=name, gender = gender, age = age)


if __name__ == "__main__":
    app.run(debug=True)
