from flask import Blueprint, url_for, g ,redirect, session, request
from werkzeug.utils import redirect
from functools import wraps
from pybo.models import User

bp = Blueprint("main", __name__, url_prefix="/")


# 로그인 요구 데코레이터
def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

# 사용자 로그인 상태를 전역 g 객체에 저장하는 함수
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

# 사용자 권한 페이지
def permission_required(allowed_levels):
    def decorator(view):
        @wraps(view)
        def wrapped_view(**kwargs):
            # 로그인이 안된 경우 로그인 페이지로 리디렉션
            if g.user is None:
                return redirect(url_for('auth.login'))

            # 사용자의 레벨이 허용되지 않는 경우 권한 부족 페이지로 리디렉션
            if g.user.level.value not in allowed_levels:
                return redirect(url_for('auth.no_permission'))  # 권한 부족 페이지로 리디렉션

            return view(**kwargs)

        return wrapped_view

    return decorator


# 일정표
@bp.route("/")
@login_required
def board_page():
    return redirect(url_for("schedule._list"))


# 전산장비
@bp.route("/equipment/list")
@login_required
def data_page():
    return redirect(url_for("equipment._list"))


# 개인장비
@bp.route("/person/list")
@login_required
def person_page():
    return redirect(url_for("person._list"))


# 게시판
@bp.route("/question/list")
@login_required
def question_page():
    return redirect(url_for("question._list"))
