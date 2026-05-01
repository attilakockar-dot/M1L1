from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/client')
def client():
    return render_template("client.html")

@app.route('/client-info')
def client_info():
    return render_template("client_info.html")

if __name__ == '__main__':
    app.run(debug=True)