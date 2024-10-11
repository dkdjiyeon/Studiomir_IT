from flask import Blueprint, render_template

bp = Blueprint("person", __name__, url_prefix="/person")


@bp.route("/list/")
def _list():
    return render_template("person/person_list.html")
