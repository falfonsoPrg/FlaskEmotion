from flask import Flask, render_template, request, redirect,url_for
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home():
    aux = None
    txt = ""
    error = False
    if(request.method == "POST"):
        if(len(request.form['twt'].strip()) > 0):
            txt = request.form['twt']
            aux = True
        else:
            error=True
    return render_template("home.html", exist = aux, txt=txt,error=error)

@app.route("/file",methods=['GET'])
def fileget():
    return redirect(url_for('home'))

@app.route("/file",methods=['POST'])
def file():
    aux = None
    arr=[]
    error = False
    if(request.method == "POST"):
        f = request.files['archivo']
        
        f.save(secure_filename(f.filename))
        archivo = open(secure_filename(f.filename),"r")
        for i in archivo:
            if(i.strip()!=''):
                arr.append(i.strip())
        aux = True if len(arr)>0 else False
        error = False if len(arr)>0 else True
    return render_template("home.html", exist = aux, arr=arr, length=len(arr),error=error)   
    
if __name__ == "__main__":
    app.run(debug=True)
