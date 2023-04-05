from flask import Flask,render_template,request
app = Flask(__name__)

import datetime
@app.route('/')
def home():
    return render_template('uno_1.html')

@app.route('/Area', methods = ['GET'])
def Areaquad():
    lato = float(request.args.get('lato'))
    area = lato**2
    return render_template('result_1.html',Lato = lato, Area = area)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)