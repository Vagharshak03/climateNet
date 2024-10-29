from flask import Flask
app = Flask(__name__)

@app.route('/')
def first_page():
    button = "<a href='/next_page' target='_blank'><button type='button'>Next page</button>"
    return button

@app.route('/next_page')
def second_page():
    button = "<a href='/' target='_blank'><button type='button'>Previous page</button>"
    return button
