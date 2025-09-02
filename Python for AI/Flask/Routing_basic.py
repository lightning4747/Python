from flask import Flask

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Home Page 🏠"

# About route
@app.route('/about')
def about():
    return "This is the About Page 👀"

# Dynamic route with variable
@app.route('/user/<name>')
def user_profile(name):
    return f"Hello, {name.capitalize()}! 👋 Welcome to your profile."

if __name__ == '__main__':
    app.run(debug=True, port=5000)

