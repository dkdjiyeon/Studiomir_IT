from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, DateField
from wtforms.validators import DataRequired, Length, EqualTo


# 내용이 올바르게 입력됐는지 체크하는 것
class QuestionForm(FlaskForm):
    subject = StringField("제목", validators=[DataRequired("제목은 필수입력 항목입니다.")])
    content = TextAreaField("내용", validators=[DataRequired("내용은 필수입력 항목입니다.")])


class AnswerForm(FlaskForm):
    content = TextAreaField("내용", validators=[DataRequired("내용은 필수입력 항목입니다.")])


class UserCreateForm(FlaskForm):
    userid = StringField("아이디", validators=[DataRequired(), Length(min=1, max=25)])
    username = StringField("사용자이름", validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField("비밀번호", validators=[DataRequired(), EqualTo("password2", "비밀번호가 일치하지 않습니다"), ])
    password2 = PasswordField("비밀번호확인", validators=[DataRequired()])


class UserLoginForm(FlaskForm):
    userid = StringField("아이디", validators=[DataRequired(), Length(min=1, max=25)])
    # username = StringField("사용자이름", validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField("비밀번호", validators=[DataRequired()])


class ProductForm(FlaskForm):
    kind = StringField("종류", validators=[DataRequired("종류는 필수입력 항목입니다.")])
    product_name = StringField("제품명", validators=[DataRequired("제품명은 필수입력 항목입니다.")])
    buy_date = DateField("구매일", format="%Y-%m-%d", validators=[DataRequired("구매일은 필수입력 항목입니다.")], )


class ItemForm(FlaskForm):
    name = StringField("종류", validators=[DataRequired("종류는 필수입력 항목입니다.")])
