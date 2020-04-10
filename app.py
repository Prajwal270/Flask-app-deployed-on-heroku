print('jfpasof')
from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def add():
    return '<h1>jfsaodjfi</h1>'




@app.route('/predict', methods= ["POST", "GET"])
def res():
    if request.method =="POST":
        f = float(request.form["first"])
        s = float(request.form["second"])
        t = float(request.form["third"])
        r = float(request.form["forth"])
        p = model.predict([np.array([f,s,t,r])])
        h = p[0]
        return render_template('index.html', f = f, s = s, t = t, r = r, h = h)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True,port=70)