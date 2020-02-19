from flask import Flask, render_template, request, redirect,url_for
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home():
    exist = None
    txt = ""
    error = False
    if(request.method == "POST"):
        if(len(request.form['twt'].strip()) > 0):
            txt = request.form['twt']
            exist = True
        else:
            error=True
    return render_template("home.html", exist = exist, txt=txt,error=error)

@app.route("/file",methods=['GET'])
def fileget():
    return redirect(url_for('home'))

@app.route("/file",methods=['POST'])
def file():
    exist = None
    error = False
    txt=""
    if(request.method == "POST"):
        f = request.files['archivo']
        for i in f:
            txt += i.decode("ISO-8859-1")
        if(txt.strip() != ""):
            exist = True
        else:
            error = True
            exist = False
    return render_template("home.html", exist = exist, txt=txt,error=error)   
    
if __name__ == "__main__":
    app.run(debug=True)
