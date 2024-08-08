from flask import Flask,redirect,url_for
import time

app=Flask(__name__)

@app.route("/")
def home():
    return "welcome to home page"

@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<h1>congrotulation {sname} you have pass with {marks} </h1>"

@app.route('/fail/<sname>/<int:marks>')
def fail(sname,marks):
    return f"<h1>sorry {sname} you are fail with {marks}</h1>"
    
    
@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num>30:
        time.sleep(1)
        return redirect(url_for('passed',sname=name,marks=num))
    else:
        return redirect(url_for('fail',sname=name,marks=num))
    
    
if __name__=="__main__":
    app.run(debug=True)
