from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import URL, InputRequired

class QRForm(FlaskForm):
    link = StringField('Link', validators=[URL()])
    image = FileField('Image')
    submit = SubmitField('Generate QR Code')
