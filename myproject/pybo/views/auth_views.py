from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import User

import functools

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/signup/", methods=("GET", "POST"))
def signup():
    form = UserCreateForm()

    if request.method == "POST" and form.validate_on_submit():
        userid = User.query.filter_by(userid=form.userid.data).first()
        # 이메일로 필터를 걸어서 계정이 있는지 먼저 확인
        if not userid:
            user = User(
                username=form.username.data,
                password=generate_password_hash(form.password1.data),
                userid=form.userid.data,
                level= form.level.data
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("schedule._list"))
        else:
            flash("이미 존재하는 사용자입니다.")
    return render_template("auth/signup.html", form=form)


@bp.route("/login/", methods=("GET", "POST"))
def login():
    form = UserLoginForm()
    if request.method == "POST" and form.validate_on_submit():
        error = None
        userid = User.query.filter_by(userid=form.userid.data).first()
        if not userid:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(userid.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session["user_id"] = userid.id
            _next = request.args.get("next", "")
            if _next:
                return redirect(_next)
            else:
                return redirect(url_for("schedule._list"))

            return redirect(url_for("schedule._list"))
        flash(error)
    return render_template("auth/login.html", form=form)

@bp.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for("schedule._list"))

@bp.route("/no_permission/")
def no_permission():
    return render_template("auth/no_permission.html")



# @bp.before_app_request
# def load_logged_in_user():
#     user_id = session.get("user_id")
#     if user_id is None:
#         g.user = None
#     else:
#         g.user = User.query.get(user_id)
#
# def login_required(view):
#     @functools.wraps(view)
#     def wrapped_view(*args, **kwargs):
#         if g.user is None:
#             _next = request.url if request.method == "GET" else ""
#             return redirect(url_for("auth.login", next=_next))
#         return view(*args, **kwargs)
#
#     return wrapped_view
