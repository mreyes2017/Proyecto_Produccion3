from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
#def index():
    #if method.request == "POST":
     #   return "<p>Hello, World!</p>"
    #else:
     #    return "<p>Hello, World!</p>"
