from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint("main", __name__, url_prefix="/")


# 일정표
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


# 게시판
@bp.route("/question/list")
def question_page():
    return redirect(url_for("question._list"))
