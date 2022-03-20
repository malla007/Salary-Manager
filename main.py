from flask import Flask, render_template, url_for, request,redirect, session
from datetime import timedelta
import pyrebase
config = {
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__)
app.secret_key = "a6as7bhjk"


@app.route('/')
def home():
    if "email" in session:
        return redirect(url_for("view_employee"))
    else:
        return redirect(url_for("login"))

@app.route('/login/', methods = ["POST","GET"])
def login():
        request.headers.get('User-Agent')
        platform = request.user_agent.platform
        if platform == "iphone" or platform == "android":
            unsuccessful = "Please check your credentials!"
            if request.method == "POST":

                email = request.form["email"]
                password = request.form["password"]
                session["email"] = email
                try:
                    auth.sign_in_with_email_and_password(email,password)
                    return redirect(url_for("view_employee"))
                    
                except:    
                    return render_template('mobileIndex.html',us = unsuccessful)
            return render_template('mobileIndex.html')

        else:
            unsuccessful = "Please check your credentials!"
            if request.method == "POST":

                email = request.form["email"]
                password = request.form["password"]
                session["email"] = email
                try:
                    auth.sign_in_with_email_and_password(email,password)
                    return redirect(url_for("view_employee"))
                    
                except:    
                    return render_template('index.html',us = unsuccessful)
            return render_template('index.html')


@app.route('/add_employee/', methods = ["POST","GET"])
def add_employee():
    if "email" in session:
        request.headers.get('User-Agent')
        platform = request.user_agent.platform
        if platform == "iphone" or platform == "android":
            if request.method == "POST":
                    fname= request.form["fname"]
                    daily_salary = request.form["daily-sal"]
                    daily_salary = int(daily_salary)
                    remaining_amount = 0
                    days_worked = 0
                    overtime_hrs_payment = 0
                    advance_total = 0
                    db = firebase.database()
                    db.child(fname).child("name").set(fname)
                    db.child(fname).child("daily_salary").set(daily_salary)
                    db.child(fname).child("remaining_amount").set(remaining_amount)
                    db.child(fname).child("days_worked").set(days_worked)
                    db.child(fname).child("overtime_hrs_payment").set(overtime_hrs_payment)
                    db.child(fname).child("advance_total").set(advance_total)

                    emp_list = db.child('employee_list').get()
                    employee_list = emp_list.val()
                    employee_list.append(fname)
                    db.child('employee_list').set(employee_list)
            return render_template('mobileMain.html')
            
        else:
            if request.method == "POST":
                    fname= request.form["fname"]
                    daily_salary = request.form["daily-sal"]
                    daily_salary = int(daily_salary)
                    remaining_amount = 0
                    days_worked = 0
                    overtime_hrs_payment = 0
                    advance_total = 0
                    db = firebase.database()
                    db.child(fname).child("name").set(fname)
                    db.child(fname).child("daily_salary").set(daily_salary)
                    db.child(fname).child("remaining_amount").set(remaining_amount)
                    db.child(fname).child("days_worked").set(days_worked)
                    db.child(fname).child("overtime_hrs_payment").set(overtime_hrs_payment)
                    db.child(fname).child("advance_total").set(advance_total)

                    emp_list = db.child('employee_list').get()
                    employee_list = emp_list.val()
                    employee_list.append(fname)
                    db.child('employee_list').set(employee_list)
            return render_template('main.html')
    else:
        return redirect(url_for("login"))

