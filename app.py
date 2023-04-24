from flask import Flask, render_template, request

from scrape import ancor

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("user_entry.html")


@app.route("/submit", methods=["GET"])
def submit():
    url = request.args["url"]
    resp_data = ancor.get_ancor(url)
    # Define a route for the Reports Data Found page

    return render_template("reports_data_found.html", data=resp_data)


app.run(host="0.0.0.0", port=5000, debug=True)
