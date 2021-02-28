from flask import Flask, request, render_template, jsonify, redirect
from forms_tree import RegForm
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY=b'Jimmy cracked eggs, with Samson and Diana, and Hucklebanana Jim')
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def sign_in():
    form = RegForm(request.form)
    if request.method == 'POST': #and form.validate_on_submit():
        name = form.user_id
        password = form.password
        sign_in.logged_dict = {'userid': name, 'password':password} 
        return redirect('/inside')
    return render_template('new_user.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm(request.form)
    if request.method == 'POST': #and form.validate_on_submit():
        name_first = form.name_first
        name_last = form.name_last
        password = form.password
        confirm_password = form.password_confirm
        register.registered_dict = {'First name': name_first, 'Last name': name_last,'password':password }
        if (password.data == confirm_password.data):                      #form.validate():
          return redirect('/')
        else:
          return "Passwords must match."
    return render_template('new_register.html', form=form)

@app.route('/logged', methods=['GET', 'POST'])
def loggedin():
  return jsonify(sign_in.logged_dict)

@app.route('/regged', methods=['GET', 'POST'])
def reggedin():
  return jsonify(register.registered_dict)

@app.route('/inside')
def entrance():
  return "Welcome"

if __name__ == '__main__':
    app.run(debug = True)