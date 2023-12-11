from flask import Flask , render_template , redirect , request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def main():
    return redirect("/home")

@app.route("/home" , methods = ["POST" , "GET"])
def home():
    if request.method == "POST":
        if request.form["user_input"] == "FN":
            return redirect("/FN")
        elif request.form["user_input"] == "SN":
            return redirect("/SN")
        elif request.form["user_input"] == "BN":
            return redirect("/BN")
    return render_template("home.html")

@app.route("/FN" , methods = ["POST" , "GET"])
def FN():
    df1 = pd.read_excel("SN-FN.xlsx")
    df2 = pd.read_excel("SN-BN.xlsx")
    if request.method == "POST":
        nodes1 = []
        nodes2 = []

        for i in range(len(df1)):
            if df1["FN Code"][i] == request.form["FN"]:
                nodes1.append([df1["FN Code"][i] , df1["SN Code"][i]])
                for j in range(len(df2)):
                    if df2["SN Node"][j] == df1["SN Code"][i]:
                        nodes2.append([df2["SN Node"][j] , df2["BN Node"][j] , df2["Component"][j]])
    else:
        nodes1 = []
        nodes2 = []
        for i in range(len(df1)):
            nodes1.append([df1["FN Code"][i] , df1["SN Code"][i]])
        for i in range(len(df2)):    
            nodes2.append([df2["SN Node"][i] , df2["BN Node"][i] , df2["Component"][i]])
    return render_template("FN.html" , nodes1 = nodes1 , nodes2 = nodes2)

@app.route("/SN" , methods = ["POST" , "GET"])
def SN():
    df1 = pd.read_excel("SN-FN.xlsx")
    df2 = pd.read_excel("SN-BN.xlsx")
    if request.method == "POST":
        nodes1 = []
        nodes2 = []
        for i in range(len(df1)):
            if df1["SN Code"][i] == request.form["SN"]:
                nodes1.append([df1["FN Code"][i] , df1["SN Code"][i]])
        for i in range(len(df2)):
            if df2["SN Node"][i] == request.form["SN"]:
                nodes2.append([df2["SN Node"][i] , df2["BN Node"][i] , df2["Component"][i]])
    else:
        nodes1 = []
        nodes2 = []
        for i in range(len(df1)):
            nodes1.append([df1["FN Code"][i] , df1["SN Code"][i]])
        for i in range(len(df2)):
            nodes2.append([df2["SN Node"][i] , df2["BN Node"][i] , df2["Component"][i]])

    return render_template("SN.html" , nodes1 = nodes1 , nodes2 = nodes2)

@app.route("/BN" , methods = ["POST" , "GET"])
def BN():
    df1 = pd.read_excel("SN-FN.xlsx")
    df2 = pd.read_excel("SN-BN.xlsx")
    if request.method == "POST":
        nodes1 = []
        nodes2 = []

        for i in range(len(df2)):
            if df2["BN Node"][i] == request.form["BN"]:
                nodes2.append([df2["SN Node"][i] , df2["BN Node"][i] , df2["Component"][i]])
                for j in range(len(df1)):
                    if df1["SN Code"][j] == df2["SN Node"][i]:
                        nodes1.append([df1["FN Code"][j] , df1["SN Code"][j]])
    else:
        nodes1 = []
        nodes2 = []
        for i in range(len(df1)):
            nodes1.append([df1["FN Code"][i] , df1["SN Code"][i]])
        for i in range(len(df2)):    
            nodes2.append([df2["SN Node"][i] , df2["BN Node"][i] , df2["Component"][i]])
    return render_template("BN.html" , nodes1 = nodes1 , nodes2 = nodes2)
