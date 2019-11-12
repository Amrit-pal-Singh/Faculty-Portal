import psycopg2
from flask import Flask, render_template, redirect, url_for, request
import psycopg2.extras
import datetime
import bcrypt
from dateutil import parser
from infrastructure.switchlang import switch
import services.data_service as svc
import program
import infrastructure.state as state
from colorama import Fore
import data.mongo_setup as mongo_setup
import infrastructure.state as state
app = Flask(__name__)


def connectToDB():
    try:
        conn = psycopg2.connect(database = "project", user = "postgres", password = "123456789", host = "127.0.0.1", port = "5432")
        print("Opened database successfully")
    except:
        print("Error Opening Database")



@app.route('/')
def index():
    if(state.active_account != None):
        obj = (state.active_account)
        return render_template('info.html', object = obj)
    else:
        return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        ss = request.form['emailid']
        password = request.form['password'].encode('utf-8')
        if(svc.find_account_by_email(ss)):
            hp = svc.find_account_by_email(ss).password.encode('utf-8')
            if bcrypt.hashpw(password, hp) == hp:
                state.active_account = svc.find_account_by_email(ss)
                return redirect(url_for('index'))
        else:
            msg = 'Invalid Email or Password'
            return render_template('login.html', msg = msg)
    return render_template('login.html')            
        

@app.route('/logout')
def logout():
   state.active_account = None
   return redirect(url_for('login'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if(request.method == 'POST'):
        name = request.form['username']
        email = request.form['emailid']
        password = request.form['password'].encode('utf-8')
        department = request.form['department']
        print('6666% name')
        if not name or not email or not password or not department :
            msg = 'Fill all the info'
            return render_template('register.html', msg = msg)
        
        hashed = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        
        old_account = svc.find_account_by_email(email)
        
        # if(' ' in name):
        #     msg = 'Username Cannot contain spaces'
        #     return render_template('register.html', msg = msg)
        

        if old_account:
            msg = 'Account of same email already exists'
            return render_template('register.html', msg = msg)
        
        try:
            conn = psycopg2.connect(database = "project", user = "postgres", password = "123456789", host = "127.0.0.1", port = "5432")
            print("Opened database successfully")
        except:
            msg = 'Cannot open database'
            return render_template('register.html', msg = msg)

        # try:
        cur = conn.cursor()
        nLeaves = 12
        cur.execute("insert into faculty(ID, noOfLeaves, department) values (%s, %s, %s);  ", (str(email), int(nLeaves), str(department)))
        conn.commit()
        print('################## Done ###############')
        print(str(name), email, department, (hashed).decode('utf-8'))
        state.active_account = svc.create_account_by_flask(str(name), email, department, (hashed).decode('utf-8'))
        return redirect(url_for('index'))
        # except:
        #     msg = 'Cannot insert the info in database'
        #     return render_template('register.html', msg = msg)
        
        
    return render_template('register.html')            


if __name__ == '__main__':
    mongo_setup.global_init()
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
