from flask import Flask, render_template,url_for,request
import joblib
model=joblib.load("LogisticRegression.lb")
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('form.html')
@app.route("/flightdata", methods=['GET','POST'])
def flightdata():
    if request.method=='POST':
        person_age=int(request.form['person_age'])
        flight_distance=int(request.form['flight_distance'])
        inflight_entertainment=int(request.form['inflight_entertainment'])
        baggage_handling=int(request.form['baggage_handling'])
        cleanliness=int(request.form['cleanliness'])
        departure_delay_in_minutes=int(request.form['departure_delay_in_minutes'])
        arrival_delay_in_minutes=int(request.form['arrival_delay_in_minutes'])
        gender_male=int(request.form['gender_male'])
        customer_type_disloyal_customer=int(request.form['customer_type_disloyal_customer'])
        type_of_travel_personal_travel=int(request.form['type_of_travel_personal_travel'])
        class_eco=int(request.form['class_eco'])
        class_eco_plus=int(request.form['class_eco_plus'])
        
        flight_data=[[person_age,flight_distance,inflight_entertainment,departure_delay_in_minutes,arrival_delay_in_minutes,baggage_handling,cleanliness,gender_male,customer_type_disloyal_customer,type_of_travel_personal_travel,class_eco,class_eco_plus]]
        prediction=model.predict(flight_data)[0]
        #passing the data through the model
        
        return str(round(prediction,2))
    
    
if __name__ == "__main__":
    app.run(debug=True)
           
           