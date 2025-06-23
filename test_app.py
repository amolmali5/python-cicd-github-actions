from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Welcome to the World of Github Actions CI/CD workflow!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
