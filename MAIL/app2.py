from flask import Flask, render_template,url_for,request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('email.html')
@app.route("/email", methods=['GET','POST'])
def email():
    if request.method=='POST':
        recievers_email=request.form['recievers_email']
        subject=request.form['Subject']
        message=request.form['Message']
        
        
        user_data=[recievers_email,subject,message]
        return user_data
    
    
if __name__ == "__main__":
    app.run(debug=True)
           
           