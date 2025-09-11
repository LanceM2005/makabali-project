
#Flask creates the app, request gives access to data from incoming HTTP requests
from flask import Flask, request, render_template_string
#Initialize the flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

#<name is a URL parameter>
#If you visit something like /greet/Lance, "Lance"
#is passed into the "greet function"
@app.route('/greet/<name>')
def greet(name):
    #HTML uses Jinja syntax to insert "Lance" into the page dynamically"
    template = """
    <h1>Hello, {{ name }}!</h1>
    <p>This page is rendered with a Jinja template</p>
    """
    return render_template_string(template, name=name)

#Visiting /echo displays a simple HTML form
#/echo supports GET and POST methods, which are HTML protocols
@app.route('/echo', methods=['GET', 'POST'])
def echo():
    if request.method == 'POST':
        data = request.form.get('data')
        return f"You posted: {data}"
    return '''
    <form method="post">
        <input name="data" placeholder="Type something">
        <input type="submit">
    </form>
    '''

