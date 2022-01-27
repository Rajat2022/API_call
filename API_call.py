from flask import Flask, request

app = Flask(__name__)


@app.route('/test', methods=["POST"])
def test():
    messages = request.get_json()

    if messages["message"] == "hello":
        return "hi"
    else:
        return "please provide some input"


app.run(host="0.0.0.0", port=3000, debug=True)
