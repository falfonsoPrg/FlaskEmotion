from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home():
    aux = None
    txt = ""
    error = False
    if(request.method == "POST"):
        if(request.form['twt'].strip()):
            txt = request.form['twt']
            aux = True
        else:
            error=True
    return render_template("home.html", exist = aux, txt=txt,error=error)

@app.route("/file",methods=['POST','GET'])
def file():
    aux = None
    txt = ""
    error = False
    if(request.method == "POST"):
        f = request.files['archivo']
        aux = True
        f.save(secure_filename(f.filename))
        archivo = open(secure_filename(f.filename),"r")
        for i in archivo:
            txt = txt + i
    return render_template("home.html", exist = aux, txt=txt,error=error)   
    
if __name__ == "__main__":
    app.run(debug=True)
