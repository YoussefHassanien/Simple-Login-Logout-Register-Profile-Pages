from flask import Flask, render_template, request, redirect, session,send_from_directory
import psycopg2.extras

app = Flask(__name__)
app.secret_key = "queensqueries"

database_session = psycopg2.connect(
     database="profiledata",
     port=5432,
     host="localhost",
     user="postgres",
     password="Youssef.17.11"
)

cursor = database_session.cursor(cursor_factory=psycopg2.extras.DictCursor)

@app.route("/", methods=["GET", "POST"])
def home():
    return redirect('/login')

@app.route("/profile", methods=["GET", "POST"])
def profile():
    biography = request.form.get('biography')
    activity1 = request.form.get('act1')
    activity2 = request.form.get('act2')
    activity3 = request.form.get('act3')
    status = request.form.get("status")
    return render_template("Profile.html", biography=biography, activity1=activity1, activity2=activity2,
                           activity3=activity3, status=status)


@app.route("/login", methods=["GET", "POST"])
def login():
    message = ''
    useremail = request.form.get("email")
    userpassword = request.form.get("password")
    if useremail:
        cursor.execute('SELECT * FROM Usernew where email = %s and password = %s', (useremail, userpassword))
        result = cursor.fetchone()
        if result:
            session['user'] = dict(result)
            return redirect('/profile')
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
    userprofileimage = "../static/Images/blank-profile-picture-973460_960_720.webp"

    if useremail:
        cursor.execute('SELECT email FROM Usernew where email = %s', (useremail,))
        if cursor.fetchone():
            message = 'Account already exits!'
        else:
            cursor.execute('INSERT INTO Usernew(Fname, Lname, phone, Address, Email, password, Job, '
                           'Facebook, Github, Instagram, Linkedin, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                           (userfname, userlname, userphone, useraddress, useremail, userpassword, userjob,
                            userfacebook, usergithub, userinstagram, userlinkedin, userprofileimage))
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

@app.route("/Save Changes", methods=["GET", "POST"])
def save_changes():
    biography = request.form['biography']
    userfname = request.form.get("Fname")
    userlname = request.form.get("Lname")
    userphone = request.form.get("phone")
    useraddress = request.form.get("Adress")
    useremail = request.form.get("email")
    userpassword = request.form.get("password")
    userjob = request.form.get("job")
    userfacebook = request.form.get("Fb")
    usergithub = request.form.get("git")
    userinstagram = request.form.get("ig")
    userlinkedin = request.form.get("li")
    activity1 = request.form.get("act1")
    activity2 = request.form.get("act2")
    activity3 = request.form.get("act3")
    status = request.form.get("status")
    CurrentEmail = session["user"]["email"]
    userprofileimage = request.form.get("image")
    cursor.execute("SELECT email FROM Usernew WHERE email = %s", (CurrentEmail,))
    current_email = cursor.fetchone()[0]

    cursor.execute('UPDATE Usernew SET Fname= %s , Lname= %s , Phone= %s, Address= %s , Job= %s , Facebook= %s,Github= %s, Instagram= %s, Linkedin= %s, image= %s WHERE email= %s',(userfname,userlname,userphone,useraddress,userjob,userfacebook,usergithub,userinstagram,userlinkedin,userprofileimage,current_email))
    database_session.commit()
    cursor.execute("SELECT * FROM Usernew WHERE email = %s", (CurrentEmail,))
    newData = cursor.fetchone()
    session['user'] = dict(newData)
    return render_template("Profile.html", biography=biography, activity1=activity1, activity2=activity2,
                           activity3=activity3, status=status)



if __name__ == '__main__':
    app.run()
