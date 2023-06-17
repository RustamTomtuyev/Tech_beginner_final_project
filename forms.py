from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,BooleanField,IntegerField
from wtforms.validators import DataRequired, Email, Length , EqualTo


class contactform(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    subject = StringField('subject', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(),Email()])
    message=TextAreaField('message',validators=[DataRequired()])


class Registerform(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=20)])
    password_check=PasswordField('password_check', validators=[DataRequired(),EqualTo('password')])

    
        
class Login(FlaskForm):
    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])

class message(FlaskForm):
    message=TextAreaField('message',validators=[DataRequired()])

class favorit(FlaskForm):
    is_active = BooleanField('name', default=False)

class search(FlaskForm):
    search = StringField('search', validators=[DataRequired()])  


class Newsletterform(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(),Email()])