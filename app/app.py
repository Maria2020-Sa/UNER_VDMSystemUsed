from flask import Flask, render_template
from menu import * 
from model.form.transaccion_form import TransaccionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/form_page')
def form_page():
    form = TransaccionForm()
    return render_template('form.html', form=form)

@app.route('/guardar', methods=['POST'])
def submit():
    form = TransaccionForm()
    

if __name__ == '__main__':
    app.run(debug=True)


