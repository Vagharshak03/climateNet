from flask import Flask
app = Flask(__name__)

@app.route('/test')
def first_page():
    button = "<a href='/my_page' target='_blank'><button type='button'>My page</button>"
    return button

@app.route('/my_page')
def second_page():
    button = "<a href='/test' target='_blank'><button type='button'>Test</button>"
    return button

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
