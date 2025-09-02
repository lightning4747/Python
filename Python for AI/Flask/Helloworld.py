# Import the Flask class. This is the core of the framework.
from flask import Flask

# Create an instance of the Flask class.
# __name__ is a special Python variable that tells Flask where to look for templates and static files.
app = Flask(__name__)

# Define a route. This decorator tells Flask what URL should trigger our function.
# Here, we are defining the route for the site's root, aka the homepage ('/').
@app.route('/')
def hello_world():
    # This function will run when someone visits the homepage.
    # Whatever string this function returns will be sent to the client's browser.
    return 'Hello, World!'

# This block ensures the server only runs if the script is executed directly (not imported).
if __name__ == '__main__':
    # Run the application.
    # debug=True enables the debugger and reloader. ONLY use this during development.
    app.run(debug=True, port=5000) # Runs on http://127.0.0.1:5000 by default