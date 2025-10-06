from flask import Flask, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

class RegisterForm(FlaskForm):
    first_name = StringField('Primeiro Nome', validators=[DataRequired()])
    last_name = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email(message='E-mail inválido!')])
    password = PasswordField('Senha', validators=[InputRequired(), EqualTo('confirm', message='As senhas devem ser iguais!')])
    confirm = PasswordField('Confirme sua Senha', validators=[DataRequired()])
    submit = SubmitField('CADASTRAR')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return render_template('success.html', name=form.first_name.data)
    return render_template('register.html', form=form)




if __name__ == '__main__':
    app.run(debug=True, port=5152)
