from flask import redirect, url_for, render_template, session, request
from flask import Blueprint
from models import InfoForm, Date, Details, Menu
from flask import Blueprint
from extensions import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/menu')
def menu():

    menu = Menu()
    fronts= menu.fronts
    ranks = menu.ranks
    names = menu.names
    contents_1 = menu.contents_1
    contents_2 = menu.contents_2
    contents_3 = menu.contents_3
    stats_1 = menu.stats_1
    stats_2 = menu.stats_2

    return render_template('menu.html', fronts=fronts, ranks=ranks,  names=names, contents_1=contents_1,
                contents_2=contents_2, contents_3=contents_3, stats_1=stats_1, stats_2=stats_2)

@main.route('/form', methods=['GET','POST'])
def form():
    # Instantiating form class
    form = InfoForm()
    
    # Performing form validation
    if form.validate_on_submit():
        bookdate = form.book_date.data
        guests = form.guests.data
        email = form.email.data
        
        # Ensuring even parity for number of guests 
        if int(guests) % 2 == 1:
            guests = guests + 1
            
        session['bookdate'] = bookdate
        session['guests'] = guests
        session['email'] = email
        
        # Checking for existing record in data base
        existing_date = Date.query.filter_by(book_date=bookdate).first()
        if not existing_date:
            
            # Creating and saving new data base objects
            new_book_date = Date(book_date=bookdate, guests_total=guests)
            new_detail = Details(email=email, guests=guests, date=new_book_date)
            db.session.add(new_book_date)
            db.session.commit()
            db.session.add(new_detail)
            db.session.commit()
            return redirect('success')
        else:
            
            # Summing up total number of guests
            old_total = existing_date.guests_total
            new_total = int(old_total) + int(guests)
            session['total'] = new_total
            
            # Ensuring that total number of guests does not exceed daily limit of 30 covers
            if new_total > 30:
                error = 'Sorry, we are already fully booked. Please choose a different date.'
                return render_template('form.html', error=error, form=form)
            else:
                existing_date.guests_total = new_total
                new_detail = Details(email=email, guests=guests, date=existing_date)
                db.session.add(new_detail)
                db.session.commit()    
                return redirect('success')
    return render_template('form.html', form=form)

@main.route('/success', methods=['GET','POST'])
def success():
    return render_template('success.html')

@main.route('/result', methods=['GET', 'POST'])
def result():
    try:
        if request.method == "POST":
            booking_date = request.form['date']
            
            # Querying data base for existing bookings on given date
            data = Date.query.filter_by(book_date=booking_date).first()
            total = data.guests_total
            data_id = data.id
            emails = Details.query.filter(Details.date_id == data_id).all()
            return render_template('result.html', total=total, emails=emails)
    except AttributeError:
        
        # Throwing an error if there are no records
        error = 'There are no bookings on the date you have selected!'
        return render_template('admin.html', error=error)
        

@main.route('/admin')
def admin():
    return render_template('admin.html')

# Custom error pages
@main.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
