from flask import Flask,redirect,url_for
import time

app=Flask(__name__)

@app.route("/")
def home():
    return "welcome to home page"

@app.route("/pass")
def passed():
    return "<h1>congrotulation you have pass </h1>"

@app.route('/fail')
def fail():
    return "<h1>sorry you are fail</h1>"
    
    
@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num>30:
        time.sleep(1)
        return redirect(url_for('passed'))
    else:
        return redirect(url_for('fail'))
    
    
if __name__=="__main__":
    app.run(debug=True)
