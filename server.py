from flask import Flask
app = Flask(__name__)

@app.errorhandler(404)
def resource_not_found(e):
    return 'Sorry, no response. Try Again!'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say(name):
    # name_string = str(name)
    return "Hi " + name +"!"

@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    return f"{word} " *num

if __name__=="__main__":
    app.run(debug=True)