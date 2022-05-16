from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('index.html')

@app.route("/modeloQ.html")
def modeloq():
    return render_template("modeloQ.html")

@app.route("/ModeloSS.html")
def modeloss():
    return render_template("ModeloSS.html")

@app.route("/ModeloP.html")
def modelop():
    return render_template("ModeloP.html")

@app.route("/lote_por_lote.html")
def modelol4l():
    return render_template("lote_por_lote.html")

@app.route("/cantidad_pedido_economica.html")
def modeloeoq():
    return render_template("cantidad_pedido_economica.html")

@app.route("/costo_total_minimo.html")
def modeloctm():
    return render_template("costo_total_minimo.html")

@app.route("/costo_unitario_minimo.html")
def modelocum():
    return render_template("costo_unitario_minimo.html")

if __name__ == '__main__':
    app.run(debug=True)
#def index():
    #if method.request == "POST":
     #   return "<p>Hello, World!</p>"
    #else:
     #    return "<p>Hello, World!</p>"
