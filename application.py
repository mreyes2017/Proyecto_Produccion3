from lib2to3.pytree import convert
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session,url_for
from flask_session import Session
from tempfile import mkdtemp
from sqlalchemy import Integer
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
from clases.q import *
from clases.ROP import *
from clases.p import *
from clases.l4l2 import *

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQL("sqlite:///proyecto.db")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Escribe un nombre de usuario valido", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Escribe una contraseña valida", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE email = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Usuario o contraseña invalida", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["nombre"] = rows[0]["nombre1"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        user = request.form.get("username")
        nombre1 = request.form.get("nombre1")
        ps = request.form.get("password")
        psa =request.form.get("Cpassword")
        email = request.form.get("username")


        userE = db.execute("SELECT username FROM users WHERE username = :username",username=user)


        if not user:
            return apology("El campo usuario esta vacio",400 )
        elif not nombre1:
            return apology("El campo primer nombre esta vacio",400 )
        elif not email:
            return apology("El campo correo esta vacio",400 )
        elif not ps:
            return apology("El campo password esta vacio",400 )
        elif not psa:
            return apology("El campo password Again esta vacio",400 )
        elif ps != psa:
            return apology("Las contraseñas no coinciden",400 )
        elif not userE :
            rows = db.execute("INSERT INTO users (id,username,hash,nombre1,nombre2,apellido1,apellido2,email) values (NULL,:username,:hashh,:nombre1,:nombre2,:apellido1,:apellido2,:email) ",username = user, hashh=generate_password_hash(ps),nombre1=nombre1,nombre2="nombre2",apellido1="apellido1",apellido2="apellido2",email=email )
        else:
            return apology("El usuario ya existe",400 )



        return redirect("/login")
    





@app.route("/")
def template_test():
    return render_template('index.html')



@app.route("/modeloQ.html", methods=["GET","POST"])
def modeloq():
    if request.method == "POST":
        demanda = request.form.get("demanda")
        #print(demanda)
        Tdemanda = request.form.get("Tdemanda")
        #print(Tdemanda)
        costo_pedir = request.form.get("costo_pedir")
        #print(costo_pedir)
        costo_almacen = request.form.get("costo_almacen")
        #print(costo_almacen)
        costo_compra = request.form.get("costo_compra")
        #print(costo_compra)
        plazo_entrega = request.form.get("plazo")
        
        tipo_demanda = request.form.get("Tdemanda")

        qt = qr(float(demanda),float(costo_pedir),float(costo_almacen),float(costo_compra),float(tipo_demanda))
        und_optima = qt.calcular_q() #Imprimir
        m = n_pedidos(float(demanda),float(und_optima),float(tipo_demanda))
        np = m.calcula_n_pedidos() #Imprimir
        o = tiempo_entre_pedidos(float(Tdemanda),float(np))
        tp = o.tiempo_entre_pedido() #Imprimir
        my = costo_total(float(demanda),float(costo_pedir),float(costo_almacen),float(costo_compra),float(und_optima),float(tipo_demanda))
        ct = my.c_total() #Imprimir
        ro = ROP(float(demanda),float(plazo_entrega),float(tipo_demanda))
        calculo=ro.calcular_rop()

        return render_template("modeloQ.html", und_optima = und_optima, np = np, tp = tp, ct = ct ,calculo=calculo)
    else:
        return render_template("modeloQ.html")

@app.route("/ModeloSS.html")
def modeloss():
    return render_template("ModeloSS.html")

@app.route("/ModeloP.html", methods=["GET","POST"])
def modelop():
    if request.method == "POST":
      demanda = request.form.get("demanda")
      desviacion = request.form.get("desviacion")
      nivel= request.form.get("nivel_confianza")
      periodo= request.form.get("periodo_revision")
      tiempo= request.form.get("tiempo_entrega")
      inventario= request.form.get("inventario")
      
      p = pr(int(demanda),int(desviacion),int(periodo),int(tiempo),int(inventario),int(nivel))
      z = p.calcular_z()
      calculo = p.calcular_p()
      o = p.inventario_seguridad()
      return render_template("ModeloP.html",calculo=calculo,resumen=" La cantidad óptima para pedir del producto es de "+str(calculo)+" Unidades ademas, se recomienda hacer un nuevo pedido al proveedor cuando las existencias lleguen hasta "+str(o)+" Unidades",stock=o)
    else:
     return render_template("ModeloP.html")

@app.route("/lote_por_lote.html", methods=["GET","POST"])
def modelol4l():
    if request.method == "POST":
        nsemanas = request.form.get("cantidad_semanas")
        datos = lista_float(request.form.get("datos"))
        print(datos)
        costo_pieza = request.form.get("costo_pieza")
        costo_pedir = request.form.get("costo_pedir")
        tasa = request.form.get("tasa")
        l4ll = l4l(nsemanas,datos,float(costo_pieza),float(costo_pedir),float(tasa))
        resultado = l4ll.ltotal()
        print(resultado)
        return render_template("lote_por_lote.html", resultado = resultado)
    else:
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

@app.route("/Persecucion.html")
def modeloperse():
    return render_template("Persecucion.html")

@app.route("/PlanAgregado.html")
def modeloagre():
    return render_template("PlanAgregado.html")

if __name__ == '__main__':
    app.run(debug=True)
#def index():
    #if method.request == "POST":
     #   return "<p>Hello, World!</p>"
    #else:
     #    return "<p>Hello, World!</p>"
