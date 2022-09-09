from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from app import db
from app.utils.managers import DbManager, RequestDepartments
from app.utils.util_methods import session_active

my_departments = Blueprint("my_departments", __name__)
db_man = DbManager(db)


@my_departments.route("/my-departments", methods=["GET", "POST"])
def show_my_departments():
    if session_active():
        departments = RequestDepartments(session["user_id"], session["user_id"]).departments
        return render_template("my-departments.html", departments=departments)
    return redirect(url_for("home.display_home_page"))
