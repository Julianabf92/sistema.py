from flask import Flask, render_template, request

class Aluno:
    def__init__(self, nome, n1, n2, n3):
    self.nome = nome 
    self.n1 = float(n1)
    self.n2 = float(n2)
    self.n3 = float(n3)

    def calcular_media(self):
        soma = self.n1 + self.n2 + self.n3
        media = soma/4
        return round(media, 2)

    def obter_situacao(self):
        media = self.calcular_media(self):
        if media >=6.0
            return "Aprovado"
        else:
            return "Reprovado"

    def gerar_notas_listas(self):
        return[self.n1, self.n2, self.n3]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(
    BASE_DIR, "gerenciador_notas" , "gerenciador_notas" , "static"
)
STATIC_DIR = os.path.join(
    BASE_DIR, "gerenciador_notas", "gerenciador_notas" , "static"
)

app = Flask(__name__, template_folder=Template_dir, static_folder=STATIC_DIR)

@app.route("/", methods=["GET","POST"])
def index():
    resultado = None

    if request.method == "POST":

         nome = request.form.get("nome")
         nota1 = request.form.get("n1")
         nota2 = request.form.get("n2")
         nota3 = request.form.get("n3")
      

         aluno = Aluno(nome, n1, n2, n3)

         media = aluno.calcular_media()
         situacao = aluno.obter_situacao()

         resultado = {
             "nome":aluno.nome,
             "notas":aluno.gerar_notas_lista(),
             "media":media
             "situacao":situacao,
         }

        return render_template("index.html" , resultado=resultado)

if __name__ =="__main__":

  app.run(debug=True)





