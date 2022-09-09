from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from app import db, Ticket
from datetime import datetime
from app.utils.queries import Query
from app.utils.managers import DbManager
from app.models.models import Group
from app.utils.util_methods import session_active, get_ticket_by_title
from app.utils.email_notification import send_notification

new_request = Blueprint("new_request", __name__)
db_man = DbManager(db)


@new_request.route('/new-request', methods=["POST", "GET"])
def new_request1():
    if session_active():
        return render_template('new-request.html', user=session["user"], groups=Query.find_all_without_condition(Group))



@new_request.route('/process-request', methods=["POST"])
def process_request():
    db_man.add_record(Ticket(session["user"], request.form["title"], datetime.now(), int(request.form["group"]), request.form["description"],
                             request.form["priority"], True))
   
    #Disabled, as there could be a security breach, taking into consideration that the password is not encrypted now
    #send_notification(get_ticket_by_title(request.form["title"]))
    
    flash('Your ticket has been added successfully', "success")
    return redirect(url_for('home.display_home_page'))
