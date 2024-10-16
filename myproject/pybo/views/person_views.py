from flask import Blueprint, render_template
from pybo.views.main_views import permission_required

bp = Blueprint("person", __name__, url_prefix="/person")


@bp.route("/list/")
@permission_required(['read','admin'])
def _list():
    return render_template("person/person_list.html")
