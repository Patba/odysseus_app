from flask import Blueprint, render_template, request, flash
from app import db
from app.utils.managers import DbManager
from app.utils.util_methods import *

admin = Blueprint("admin", __name__)
db_man = DbManager(db)

@admin.route('/add_group')
def adding_group():
    if session_active():
        return render_template('add-group.html')
    return redirect(url_for("home.display_home_page"))

@admin.route('/new_group', methods=["POST"])
def new_group():
    if request.method == "GET":
        return render_template("add-group.html")

    if Query.find_first(Group, {"name": request.form["group"]}):
        flash("Group already exists!", "warning")
        return redirect(url_for('admin.adding_group'))
    db_man.add_record(Group(request.form["group"]))
    flash('Group has been added successfully!', 'success')
    return redirect(url_for('home.display_home_page'))


@admin.route('/add-user', methods=["POST", "GET"])
def new_user():
    if request.method == "GET":
        return render_template("add-user.html", user=get_session_user(),
                               departments=Query.find_all_without_condition(Group))

    potential_user = Query.find_first(User, {"username": request.form["username"]})
    if potential_user:
        return render_template("add-user.html", user_err=True, user=get_session_user(),
                               departments=Query.find_all_without_condition(Group))
    new_user_record = User(request.form["username"], request.form["password"])
    db_man.add_record(new_user_record)
    for department_id in request.form.getlist('departments'):
        db_man.add_record(UserGroup(new_user_record.id, department_id))
    return render_template("add-user.html", user=get_session_user(), user_added=True,
                           departments=Query.find_all_without_condition(Group))

