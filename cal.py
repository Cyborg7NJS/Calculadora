from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    op = int(request.form["operacao"])
    resultado = None

    if op == 1:
        n1 = float(request.form.get("n1", 0))
        n2 = float(request.form.get("n2", 0))
        resultado = n1 + n2

    elif op == 2:
        n1 = float(request.form.get("n1", 0))
        n2 = float(request.form.get("n2", 0))
        resultado = n1 - n2

    elif op == 3:
        n1 = float(request.form.get("n1", 0))
        n2 = float(request.form.get("n2", 0))
        resultado = n1 * n2

    elif op == 4:
        n1 = float(request.form.get("n1", 0))
        n2 = float(request.form.get("n2", 0))
        if n2 != 0:
            resultado = n1 / n2
        else:
            resultado = 'Isso é irresistível não é? O resultado é Infinito ou Indefinido'

    elif op == 5:
        n1 = float(request.form.get("n1", 0))
        n2 = float(request.form.get("n2", 0))
        R = n1 ** (1/n2)
        resultado = 'A raiz de ' + str(n1) + ' no índice ' + str(n2) + ' é ' + str(R)

    elif op == 6:
        n1 = float(request.form.get("n1", 0))
        n2 = float(request.form.get("n2", 0))
        P = math.pow(n1, n2)
        resultado = f'A potencia de {n1} com o expoente {n2} é: {P} '

    elif op == 7:
        n1 = float(request.form.get("n1", 0))
        S = math.sin(math.radians(n1))
        resultado = f'O seno de {n1} é {S}'

    elif op == 8:
        n1 = float(request.form.get("n1", 0))
        C = math.cos(math.radians(n1))
        resultado = f'O cosseno de {n1} é {C}'

    elif op == 9:
        n1 = float(request.form.get("n1", 0))
        T = math.tan(math.radians(n1))
        resultado = f'A tangente de {n1} é {T}'

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)