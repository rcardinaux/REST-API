from flask import render_template
# Remove: import connexion
import config
from model import Person

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

# Connect the URL route "/" to the home() function
@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

""" In short, this code gets a basic web server up and running and makes it respond with a home.html template,
which will be served to a browser when navigating to the URL "/".
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

# When you run app.py, a web server will start on port 8000