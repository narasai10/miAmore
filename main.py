from flask import Flask, redirect, url_for, request, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


coupleName = None

@app.route("/", methods=["POST", "GET"])
def index():
    couple = "+".join(request.form.get("couple").split())
    coupleName = couple
    return render_template("index.html", bootstrap=bootstrap)

@app.route("/create")
def create():
    request.args.get("coupleName", coupleName)
    if request.args.get("coupleName") == None or request.args.get("coupleName").strip() == "":
        return render_template("index.html")
    else:
        return render_template("create.html", bootstrap=bootstrap)

if __name__ == "__main__":
    app.run(debug=True)