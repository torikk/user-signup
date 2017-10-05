from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template('index.html',
    username = '',
    email = '',
    username_error = '',
    password_error = '',
    verify_error = '',
    email_error = '')
    

@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    password_confirm = request.form['password_confirm']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    emailverify = ''
    emailverify2 = ''

    #username
    if username == '':
        username_error = "That's not a valid username"
    else:
        if len(username) > 20:
            username_error = "That's not a valid username"
        elif len(username) < 3:
            username_error = "That's not a valid username"
        else:
            for i in username:
                if i == '':
                    username_error = "That's not a valid username"

    #password
    if password == '':
        password_error = "That's not a valid password"
    else:
        if len(password) > 20:
            password_error = "That's not a valid password"
        elif len(password) < 3:
            password_error = "That's not a valid password"
        else:
            for i in password:
                if i == ' ':
                    password_error = "That's not a valid password"            
    
    #password verification
    if password_confirm != password:
        verify_error = "Passwords don't match"

    if password_confirm == '':
        verify_error = "Passwords don't match"

    
    #email
    if email == '':
        emailverify = True
        emailverify2 = True
    else:
        if len(email) > 20:
                email_error = "That's not a valid email"
        elif len(email) < 3:
                email_error = "That's not a valid email"
        

        for i in email:
            if i == "@":
                emailverify = True
                    
            if i == ".":
                emailverify2 = True
            
            if i == " ":
                email_error = "That's not a valid email"
                
    if not emailverify or not emailverify2:
        email_error = "That's not a valid email"


        
    #redirect
    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('index.html',
        username=username,
        email=email,
        username_error=username_error, 
        password_error=password_error, 
        verify_error=verify_error, 
        email_error=email_error)

@app.route("/welcome", methods=['GET'])
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()

