import time

from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__) #look for the static files

db = mysql.connector.connect( # to run the msql db
    host="localhost",
    user="root",
    password="Thor1991",
    database="barbershop"
)

cursor = db.cursor(dictionary=True) #to run sql commands in the code
haircut_id = request.form['haircut_id'] #to get the haircut id


@app.route('/') #the url route like localhost:5000
def index():
    return render_template('index.html')


@app.route('/client') #client booking page
def client():

    cursor.execute("SELECT * FROM barbers")
    barbers = cursor.fetchall()

    cursor.execute("SELECT * FROM haircuts")
    haircuts = cursor.fetchall()

    return render_template('client.html', barbers=barbers, haircuts=haircuts)


@app.route('/book', methods=['POST']) #barber booking route. 1 for barber_id, 2 for client_name, 3 for date, 4 for time
def book():
    barber_id = request.form['barber_id']
    client_name = request.form['client_name']
    date = request.form['date']
    time = request.form['time']
    

    check = """SELECT * FROM appointments 
               WHERE barber_id=%s AND appointment_date=%s AND appointment_time=%s""" #check if the appointment already exists in the db

    cursor.execute(check, (barber_id, date, time)) #execute the checking
    result = cursor.fetchone()

    if result:
        return "Time slot already booked!" #if the appointment is already booked, return msg

    sql = """INSERT INTO appointments
            (barber_id, client_name, haircut_id, appointment_date, appointment_time)
            VALUES (%s,%s,%s,%s,%s)"""

    cursor.execute(sql, (barber_id, client_name, haircut_id, date, time)) #execute into the db the appointment
    db.commit()

    return "Appointment booked successfully!" #msg if the appointment is booked successfully


@app.route('/barber') #path to the barber page see the appointments
def barber():
    cursor.execute("""
        SELECT a.client_name, a.appointment_date, a.appointment_time, b.barber_name
        FROM appointments a
        JOIN barbers b ON a.barber_id = b.barber_id
        ORDER BY appointment_date, appointment_time
    """) #gets all appointments for the barber name

    appointments = cursor.fetchall() #check appointments in the db

    return render_template('barber.html', appointments=appointments) #show the appointments in the barber page


if __name__ == '__main__': #run the app
    app.run(debug=True) #run the app 