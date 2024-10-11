from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from pybo.forms import ProductForm, ItemForm
from pybo import db
from pybo.models import Equipment, EquipmentList

bp = Blueprint("equipment", __name__, url_prefix="/equipment")


@bp.route("/list/")
def _list():
    item_list = EquipmentList.query.order_by(EquipmentList.id.asc())
    return render_template("equipment/equipment_list.html", item_list=item_list)


@bp.route("/enroll/")
def enroll():
    form = ProductForm()
    return render_template("equipment/equipment_enroll.html", form=form)


@bp.route("/enroll_complete/", methods=("GET", "POST"))
def enroll_complete():
    form = ProductForm()
    if request.method == "POST" and form.validate_on_submit():
        equipment = Equipment(
            kind=form.kind.data,
            product_name=form.product_name.data,
            buy_date=form.buy_date.data, )
        db.session.add(equipment)
        db.session.commit()
        return redirect(url_for("equipment._list"))
    return render_template("equipment/equipment_enroll.html", form=form)


@bp.route("/add/")
def add():
    form = ItemForm()
    return render_template("equipment/equipment_add.html", form=form)


@bp.route("/add_complete/", methods=("GET", "POST"))
def add_complete():
    form = ItemForm()
    if request.method == "POST" and form.validate_on_submit():
        equipment_list = EquipmentList(name=form.name.data, )
        db.session.add(equipment_list)
        db.session.commit()
        return redirect(url_for("equipment._list"))
    return render_template("equipment/equipment_add.html", form=form)


@bp.route("/list/detail/<string:item>/")
def detail(item):
    product_list = Equipment.query.filter_by(item=item).all()
    return render_template("equipment/equipment_list.html", product_list=product_list)
