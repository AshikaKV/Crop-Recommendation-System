import joblib
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Load the model once when the application starts
model_path = 'E:\\Crop-system\\Crop-system\\crop_app\\crop_app'  # Make sure the file path is correct
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('Home_1.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index1')
def user1():
    return render_template('index1.html')

@app.route('/home', methods=["POST"])
def user2():
    return render_template('index.html')

@app.route('/register')
def user():
    return render_template('register.html')

@app.route('/Predict')
def prediction():
    return render_template('index1.html')

@app.route('/form', methods=["POST"])
def brain():
    try:
        Nitrogen = float(request.form['Nitrogen'])
        Phosphorus = float(request.form['Phosphorus'])
        Potassium = float(request.form['Potassium'])
        Temperature = float(request.form['Temperature'])
        Humidity = float(request.form['Humidity'])
        Ph = float(request.form['ph'])
        Rainfall = float(request.form['Rainfall'])
        
        values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]
        
        if 0 < Ph <= 14 and Temperature < 100 and Humidity > 0:
            arr = [values]
            acc = model.predict(arr)
            return render_template('prediction.html', prediction=str(acc[0]))
        else:
            return "Sorry... Error in entered values in the form. Please check the values and fill it again."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
