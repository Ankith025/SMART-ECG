from flask import Flask, render_template, request, flash, redirect
import sqlite3
import pickle
import numpy as np

app = Flask(__name__)
import pickle
knn=pickle.load(open("model/model.pkl","rb"))
import telepot
bot=telepot.Bot("8589940063:AAGvj2phQmR-6fM2yBYbygc0-Py6oYwpjgk")
ch_id="2069255228"
    

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/userlog', methods=['GET', 'POST'])
def userlog():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT name, password FROM user WHERE name = '"+name+"' AND password= '"+password+"'"
        cursor.execute(query)

        result = cursor.fetchall()

        if result:
            import requests
            import pandas as pd
            data=requests.get("https://api.thingspeak.com/channels/2777003/feeds.json?results=2")
            hb=data.json()['feeds'][-1]['field1']
            temp=data.json()['feeds'][-1]['field2']
            ecg=data.json()['feeds'][-1]['field3']
            print(f"heart beat : {hb} \n temperature : {temp} \n ECG : {ecg}")
            return render_template('fetal.html',hb=hb,temp=temp,ecg=ecg,name=name)
        else:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')

    return render_template('index.html')


@app.route('/userreg', methods=['GET', 'POST'])
def userreg():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
        cursor.execute(command)

        cursor.execute("INSERT INTO user VALUES ('"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        connection.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')

@app.route('/logout')
def logout():
    return render_template('index.html')


@app.route("/fetalPage", methods=['GET', 'POST'])
def fetalPage():
    import requests
    import pandas as pd
    data=requests.get("https://api.thingspeak.com/channels/2777003/feeds.json?results=2")
    hb=data.json()['feeds'][-1]['field1']
    temp=data.json()['feeds'][-1]['field2']
    ecg=data.json()['feeds'][-1]['field3']
    print(f"heart beat : {hb} \n temperature : {temp} \n ECG : {ecg}")
    return render_template('fetal.html',hb=hb,temp=temp,ecg=ecg)




@app.route("/predict", methods = ['POST', 'GET'])
def predictPage():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        Gender = request.form['Gender']
        height = request.form['height']
        Weight = request.form['Weight']
        ECG = request.form['ECG']
        his = int(request.form['his'])
        if his == 1:
            history="Cardiac Arrest Happened"
        elif his == 0:
            history="No Previous Cardiac Arrest Happened"
        
        Heart_Rate = request.form['Heart_Rate']
        Temperature = request.form['Temperature']
        data = np.array([[age, Gender, height, Weight, ECG, Heart_Rate, Temperature]])
        my_prediction = knn.predict(data)
        result = my_prediction[0]
        avg = float(367.2)

        # Calculate deviation percentage
        cent = abs(float(ECG) - avg) / avg * 100
        cent=f"{cent:.2f}"
        print("Deviation percentage:", cent)
        print(result)

        def classify_risk(result):
            if result in [ 5, 6, 7, 8, 9, 10]:
                ress=["LOW","Regular Checkups: Continue periodic monitoring of heart health to catch early warning signs if the condition progresses.",
                "Avoid Excessive Stimulants: Limit caffeine, energy drinks, or other stimulants that might stress the heart.",
                "Regular Exercise: Incorporate moderate physical activity, such as brisk walking or swimming, for at least 30 minutes a day, five times a week.",
                "Balanced Diet: Focus on a heart-healthy diet rich in fruits, vegetables, whole grains, and lean proteins."]
                return ress
            elif result in [2, 3, 4, 14]:
                ress=["High","Monitor Symptoms Closely: Be alert to signs like shortness of breath, dizziness, or palpitations and report them to a healthcare provider promptly.",
                "Follow Medication Plans: Adhere strictly to prescribed medications or treatments to stabilize arrhythmia.",
                "Stress Management: Practice relaxation techniques like yoga or mindfulness to reduce stress, which can exacerbate arrhythmias.",
                "Quit Smoking: Eliminate tobacco use to reduce heart strain and improve cardiovascular health."]
                return ress
            elif result in [15, 16]:
                ress=["Moderate","Immediate Medical Attention: Seek urgent medical care for severe symptoms or complications to prevent emergencies like cardiac arrest.",
                "Restrict Strenuous Activities: Avoid activities that may overexert the heart, as advised by your doctor.",
                "Low-Sodium Diet: Adopt a diet that minimizes salt intake to manage blood pressure and reduce heart stress.",
                "Weight Management: Maintain a healthy weight through a supervised diet and light, safe exercise as recommended by healthcare professionals."]
                return ress
            else:
                return 'Unknown'
        risk = classify_risk(result)
        var=0
        if result == 1 :
            res='Normal'
        elif result == 2: 
            res='Ischemic changes (Coronary Artery)'
        elif result == 3:
            res='Old Anterior Myocardial Infarction'
        elif result == 4:
            res='Old Inferior Myocardial Infarction'
        elif result == 5:
            res='Sinus tachycardia'
        elif result == 6:
            res='Ventricular Premature Contraction (PVC)'
        elif result == 7:
            res='Supraventricular Premature Contraction'
        elif result == 8:
            res='Left bundle branch block'
        elif result == 9 :
            res='Right bundle branch block'
        elif result == 10:
            res='Left ventricle hypertrophy'
        elif result == 14:
            res='Atrial Fibrillation or Flutter'
        elif result == 15:
            res='Others1'
        elif result == 16:
            res='Others2' 
        if result != 1:
            bot.sendMessage(ch_id,f" Name : {name} \n Age : {age} \n Gender : {Gender} \n ECG : {ECG} \n Heart Rate : {Heart_Rate} \n Temperature : {Temperature} \n Risk Level : {risk[0]} \n Deviation percentage : {cent} % \n History of Cardiac Occured :  {history}")
        else :
            bot.sendMessage(ch_id,f" Name : {name} \n Age : {age} \n Gender : {Gender} \n ECG : {ECG} \n Heart Rate : {Heart_Rate} \n Temperature : {Temperature} \n Risk Level : No Risk ,You are Healthy ")
        print(res)

        
        

           
        return render_template('predict.html',name=name, pred = result,status=res,risk=risk,cent=cent)

    return render_template('predict.html')

if __name__ == '__main__':
	app.run(debug = True)