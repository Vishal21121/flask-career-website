# there is module flask and class is Flask
from flask import Flask

# creating an instance of the Flask class
app = Flask(__name__)

# here we are using decorator basically we are passing the below function as argument to app.route funnction
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)