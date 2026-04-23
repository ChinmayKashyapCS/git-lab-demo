from flask import flask
app=Flask(__name__)
@app.route('/')
def home():
  print("Docker is running')
app.run(port=5000)
