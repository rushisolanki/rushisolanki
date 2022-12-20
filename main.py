from flask import Flask,render_template,request,url_for,redirect
import pandas as pd
import datetime
from datetime import datetime,date,timedelta

from  functions import print_myname,List_To_String,Download_Delivery_Data,High_Delivery_Percent,Download_Delivery_Data_For_N_DAYS


app = Flask(__name__)



print_myname("rushi")

@app.route('/')
def Hello_World() :
    #today_date = datetime.date.today()
    username = "Rushi"
    return  render_template("index.html", name = username)

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        selected_date = (request.form['date'])
        date = List_To_String(selected_date)
        print(date)
        print(type(date))
        date_date_format = datetime.strptime(date,'%d%m%Y')
        print(date_date_format)
        l = High_Delivery_Percent(date_date_format)
        print(l)
        
        
    return render_template("index.html", selected_date = date_date_format,List_index = l)


@app.route('/download',methods=['POST','GET'])
def a():   
    if request.method == 'POST':
        Download_Delivery_Data_For_N_DAYS(30)
        return  render_template("test.html")

        
if __name__ == "__main__":
    app.run(debug=True, port = 8000)