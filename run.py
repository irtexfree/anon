from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./templates/",  static_url_path='', static_folder='./')

@app.route("/pay")
def pay():
    return ({'result': {'message': "tets"}})


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/privacy_policy")
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route("/handle_privacy")
def handle_privacy():
    return render_template('handle_privacy.html')

@app.route("/payment")
def payment():
    return render_template('payment.html')

app.run(host="0.0.0.0", port=8081)