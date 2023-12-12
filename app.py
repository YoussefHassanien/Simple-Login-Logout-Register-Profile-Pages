from flask import Flask, render_template, request, redirect, session
import psycopg2.extras

app = Flask(__name__)
app.secret_key = "queensqueries"

database_session = psycopg2.connect(
     database="profiledata",
     port=5432,
     host="localhost",
     user="postgres",
     password="8383"
)

cursor = database_session.cursor(cursor_factory=psycopg2.extras.DictCursor)


@app.route("/", methods=["GET", "POST"])
def home():
    biography = "Please tell us more about you!"
    activity1 = "I love Rebecca!"
    activity2 = "I love Rebecca!"
    activity3 = "I love Rebecca!"
    userprofileimage = "../static/Images/44-facts-about-rebecca-ferguson-1690782435.jpg"
    status = "Online"
    return render_template("Profile.html", biography=biography, activity1=activity1, activity2=activity2,
                           activity3=activity3, userprofileimage=userprofileimage, status=status)


@app.route("/login", methods=["GET", "POST"])
def login():
    message = ''
    useremail = request.form.get("email")
    userpassword = request.form.get("password")
    if useremail:
        cursor.execute('SELECT * FROM usersinformation where email = %s and password = %s', (useremail, userpassword))
        result = cursor.fetchone()
        if result:
            session['user'] = dict(result)
            return redirect('/')
        else:
            message = 'Please enter correct email and password'
    return render_template('Login.html', msg=message)


@app.route("/register", methods=["GET", "POST"])
def register():
    message = ''
    userfname = request.form.get("Fname")
    userlname = request.form.get("Lname")
    userphone = request.form.get("phone")
    useraddress = request.form.get("address")
    useremail = request.form.get("email")
    userpassword = request.form.get("password")
    userjob = request.form.get("job")
    userfacebook = request.form.get("facebook")
    usergithub = request.form.get("github")
    userinstagram = request.form.get("instagram")
    userlinkedin = request.form.get("linkedin")

    if useremail:
        cursor.execute('SELECT email FROM usersinformation where email = %s', (useremail,))
        if cursor.fetchone():
            message = 'Account already exits!'
        else:
            cursor.execute('INSERT INTO usersinformation(Fname, Lname, phone, Address, Email, password, Job, '
                           'Facebook, Github, Instagram, Linkedin) VALUES (%s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, '
                           '%s)', (userfname, userlname, userphone, useraddress, useremail, userpassword, userjob,
                                   userfacebook, usergithub, userinstagram, userlinkedin))
            database_session.commit()
            message = 'You have successfully registered!'

    return render_template("Registration.html", msg=message)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session['user'] = None
    return redirect('/login')


@app.route("/edit", methods=["GET", "POST"])
def edit_profile():
    return render_template("Edit Information.html")


if __name__ == '__main__':
    app.run()
