from flask import Flask,render_template,request
import requests
app =Flask(__name__)
API_KEY="e541f771da23a4c4f078a48a62394f59"
#premiere route vers la page d'accueil
@app.route("/")
def home():
    return render_template("index.html")


# route vers weather
@app.route("/weather",methods=["POST"])
def weather():
    city=request.form["city"] 
    #URL API
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    # envoie de la requete
    response=requests.get(url)
    #convertir en json
    data=response.json()
    #extraire les infos itules
    temp=data["main"]["temp"] #temprature
    description=data["weather"]["description"]
    return render_template("index.html",temp=temp)   

if __name__=="__main__":
    app.run(debug=True)