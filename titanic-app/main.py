from flask import Flask, render_template, request
import numpy as np
import joblib, sklearn
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict/', methods=['GET','POST'])
def predict():
    if request.method == "POST":
        Sex_male = request.form.get('is_male')
        Embarked_C = request.form.get('embC')
        Embarked_Q = request.form.get('embQ')
        Embarked_S = request.form.get('embS')
        misAge_1 = request.form.get('mis_age')
        Pclass = request.form.get('pclass')
        Age = request.form.get('age')
        SibSp = request.form.get('sibsp')
        Parch = request.form.get('parch')
        Fare = request.form.get('fare')
        Age2 = int(Age)**2
        try:
            prediction = preprocessDataAndPredict(
                Sex_male, 
                Embarked_C, 
                Embarked_Q, 
                Embarked_S, 
                misAge_1, 
                Pclass, 
                Age, 
                SibSp, 
                Parch, 
                Fare, 
                Age2)
            return render_template('predict.html', prediction = prediction)
        except ValueError:
            return "Please Enter valid values"
        pass        
    pass
def preprocessDataAndPredict(Sex_male, Embarked_C, Embarked_Q, Embarked_S, misAge_1, Pclass, Age, SibSp, Parch, Fare, Age2):
    test_data = [Sex_male, Embarked_C, Embarked_Q, Embarked_S, misAge_1, Pclass, Age, SibSp, Parch, Fare, Age2]
    print(test_data)
    test_data = np.array(test_data).astype(np.float) 
    test_data = test_data.reshape(1,-1)
    print(test_data)
    file = open("rf_model.pkl","rb")
    trained_model = joblib.load(file)
    prediction = trained_model.predict(test_data)
    return prediction
    pass
if __name__ == '__main__':
    app.run(debug=True)
