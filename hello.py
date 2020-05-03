from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
	return render_template('hello.html')
    






    
    Ajesh english mark = 50 
Subin malayalam mark = 80
Sachin python mark = 100
Lester html mark = 100
