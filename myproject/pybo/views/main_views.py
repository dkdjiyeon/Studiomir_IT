from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint("main", __name__, url_prefix="/")


# 기본 페이지
@bp.route("/")
def board_page():
    return redirect(url_for("schedule._list"))


# 전산장비
@bp.route("/equipment/list")
def data_page():
    return redirect(url_for("equipment._list"))


# 개인장비
@bp.route("/person/list")
def person_page():
    return redirect(url_for("person._list"))


# 만든이 페이지
@bp.route("/creator")
def about_page():
    return redirect(url_for("creator._list"))
