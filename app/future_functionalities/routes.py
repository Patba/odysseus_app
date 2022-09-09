from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from app import db
from app.utils.managers import DbManager, RequestDepartments
from app.utils.util_methods import session_active

future_functionalities = Blueprint("future_functionalities", __name__)
db_man = DbManager(db)


@future_functionalities.route("/future", methods=["GET", "POST"])
def show_my_departments():
        flash('Functionality will be added soon', 'warning')
        return redirect(url_for("home.display_home_page"))