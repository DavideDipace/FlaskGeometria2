from flask import Flask,render_template,request
app = Flask(__name__)

import datetime
@app.route('/')
def home():
    return render_template('due_2.html')

@app.route('/Area', methods = ['GET'])
def Areaquad():
    
    if request.args.get('lato').isdigit() == True :
        lato = float(request.args.get('lato'))
        if lato > 0 :
            area = lato**2
            return render_template('result_1.html',Lato = lato, Area = area)
        else:
            return render_template('errore_1.html', msg= "dati negativi")
    else:
         return render_template('errore_1.html', msg= "hai inserito una stringa")



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)