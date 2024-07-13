from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return "My HOme Page!"




if __name__ == "__main__"
    app.run(debug=True)
    