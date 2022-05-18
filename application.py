from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session,url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

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
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Usuario o contraseña invalida", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

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


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = request.form.get("username")
        nombre1 = request.form.get("nombre1")
        nombre2 = request.form.get("nombre2")
        apellido1 = request.form.get("apellido1")
        apellido2 = request.form.get("apellido2")
        ps = request.form.get("password")
        psa =request.form.get("Cpassword")
        email = request.form.get("email")


        userE = db.execute("SELECT username FROM users WHERE username = :username",username=user)


        if not user:
            return apology("El campo usuario esta vacio",400 )
        elif not nombre1:
            return apology("El campo primer nombre esta vacio",400 )
        elif not nombre2:
            return apology("El campo segundo nombre esta vacio",400 )
        elif not apellido1:
            return apology("El campo primer apellido esta vacio",400 )
        elif not apellido2:
            return apology("El campo segundo apellido esta vacio",400 )
        elif not email:
            return apology("El campo correo esta vacio",400 )
        elif not ps:
            return apology("El campo password esta vacio",400 )
        elif not psa:
            return apology("El campo password Again esta vacio",400 )
        elif ps != psa:
            return apology("Las contraseñas no coinciden",400 )
        elif not userE :
            rows = db.execute("INSERT INTO users (id,username,hash,nombre1,nombre2,apellido1,apellido2,email) values (NULL,:username,:hashh,:nombre1,:nombre2,:apellido1,:apellido2,:email) ",username = user, hashh=generate_password_hash(ps),nombre1=nombre1,nombre2=nombre2,apellido1=apellido1,apellido2=apellido2,email=email )
        else:
            return apology("El usuario ya existe",400 )



        return redirect("/")
    else:
        return render_template("val.html")





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
