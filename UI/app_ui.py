from flask import Flask, redirect, url_for, render_template, request, session, jsonify
import json
import sys
import os
from ..app import ui_data
app = Flask(__name__)
# app.secret_key = os.urandom(12)  # Generic key for dev purposes only


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    ans = [{"id": 1, "Title": "wee", "Content": "je5"}, {"id": 2, "Title": "wee", "Content": "je5"}, {"id": 3, "Title": "wee", "Content": "je5"}]
    return jsonify(ans)


# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
