from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def home():
    return 'Welcone to simple flask WebServer'

if __name__ == '__main__':
    app.run()