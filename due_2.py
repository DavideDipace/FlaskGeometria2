from flask import Flask,render_template,request
import re
app = Flask(__name__)

import datetime
@app.route('/')
def home():
    return render_template('due_2.html')


@app.route('/Area', methods = ['POST'])
def Arearett():

    num_format = re.compile(r'^-?\d+(\.\d+)?$')
    numero = re.match(num_format,request.form['lato'])

    if  numero:
        lato = float(request.form['lato'])
        if lato > 0:
            area = lato **2
            return render_template('due_21.html',Lato = lato, Area = area)
        else:
            return render_template('errore_1.html', msg= "dati negativi")
    else:
         return render_template('errore_1.html', msg= "hai inserito una stringa")



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)