from flask import Flask,render_template,request
import math
app = Flask(__name__)

import datetime
@app.route('/')
def home():
    return render_template('tre_3.html')

@app.route('/Geometria', methods = ['GET'])
def FunzioniQuad():
    lato = float(request.args.get('lato'))
    geometria = request.args.get("geometria")
    if geometria == "Area":
        area = lato**2
        return render_template('result_1.html', Area = area)
    else:
        diagonale = math.sqrt(lato ** 2 + lato ** 2)
        return render_template('result_2.html', Diagonale = diagonale)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)