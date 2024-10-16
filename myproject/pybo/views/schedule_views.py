from flask import Blueprint, render_template, jsonify, request
from pybo import db
from pybo.views.main_views import permission_required
from pybo.models import Schedule  # 스케줄 테이블 모델 정의 필요

bp = Blueprint("schedule", __name__, url_prefix="/schedule")



# 스케줄 리스트 페이지 렌더링
@bp.route('/list')
@permission_required(['admin'])
def _list():
    return render_template('schedule/schedule_list.html')

@bp.route('/events')
@permission_required(['admin'])
def events():
    schedules = Schedule.query.all()
    events = []
    if schedules:
        for schedule in schedules:
            events.append({
                'title': schedule.title,
                'start': schedule.start_date.strftime('%Y-%m-%d'),
                'end': schedule.end_date.strftime('%Y-%m-%d') if schedule.end_date else None
            })
    return jsonify(events)  # 빈 리스트라도 반환


@bp.route('/add', methods=['POST'])
def add_event():
    data = request.get_json()
    title = data.get('title')
    start_date = data.get('start')

    new_schedule = Schedule(title=title, start_date=start_date)
    db.session.add(new_schedule)
    db.session.commit()
    return jsonify({'success': True})