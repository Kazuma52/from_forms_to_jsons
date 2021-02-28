# model.py
from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import Form
class RegForm(Form):
  user_id = StringField('User Id', [validators.DataRequired()])
  name_first = StringField('First Name', [validators.DataRequired()])
  name_last = StringField('Last Name', [validators.DataRequired()])
  email = StringField('Email Address', [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
  password = StringField('Password', [validators.DataRequired()] )
  #password = PasswordField('Password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords must match') ])
  #confirm = PasswordField('Repeat Password')
  password_confirm = StringField('Confirm Password', [validators.DataRequired(), validators.EqualTo('password', message = 'not match')] )
  submit = SubmitField('Submit')
 
