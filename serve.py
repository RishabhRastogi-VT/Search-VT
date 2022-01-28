from flask import Flask, request
app = Flask(__name__)

            
@app.route('/health')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)