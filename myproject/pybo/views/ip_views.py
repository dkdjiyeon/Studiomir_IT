from flask import Blueprint, render_template
from pybo.views.main_views import permission_required

bp = Blueprint("ip", __name__, url_prefix="/ip")


@bp.route("/list/")
@permission_required(['admin'])
def _list():
    return render_template("ip/ip_list.html")
