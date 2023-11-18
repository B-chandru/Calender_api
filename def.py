import calendar;
from flask import Flask, render_template, request;
app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/calender_details',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      year = request.form['year']  
      a =calendar.calendar(int(year)).split('\n')
      b =calendar.month(2001,1)
      return render_template("result.html",result = a)

@app.route('/calender_details/<year>',methods = ['POST', 'GET'])
def calender_result(year):
      year_details =calendar.calendar(int(year)).split('\n')
      return year_details

@app.route('/Calender_Month_details/<year>/<month>',methods = ['POST', 'GET'])
def month_result(year,month):
      month_details =calendar.month(int(year),int(month)).split('\n')
      return month_details

if __name__ == '__main__':
   app.run(debug = True)
