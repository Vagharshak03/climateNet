from flask import Flask
app = Flask(__name__)

@app.route('/prev_page')
def first_page():
    button = "<a href='/next_page' target='_blank'><button type='button'>Next page</button>"
    return button

@app.route('/next_page')
def second_page():
    button = "<a href='/prev_page' target='_blank'><button type='button'>Previous page</button>"
    return button

@app.route('/test')
def test():
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8484', debug=True)

