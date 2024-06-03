from flask import Flask, render_template, request
from forms import QRForm
from generate_qr import generate_qr_code

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = QRForm()
    if form.validate_on_submit():
        link = form.link.data
        image = form.image.data
        if link:
            qr_code = generate_qr_code(link)
        elif image:
            # Handle image upload and generate QR code
            pass
        else:
            # Handle case where neither link nor image is provided
            pass
        return render_template('result.html', qr_code=qr_code)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
