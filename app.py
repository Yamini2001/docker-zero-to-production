from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from inside Docker! 🐳</h1><p>Your Python Flask application is running successfully.</p>"

if __name__ == '__main__':
    # host='0.0.0.0' is required so the app can accept connections from outside the container
    app.run(host='0.0.0.0', port=5000)