@app.route('/view_employee/', methods = ["POST","GET"])
def view_employee():
    if "email" in session:
        request.headers.get('User-Agent')
        platform = request.user_agent.platform
        if platform == "iphone" or platform == "android":
            db = firebase.database()
            emp_list = db.child('employee_list').get()
            employee_list = emp_list.val()
            if request.method == "POST":
                if request.form['btn'] == 'View':

                    name = request.form.get('name_list')

                    remaining_salary = db.child(name).child("remaining_amount").get()
                    remaining_salary = remaining_salary.val()

                    daily_salary = db.child(name).child("daily_salary").get()
                    daily_salary = daily_salary.val()

                    days_worked = db.child(name).child("days_worked").get()
                    days_worked = days_worked.val()

                    overtime_total = db.child(name).child('overtime_hrs_payment').get()
                    overtime_total = overtime_total.val()

                    advance_paid = db.child(name).child('advance_total').get()
                    advance_paid = advance_paid.val()

                elif request.form['btn'] == 'Pay':
                    name = request.form.get('name_list')
                    payment = request.form.get('payment')
                    advance_paid = db.child(name).child('advance_total').get()
                    advance_paid = advance_paid.val()
                    
                    payment = int(payment)
                    total_advance = payment +advance_paid
                    remaining_amount = db.child(name).child("remaining_amount").get()
                    remaining_amount = remaining_amount.val()
                    
                    final_amount = remaining_amount-payment
                    db.child(name).child("remaining_amount").set(final_amount)
                    db.child(name).child("advance_total").set(total_advance)
                    return render_template('mobileEmployee_details.html', employees = employee_list)

                return render_template('mobileEmployee_details.html', employees = employee_list, remaining_salary = remaining_salary, emp_name = name, daily_salary = daily_salary, days_worked = days_worked, overtime_total = overtime_total, advance_paid = advance_paid)
                        
            return render_template('mobileEmployee_details.html', employees = employee_list)
            
        else:
            db = firebase.database()
            emp_list = db.child('employee_list').get()
            employee_list = emp_list.val()
            if request.method == "POST":
                if request.form['btn'] == 'View':

                    name = request.form.get('name_list')

                    remaining_salary = db.child(name).child("remaining_amount").get()
                    remaining_salary = remaining_salary.val()

                    daily_salary = db.child(name).child("daily_salary").get()
                    daily_salary = daily_salary.val()

                    days_worked = db.child(name).child("days_worked").get()
                    days_worked = days_worked.val()

                    overtime_total = db.child(name).child('overtime_hrs_payment').get()
                    overtime_total = overtime_total.val()

                    advance_paid = db.child(name).child('advance_total').get()
                    advance_paid = advance_paid.val()

                elif request.form['btn'] == 'Pay':
                    name = request.form.get('name_list')
                    payment = request.form.get('payment')
                    advance_paid = db.child(name).child('advance_total').get()
                    advance_paid = advance_paid.val()
                    
                    payment = int(payment)
                    total_advance = payment +advance_paid
                    remaining_amount = db.child(name).child("remaining_amount").get()
                    remaining_amount = remaining_amount.val()
                    
                    final_amount = remaining_amount-payment
                    db.child(name).child("remaining_amount").set(final_amount)
                    db.child(name).child("advance_total").set(total_advance)
                    return render_template('employee_details.html', employees = employee_list)

                return render_template('employee_details.html', employees = employee_list, remaining_salary = remaining_salary, emp_name = name, daily_salary = daily_salary, days_worked = days_worked, overtime_total = overtime_total, advance_paid = advance_paid)
                        
            return render_template('employee_details.html', employees = employee_list)
    else:
        return redirect(url_for("login"))
