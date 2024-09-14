from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'status':'success','message':'hello'})
