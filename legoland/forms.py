from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, TextAreaField
from wtforms.validators import InputRequired, email, Length

# form used in basket


class CheckoutForm(FlaskForm):
    firstname = StringField("First name", validators=[
                            Length(min=1, max=20)])
    surname = StringField("Surname", validators=[
                          Length(min=1, max=20)])
    email = StringField("Email Address", validators=[
        InputRequired(message='Please provide a value'), email(message='Invalid email format'), Length(min=3, max=30)])
    phone = StringField("Phone number", validators=[
                        InputRequired(message='Please provide a value'), Length(min=5, max=13)])
    submit = SubmitField("Submit", render_kw={
                         'style': 'margin-top: 10px; background-color: #dc3545; color:#fff'})


class SupportForm(FlaskForm):
    email = StringField("Email Address", validators=[
        InputRequired(message='Please provide a value'), email(message='Invalid email format'), Length(min=3, max=30)])
    phone = StringField("Phone number", validators=[
                        InputRequired(message='Please provide a value'), Length(min=5, max=13)])
    question = TextAreaField("Question", render_kw={
        'style': 'min-height: 180px;'}, validators=[
        InputRequired(message='Please provide your question'), Length(min=5, max=400)])
    submit = SubmitField("Submit", render_kw={
                         'style': 'margin-top: 10px; background-color: #dc3545; color:#fff'})
