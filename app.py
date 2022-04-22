from flask import request

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def getvalue():
    name = request.form['first']
    year = request.form['second']
    price = request.form['third']    

    print(name+" "+year+" "+price)

    return render_template('index.html')



if __name__ == "__main__":
    app.run()