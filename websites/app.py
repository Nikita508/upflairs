from flask import Flask, render_template,url_for,request
import joblib
model=joblib.load(r'D:\Python\websites\LinearRegressionmodel.lb')
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route("/prediction", methods=['GET','POST'])
def prediction():
    if request.method=='POST':
        brand_name=int(request.form['brand_name'])
        owner=int(request.form['owner'])
        kms_driven=int(request.form['kms_driven'])
        age=int(request.form['age'])
        power=int(request.form['power'])
        
        user_data=[[owner,brand_name,kms_driven,age,power]]
        prediction=model.predict(user_data)[0]
        #passing the data through the model
        return str(round(prediction[0],2))
    
    
if __name__ == "__main__":
    app.run(debug=True)
           
           
           
           # get do not secure information clearly via front end and backend
           # if method not mentioned by default get will run
           #data will go via url and url is sended information
           # form tag in html file send data to here in py file 
           #our algorithm is trained on basis of 2d list 
           #debugger =shows live changes automaticaly without opening the app.py
           #flask return limited data types only
           # prediction datatype will be numpy array
           #prediction[0]=the answer we get
          # we had 2 D array then again prediction[0] for taking it out of 1D array
          # linear regression algorithm is of 2 types --> Simple and multiple linear regresion
          #simple lr=if no. of x variable is one
          #multiple lr=if no. of x variable is more then one.
          #linear regression algo while training of data try to fit the best line
          #while predeiction the point on line is taken 
          #firstly from x axis we reach to line of regression and then we can match it to y
          # if the points actually and on line do not coincide or data is not same
          #so there are many lines of regression but we take optimal one
          #optimal=Actual-predictions  it should be less
          #MSE=1/nsubmission(Yi-Y^i)^2,Y=Actual value
                                        #Y^=prediction
         # difference calculated for all the points and then it get divided from all
         #square is done for positive values
         #difference needs to be less
         #y=mx+c  lines come according to this only
         #y=B0+B1x1+B2x2+B3x3
         #linear regression algo only solves regression
         #linearregression lines cant be optimal in first time
           #Classification
           #Logistic Regression
           #diff btw linear and logistic regression
           # logistic only used for classifivcation purpose
           #logistic regression is same as linear regression
#sigmoid=sigma(linear regression)
#out put of linear regression prediction passes via sigmoid active func
#value above0.5==1 otherwise 0
#1/1+e^-z
#MSE=logloss(loss function)
# by this loss will be less

           
           