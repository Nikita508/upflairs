from flask import Flask, render_template,url_for,request
app = Flask(__name__)
@app.route('/')
def home():
    #return "my home page"
    return render_template('home.html')
@app.route("/userdata", methods=['GET','POST'])
def userdata():
    if request.method=='POST':
        sender_email=request.form['sender_email']
        
        sender_message=request.form['sender_message']
        user_data={'user_email':[sender_email],'sender_messafge':[sender_message]}
        return user_data
@app.route("/userhappy", methods=['GET','POST'])
def userhappy():
    if request.method=='POST':
        User_Name = request.form['User_Name']
        
        #user_data={'user_name':[user_name]}
       # return f"hii {User_Name} welcome to upflairs"
        return render_template('render.html',User_Name=User_Name)
if __name__ == "__main__":
    app.run(debug=True)