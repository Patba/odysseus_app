from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from app import db, Ticket
from datetime import datetime
from app.utils.queries import Query
from app.utils.managers import DbManager
from app.models.models import Group, Note
from app.utils.util_methods import get_ticket_by_id

tickets = Blueprint("tickets", __name__)
db_man = DbManager(db)


@tickets.route('/view-ticket/<ticket_id>', methods=["GET"])
def view_ticket(ticket_id: str):
    ticket = get_ticket_by_id(ticket_id)
    department = Query.find_first(Group, {"id": ticket.group}).name
    notes = reversed(Query.find_all(Note, {"ticket_id": ticket.id}))
    return render_template("preview-ticket.html", ticket=ticket,
                           department=department, notes=notes)


@tickets.route('/add-note', methods=["POST"])
def add_note():
    ticket = Query.find_first(Ticket, {"id": request.form["ticket_id"]})
    db_man.add_record(Note(ticket_id=request.form["ticket_id"], owner=session["user"],
                           date=datetime.now(), content=request.form["content"],
                           closing=bool(request.form["final"])))

    ticket.is_open = bool(request.form["final"])
    db_man.commit_changes()
    if ticket.is_open:
        flash('Note has been added successfully', "success")
        return redirect(url_for('tickets.view_ticket', ticket_id=ticket.id))
    flash('Issue has been closed', "success")
    return redirect(url_for('home.display_home_page'))
