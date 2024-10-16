from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp, Optional


# 내용이 올바르게 입력됐는지 체크하는 것
class QuestionForm(FlaskForm):
    subject = StringField("제목", validators=[DataRequired("제목은 필수입력 항목입니다.")])
    content = TextAreaField("내용", validators=[DataRequired("내용은 필수입력 항목입니다.")])


class AnswerForm(FlaskForm):
    content = TextAreaField("내용", validators=[DataRequired("내용은 필수입력 항목입니다.")])


class UserCreateForm(FlaskForm):
    userid = StringField("아이디", validators=[DataRequired(), Length(min=1, max=25)])
    username = StringField("사용자이름", validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField(
        "비밀번호",
        validators=[
            DataRequired(),
            Length(min=8, message="비밀번호는 최소 8자 이상이어야 합니다."),
            Regexp(r'^(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])',
                message="비밀번호는 소문자, 숫자, 특수문자를 포함해야 합니다."
            ),
            EqualTo("password2", message="비밀번호가 일치하지 않습니다.")
        ]
    )

    password2 = PasswordField("비밀번호확인", validators=[DataRequired()])
    level = StringField("레벨", validators=[DataRequired(), Length(min=1, max=25)])

class PasswordForm(FlaskForm):
    password1 = PasswordField(
        '새 비밀번호',
        validators=[
            Optional(),  # 선택적 입력 허용
            Length(min=8, message="비밀번호는 최소 8자 이상이어야 합니다."),
            Regexp(
                r'^(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])',
                message="비밀번호는 소문자, 숫자, 특수문자를 포함해야 합니다."
            )
        ]
    )
    password2 = PasswordField(
        '비밀번호 확인',
        validators=[
            Optional(),  # 선택적 입력 허용
            EqualTo('password1', message="비밀번호가 일치하지 않습니다.")
        ]
    )
    submit = SubmitField('정보 변경')


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
