from flask import Flask, render_template, request
from conversoes import converter

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/integrantes")
def integrantes():
    return render_template("integrantes.html")


@app.route("/conversor", methods=["GET", "POST"])
def conversor():
    resultado = None
    erro = None

    if request.method == "POST":
        numero = request.form.get("numero", "").strip()
        base_origem = request.form.get("base_origem", "")
        base_destino = request.form.get("base_destino", "")

        try:
            if not numero:
                raise ValueError("Digite um número para converter.")

            base_origem = int(base_origem)
            base_destino = int(base_destino)

            resultado = converter(numero, base_origem, base_destino)

        except (ValueError, TypeError):
            erro = (
                "Número inválido ou bases selecionadas incorretamente. "
                "Confira os dados e tente novamente."
            )

    return render_template(
        "conversor.html",
        resultado=resultado,
        erro=erro
    )


if __name__ == "__main__":
    app.run(debug=True)