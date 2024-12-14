from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignupForm(FlaskForm):
    username = StringField('사용자 이름', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('비밀번호 확인', validators=[DataRequired(), EqualTo('password')])
    accept_terms = BooleanField('이용약관에 동의합니다.', validators=[DataRequired()])
    submit = SubmitField('회원가입')

class LoginForm(FlaskForm):
    email = StringField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired()])
    submit = SubmitField('로그인')