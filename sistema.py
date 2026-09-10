from flask import Flask, render_template, request

class Aluno:
    def__init__(self, n1, n2, n3):
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