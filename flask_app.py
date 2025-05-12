from flask import Flask, render_template

app = Flask(__name__)

# Route to serve index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to serve play (placeholder)
@app.route('/play')
def play():
    return "Play page is under construction!"

if __name__ == '__main__':
    app.run(port='80')