from flask import Flask


app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>welcome to home page!</h1>"
    
@app.route("/about")
def about():
    return "<h1>welcome to about page</h1>"

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>welcome {name.title()} to our we page<h1/>"
    
if __name__=="__main__":
    app.run(debug=True)