from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Remove space and quotes that might break some copy/paste scenarios
    caracteres = caracteres.replace(' ', '').replace('"', '').replace("'", "")
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

@app.route("/", methods=["GET", "POST"])
def index():
    senha_gerada = None
    if request.method == "POST":
        try:
            tamanho = int(request.form.get("tamanho", 12))
            if tamanho < 4:
                tamanho = 4
            if tamanho > 100:
                tamanho = 100
        except:
            tamanho = 12
        incluir = request.form.get("incluir", "all")
        # For now the generator always uses letters+digits+punctuation; frontend filtering could be added.
        senha_gerada = gerar_senha(tamanho)
    return render_template("index.html", senha=senha_gerada)

if __name__ == "__main__":
    app.run(debug=True)
