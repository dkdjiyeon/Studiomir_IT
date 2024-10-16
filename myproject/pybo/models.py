from pybo import db
from enum import Enum
from sqlalchemy import Enum as SQLAEnum
from flask_sqlalchemy import SQLAlchemy

# 데이터 베이스에 저장될 항목들


question_voter = db.Table("question_voter",  # 첫 번째 인자로 테이블 이름을 전달
                          db.Column("user_id", db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"),
                                    primary_key=True, ),
                          db.Column("question_id", db.Integer, db.ForeignKey("question.id", ondelete="CASCADE"),
                                    primary_key=True, ), )

answer_voter = db.Table("answer_voter",
                        db.Column("user_id", db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"),
                                  primary_key=True, ),
                        db.Column("answer_id", db.Integer, db.ForeignKey("answer.id", ondelete="CASCADE"),
                                  primary_key=True, ), )

class UserLevelEnum(Enum):
    basic = "basic"
    read = "read"
    admin = "admin"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    level = db.Column(SQLAEnum(UserLevelEnum), default=UserLevelEnum.basic)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user = db.relationship("User", backref=db.backref("question_set"))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship("User", secondary=question_voter, backref=db.backref("question_voter_set"))


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id", ondelete="CASCADE"))
    question = db.relationship("Question", backref=db.backref("answer_set"))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user = db.relationship("User", backref=db.backref("answer_set"))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship("User", secondary=answer_voter, backref=db.backref("answer_voter_set"))


class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    kind = db.Column(db.String(50), nullable=False)
    person = db.Column(db.String(50))
    note = db.Column(db.Text())
    buy_date = db.Column(db.DateTime(), nullable=False)
    enroll_date = db.Column(db.DateTime())


class EquipmentList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)