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
        color = request.form['color'] # get selected color from form
        if link:
            qr_code = generate_qr_code(link, color) # pass color to generate_qr_code function
            return render_template('result.html', qr_code=qr_code)
        else:
            # Handle case where link is not provided
            return "Please provide a link"
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
