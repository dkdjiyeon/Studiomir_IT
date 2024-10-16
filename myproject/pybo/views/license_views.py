from flask import Blueprint, render_template
from pybo.views.main_views import permission_required

bp = Blueprint("license", __name__, url_prefix="/license")


@bp.route("/list/")
@permission_required(['admin'])
def _list():
    return render_template("license/license_list.html")
