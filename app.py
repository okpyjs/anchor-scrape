from flask import Flask, render_template, request

from scrape import ancor

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("user_entry.html", data="home")


@app.route("/submit", methods=["GET"])
def submit():
    return render_template("reports_data_found.html", data="submit")


@app.route("/scrape", methods=["POST"])
def scrape():
    url = request.form["url"]
    print(url)
    try:
        resp_data = ancor.get_ancor(url)
    except:  # noqa
        return render_template("user_entry.html", data="url_error")
    return resp_data


app.run(host="0.0.0.0", port=5000, debug=True)
