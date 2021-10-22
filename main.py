from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:12345678@localhost/kuber'
db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    feedback = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Reg(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    customer_name = db.Column(db.String(30),nullable=False)
    address = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(30),nullable=False)
    event = db.Column(db.String(30),nullable=False)
    event_date = db.Column(db.String(30),nullable=True)
    event_days = db.Column(db.Integer,nullable=True)
    mobile_no =  db.Column(db.Integer,nullable=True)
    card_name = db.Column(db.String(30),nullable=False)
    card_number = db.Column(db.Integer,nullable=True)
    exp_month = db.Column(db.String(30),nullable=False)
    exp_year = db.Column(db.Integer,nullable=True)
    cvv = db.Column(db.Integer,nullable=True)
    zip_code = db.Column(db.Integer,nullable=True)
    date =  db.Column(db.String(12), nullable=True)
   

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/amenities')
def aminities():
    return render_template('amenities.html')
@app.route('/reg',methods =['GET','POST'])
def reg():
    if request.method =='POST':
        nm = request.form.get('name')
        add = request.form.get('address')
        mail = request.form.get('email')
        eve = request.form.get('event')
        event_date = request.form.get('eventdate')
        event_day = request.form.get('eventday')
        mobile = request.form.get('no')
        cname = request.form.get('cardname')
        cnumber = request.form.get('cardnumber')
        emonth = request.form.get('expmonth')
        eyear = request.form.get('expyear')
        cv = request.form.get('cvv')
        zp= request.form.get('zip')
        b=Reg(customer_name=nm,address=add,email=mail,event=eve,event_date=event_date,
            event_days=event_day,mobile_no=mobile,card_name=cname,card_number=cnumber,
            exp_month=emonth,exp_year=eyear,cvv=cv,zip_code=zp, date=datetime.now())
        db.session.add(b)
        db.session.commit()
        redirect('/')
    return render_template('reg.html')

@app.route('/contact', methods = ['GET' ,'POST'])
def contact():
    if request.method == 'POST':
        nm = request.form.get('name')
        fb = request.form.get('feedback')
        a = Contact(name=nm,feedback=fb,date=datetime.now())
        db.session.add(a)
        db.session.commit()
        redirect('/')
    return render_template('contact.html')

@app.route('/decoration')
def decoration():
    return render_template('decoration.html')
@app.route('/demo')
def demo():
    return render_template('demo.html')
@app.route('/food')
def food():
    return render_template('food.html')
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
@app.route('/location')
def location():
    return render_template('location.html')
@app.route('/online')
def online():
    return render_template('online.html')
@app.route('/package')
def package():
    return render_template('package.html')
@app.route('/reagistration')
def reagistration():
    return render_template('reagistration.html')
@app.route('/submit')
def submit():
    return render_template('submit.html')
app.run(debug = True,port=8000)
