from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from pybo.models import User
from pybo import db
from pybo.forms import PasswordForm
from pybo.views.main_views import permission_required

bp = Blueprint("admin", __name__, url_prefix="/admin")

@bp.route("/list/", methods=["GET", "POST"])
@permission_required(["admin"])
def _list():
    users = User.query.all()
    password_form = PasswordForm(request.form)

    if request.method == "POST":
        user_id = request.form.get("user_id")
        new_level = request.form.get("level")
        user = User.query.get(user_id)

        # 비밀번호가 입력된 경우에만 비밀번호 검증 및 업데이트
        if password_form.password1.data or password_form.password2.data:
            if password_form.validate_on_submit():
                user.password = generate_password_hash(password_form.password1.data)
            else:
                # 검증 실패 시 에러 메시지와 함께 폼 재렌더링
                flash("비밀번호가 조건에 맞지 않습니다. 다시 시도해 주세요.", "danger")
                return render_template("admin/admin.html", users=users, password_form=password_form)
        else:
            # 비밀번호를 입력하지 않은 경우 비밀번호를 변경하지 않고 레벨만 변경
            flash("비밀번호는 변경되지 않았습니다.")

        # 레벨 업데이트
        if new_level:
            user.level = new_level

        db.session.commit()
        flash("사용자 정보가 성공적으로 변경되었습니다.")
        return redirect(url_for("admin._list"))

    return render_template("admin/admin.html", users=users, password_form=password_form)
