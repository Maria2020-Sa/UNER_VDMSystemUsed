from flask import Flask, render_template
import webbrowser
from menu import * 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/form_page')
def form_page():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)


