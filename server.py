import json
from typograf import do_typograf

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def form():
    return render_template('form.html')

@app.route('/typograf',methods=['POST'])
def typograf():
    return jsonify(text = do_typograf(request.form['text']))

if __name__ == "__main__":
    app.run()
