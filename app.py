from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create Database
def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll_no TEXT,
        name TEXT,
        subject1 INTEGER,
        subject2 INTEGER,
        subject3 INTEGER,
        total INTEGER,
        percentage REAL,
        grade TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()

# Home Page
@app.route('/')
def index():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    return render_template('index.html', students=students)

# Add Student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':

        roll_no = request.form['roll_no']
        name = request.form['name']

        s1 = int(request.form['subject1'])
        s2 = int(request.form['subject2'])
        s3 = int(request.form['subject3'])

        total = s1 + s2 + s3

        percentage = (total / 300) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "F"

        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students
        (roll_no, name, subject1, subject2, subject3,
        total, percentage, grade)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (roll_no, name, s1, s2, s3,
         total, percentage, grade))

        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('add_student.html')

# Delete Student
@app.route('/delete/<int:id>')
def delete_student(id):

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
