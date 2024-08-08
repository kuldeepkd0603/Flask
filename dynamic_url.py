from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>welcome to home page</h1>"

app.route("/welcome/kuldeep")
def welcome_kuldeep():
    return f"welcome kuldeep to our web page"

app.route("/welcome/mihir")
def welcome_mihir():
    return f"welcome mihir to our web page"



if __name__=="__main__":
    app.run(debug=True)