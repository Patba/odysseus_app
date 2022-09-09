from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from app import db, bcrypt, User, UserGroup, Group
from app.utils.queries import Query
from app.utils.managers import DbManager
from app.utils.managers import UserManager
from app.utils.util_methods import get_user_group, session_active

settings = Blueprint("settings", __name__)
db_man = DbManager(db)


@settings.route('/user_settings', methods=["GET"])
def user_dashboard():
    if session_active():
        groups_id = [result.group_id for result in Query.find_all(UserGroup, {"user_id": session["user_id"]})]
        groups = [Query.find_first(Group, {"id": _id}) for _id in groups_id]
        return render_template('settings.html', groups=groups)
    return redirect(url_for("home.display_home_page"))


@settings.route('/change_password', methods=["POST"])
def change_password():
    user_to_change = UserManager(Query.find_first(User, {"username": session["user"]}))

    if bcrypt.check_password_hash(user_to_change.get_password(), request.form["current_password"]):
        user_to_change.update_password(request.form["new_password"])
        db_man.commit_changes()
        flash("Password has been successfully changed", "success")
        return redirect(url_for("home.display_home_page"))
    flash("Incorrect current password", "warning")
    return redirect(url_for("settings.user_dashboard"))


@settings.route('/change_email', methods=["POST"])
def change_email():
    user_to_change = UserManager(Query.find_first(User, {"user": session["user"]}))
    if user_to_change.get_email() == request.form["current_email"]:
        user_to_change.update_email(request.form["new_email"])
        db_man.commit_changes()
        flash("Email has been successfully changed", "success")
        return redirect(url_for("home.display_home_page"))
    flash("Incorrect current email", "warning")
    return redirect(url_for("settings.user_dashboard"))


# @settings.route('/change_email_notifications', methods=["POST"])
# def change_email():
#     user_to_change = UserManager(Query.find_first(User, {"username": session["user"]}))
#     option = request.form['email_options']
#     pass


