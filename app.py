from flask import Flask
app = Flask(__name__)

@app.route('/info')
def lwinfo():
    return 'Hello from Jenkins!'
@app.route('/phone')
def  lwphone():
    return "8813739110"
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')
