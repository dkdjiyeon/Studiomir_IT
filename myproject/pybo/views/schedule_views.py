from flask import Blueprint, render_template

bp = Blueprint("schedule", __name__, url_prefix="/schedule")


@bp.route("/list/")
def _list():
    return render_template("schedule/schedule_list.html")
