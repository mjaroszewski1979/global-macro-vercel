from extensions import db
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, IntegerField, EmailField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField, ValidationError

# Custom validator for weekends exclusion
class WeekdayValidator(object):
    def __call__(self, form, field):
        if field.data and field.data.isoweekday() > 6:
            raise ValidationError("Sorry, we are closed on weekends. Please choose a different date.")

# Creating form class for booking system
class InfoForm(FlaskForm):
    book_date = DateField('Booking Date', format='%Y-%m-%d', validators=[WeekdayValidator(), DataRequired()])
    guests = IntegerField('Number of Guests', [validators.DataRequired(), validators.NumberRange(min=0, max=30, message='Sorry, maximum number of guests per day is 30.')])
    email = EmailField('Email Address', [validators.DataRequired()])
    submit = SubmitField('Book Now')

# Creating data base models with implementation of one-to-many relationship
class Date(db.Model):
    __tablename__ = 'date'
    id = db.Column(db.Integer, primary_key=True)
    book_date = db.Column(db.String(80), nullable=False)
    guests_total = db.Column(db.Integer, nullable=False)
    details_id = db.relationship('Details', backref='date', lazy=True)

    def __init__(self, book_date, guests_total):
        self.book_date = book_date
        self.guests_total = guests_total

    def __repr__(self):
        return f'<Date: {self.id} {self.book_date} {self.guests_total}>'

class Details(db.Model):
    __tablename__ = 'details'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    date_id = db.Column(db.Integer, db.ForeignKey('date.id'))

    def __repr__(self):
        return f'<Details: {self.id} {self.email} {self.guests}>'
    
class Menu:
    def __init__(self):
        
        self.fronts = ['food1.png', 'food2.png', 'food3.png']
        self.ranks = [1,2,3]
        self.names = ['3 Course Set', '6 Course Set', '9 Course Set']
        self.contents_1 = ['prawn2.png', 'prawn3.png', 'nut1.png']
        self.contents_2 = ['meat.png', 'fruit2.png', 'prawn1.png']
        self.contents_3 = ['cheese.png', 'nut2.png', 'fish4.png']
        self.stats_1 = ['50.00', '70.00', '90.00']
        self.stats_2 = ['100.00', '140.00', '180.00']
