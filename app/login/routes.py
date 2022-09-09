from flask import Blueprint, session, request, render_template, redirect, url_for, flash
from app.utils.queries import *
from app import bcrypt


login = Blueprint("login", __name__)


@login.route('/login', methods=["GET"])
def get_access():
    if 'user' in session:
        flash(f"Welcome back {session['user']}", "success")
        return redirect(url_for("home.display_home_page"))
    return render_template('login.html')


@login.route('/verify', methods=["POST"])
def verify():
    potential_user = Query.find_first(User, {"username": request.form["username"]})
    print(potential_user)
    if potential_user:
        if bcrypt.check_password_hash(potential_user.password, request.form["password"]):
            session["user_id"] = potential_user.id
            session["user"] = potential_user.username
            session["logged_in"] = True
            return redirect(url_for('home.display_home_page'))
    return render_template("login.html", visibility=True)


@login.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login.get_access'))
