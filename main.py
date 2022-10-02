from flask import Flask
app = Flask(__name__)

@app.route("/api")
def api():
    return {"name":"Hello"}


if __name__ == "__main__":
    app.run(debug=True)