@app.route('/daily_work/', methods = ["POST","GET"])
def daily_work():
    if "email" in session:
        request.headers.get('User-Agent')
        platform = request.user_agent.platform
        if platform == "iphone" or platform == "android":
            db = firebase.database()
            emp_list = db.child('employee_list').get()
            employee_list = emp_list.val()
            if request.method == "POST":
                if request.form['btn'] == 'Submit':
                    employee_name = request.form.get('name_list')

                    daily_salary = db.child(employee_name).child("daily_salary").get()
                    daily_salary = daily_salary.val()

                    remaining_amount = db.child(employee_name).child("remaining_amount").get()
                    remaining_amount = remaining_amount.val()

                    work_status = request.form.get('options')
                    overTimeHrs = request.form.get('over_time')

                    days_worked = db.child(employee_name).child('days_worked').get()
                    days_worked = days_worked.val()

                    overtime_total = db.child(employee_name).child('overtime_hrs_payment').get()
                    overtime_total = overtime_total.val()

                    if work_status == "option1":
                        add_days_worked = days_worked + 1
                        remaining_amount = daily_salary+remaining_amount
                        overtime_amt = daily_salary/8
                        overTimeHrs = int(overTimeHrs)
                        overtime_amt_day = overtime_amt*overTimeHrs
                        final_amount = overtime_amt_day+remaining_amount

                        overtime_total = overtime_amt_day +overtime_total

                        db.child(employee_name).child("overtime_hrs_payment").set(overtime_total)
                        db.child(employee_name).child("remaining_amount").set(final_amount)
                        db.child(employee_name).child('days_worked').set(add_days_worked)
                    elif work_status == "option2":
                        overtime_amt = daily_salary/8
                        overTimeHrs = int(overTimeHrs)
                        overtime_amt_day = overtime_amt*overTimeHrs
                        final_amount = overtime_amt_day+remaining_amount
                        overtime_total = overtime_amt_day +overtime_total
                        db.child(employee_name).child("overtime_hrs_payment").set(overtime_total)
                        final_amount = overtime_amt_day+remaining_amount
                        db.child(employee_name).child("remaining_amount").set(final_amount)

                elif request.form['btn'] == 'Reset Employee':
                    name = request.form.get('name_list')
                    db.child(name).child("advance_total").set(0)
                    db.child(name).child("days_worked").set(0)
                    db.child(name).child("overtime_hrs_payment").set(0)
                    db.child(name).child("remaining_amount").set(0)

                elif request.form['btn'] == 'Reset All Employees':
                    for employee in employee_list:
                        db.child(employee).child("advance_total").set(0)
                        db.child(employee).child("days_worked").set(0)
                        db.child(employee).child("overtime_hrs_payment").set(0)
                        db.child(employee).child("remaining_amount").set(0)
                return render_template('mobileDaily_work.html',employees = employee_list)
        
            return render_template('mobileDaily_work.html',employees = employee_list)
        else:
            db = firebase.database()
            emp_list = db.child('employee_list').get()
            employee_list = emp_list.val()
            if request.method == "POST":
                if request.form['btn'] == 'Submit':
                    employee_name = request.form.get('name_list')

                    daily_salary = db.child(employee_name).child("daily_salary").get()
                    daily_salary = daily_salary.val()

                    remaining_amount = db.child(employee_name).child("remaining_amount").get()
                    remaining_amount = remaining_amount.val()

                    work_status = request.form.get('options')
                    overTimeHrs = request.form.get('over_time')

                    days_worked = db.child(employee_name).child('days_worked').get()
                    days_worked = days_worked.val()

                    overtime_total = db.child(employee_name).child('overtime_hrs_payment').get()
                    overtime_total = overtime_total.val()

                    if work_status == "option1":
                        add_days_worked = days_worked + 1
                        remaining_amount = daily_salary+remaining_amount
                        overtime_amt = daily_salary/8
                        overTimeHrs = int(overTimeHrs)
                        overtime_amt_day = overtime_amt*overTimeHrs
                        final_amount = overtime_amt_day+remaining_amount

                        overtime_total = overtime_amt_day +overtime_total

                        db.child(employee_name).child("overtime_hrs_payment").set(overtime_total)
                        db.child(employee_name).child("remaining_amount").set(final_amount)
                        db.child(employee_name).child('days_worked').set(add_days_worked)
                    elif work_status == "option2":
                        overtime_amt = daily_salary/8
                        overTimeHrs = int(overTimeHrs)
                        overtime_amt_day = overtime_amt*overTimeHrs
                        final_amount = overtime_amt_day+remaining_amount
                        overtime_total = overtime_amt_day +overtime_total
                        db.child(employee_name).child("overtime_hrs_payment").set(overtime_total)
                        final_amount = overtime_amt_day+remaining_amount
                        db.child(employee_name).child("remaining_amount").set(final_amount)

                elif request.form['btn'] == 'Reset Employee':
                    name = request.form.get('name_list')
                    db.child(name).child("advance_total").set(0)
                    db.child(name).child("days_worked").set(0)
                    db.child(name).child("overtime_hrs_payment").set(0)
                    db.child(name).child("remaining_amount").set(0)

                elif request.form['btn'] == 'Reset All Employees':
                    for employee in employee_list:
                        db.child(employee).child("advance_total").set(0)
                        db.child(employee).child("days_worked").set(0)
                        db.child(employee).child("overtime_hrs_payment").set(0)
                        db.child(employee).child("remaining_amount").set(0)
                return render_template('daily_work.html',employees = employee_list)
        
            return render_template('daily_work.html',employees = employee_list)
    else:
        return redirect(url_for("login"))


@app.route("/logout/")
def logout():
    session.pop("email",None)
    return redirect(url_for("login")) 
            

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
