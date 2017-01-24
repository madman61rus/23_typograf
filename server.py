import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def form():
    return render_template('form.html')

@app.route('/typograf',methods=['POST'])
def typograf():
        result = ""
        for character in request.form['text']:
            result += str(ord(character))+ " "
        return jsonify({'text':result})

if __name__ == "__main__":
    app.run()
