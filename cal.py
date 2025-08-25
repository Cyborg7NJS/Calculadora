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
    elif op == 10:
        n1 = float(request.form.get("n1", 0))
        n2 = float(request.form.get("n2", 0))
        L = math.log(n1, n2)
        resultado = f'O logaritmo de {n1} na base {n2} é {round(L, 2)}'



    elif op == 11:
        try:
            n1 = int(request.form.get("n1", 0))
            if n1 < 0:
                resultado = "Fatorial não definido para números negativos."
            elif n1 == 0:
                resultado = "O fatorial de 0 é 1."
            elif n1 > 20:
                resultado = "Número muito grande para calcular o fatorial."
            else:
                F = math.factorial(n1)
                resultado = f'O fatorial de {n1} é {F}'
        except ValueError:
            resultado = "Por favor, insira um número inteiro válido."

    elif op == 12:  
        n1 = float(request.form.get("n1", 0))
        L = math.log(n1)
        resultado = f'O logaritmo natural (ln) de {n1} é {round(L, 4)}'

    elif op == 13:  
        n1 = float(request.form.get("n1", 0))
        L = math.log10(n1)
        resultado = f'O logaritmo decimal (log10) de {n1} é {round(L, 4)}'

    elif op == 14: 
        n1 = float(request.form.get("n1", 0))
        E = math.exp(n1)
        resultado = f'e elevado a {n1} é {round(E, 4)}'

    elif op == 15:  
        n1 = float(request.form.get("n1", 0))
        P = n1 * math.pi
        resultado = f'{n1} vezes π é {round(P, 4)}'

    elif op == 16:  
        n1 = float(request.form.get("n1", 0))
        E = n1 * math.e
        resultado = f'{n1} vezes e é {round(E, 4)}'

    elif op == 17:  
        n1 = int(request.form.get("n1", 0))
        n2 = int(request.form.get("n2", 0))
        resultado = f'O MDC entre {n1} e {n2} é {math.gcd(n1, n2)}'

    elif op == 18:  
        n1 = int(request.form.get("n1", 0))
        n2 = int(request.form.get("n2", 0))
        resultado = f'O MMC entre {n1} e {n2} é {math.lcm(n1, n2)}'

    elif op == 19:  
        n1 = int(request.form.get("n1", 0))
        n2 = int(request.form.get("n2", 0))
        resultado = f'O número de combinações C({n1}, {n2}) é {math.comb(n1, n2)}'

    elif op == 20:  
        n1 = int(request.form.get("n1", 0))
        n2 = int(request.form.get("n2", 0))
        resultado = f'O número de permutações P({n1}, {n2}) é {math.perm(n1, n2)}'

    elif op == 21:  
        n1 = float(request.form.get("n1", 0))
        A = math.degrees(math.asin(n1))
        resultado = f'O arco seno de {n1} é {round(A, 2)}°'

    elif op == 22:  
        n1 = float(request.form.get("n1", 0))
        A = math.degrees(math.acos(n1))
        resultado = f'O arco cosseno de {n1} é {round(A, 2)}°'

    elif op == 23:  
        n1 = float(request.form.get("n1", 0))
        A = math.degrees(math.atan(n1))
        resultado = f'O arco tangente de {n1} é {round(A, 2)}°'


    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)