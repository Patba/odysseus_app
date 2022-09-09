from flask import Blueprint, render_template, session, redirect, url_for
from app.utils.util_methods import get_user_tickets_with_condition, session_active

home = Blueprint("home", __name__)


@home.route('/')
def display_home_page():
    if session_active():
        tickets = get_user_tickets_with_condition(session["user_id"], True)
        ticket_added = False if session.get("ticket_added", False) is False else True
        session["ticket_added"] = False
        return render_template('home.html', tickets=tickets)
    return redirect(url_for('user.get_access'))
