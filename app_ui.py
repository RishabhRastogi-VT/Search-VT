from flask import Flask, redirect, url_for, render_template, request, session, jsonify
import json
import sys
import os
from app import get_ui_data, main
app = Flask(__name__)
# app.secret_key = os.urandom(12)  # Generic key for dev purposes only


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    tmp_data = request.get_json()['input_text']
    main(tmp_data)
    print("--------------")
    print("--------------")
    print(tmp_data)
    tmp = []
    data = get_ui_data()
    for d in data:
        tmp.append(json.loads(d)[0])
    print("------------xxxxx----")
    print(type(data))
    print("------------xxxxx----")
    return jsonify(tmp)

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
