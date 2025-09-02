from flask import Flask, request

app = Flask (__name__) 

@app.route('/')
def home():
    return "Go to <a href='/predict'>/predict</a> to try the form!"


@app.route('/predict', methods = ['GET', 'POST'])   
def predict () :
    if request.method == "POST" :
        user_data = request.form['data']

        return f"you have submitted the form {user_data}"

    else :
        return ''' 
        <form method = "POST">
        <input type = "text" name= "data" placeholder = "enter the data to predict">
        <input type = "submit" value = "predict">
        </form>
        '''
            
if __name__ == '__main__':
    app.run(debug = True, port = 5000)            