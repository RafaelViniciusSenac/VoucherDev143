from bingo import Bingo
from sorteio import Sorteador
from tkinter import *

def interface():
    jogo = Bingo()
    abaPrincipal = Tk()
    abaPrincipal.geometry("305x430")
    botoes = []
    textos = []
    sorteados = []

    class Botao:
        def __init__(self, texto, x, y):
            self.x = x + 1
            self.y = y
            self.botao = Button(abaPrincipal, text = texto, padx = 20, pady = 20, command = self.marcar, state = "active")
            self.botao.grid(row = x + 1, column = y)

        def marcar(self):
            jogo.marcarNumero(self.botao.cget("text"))
            self.botao = Label(abaPrincipal, text = "X", padx = 20, pady = 20)
            self.botao.grid(row = self.x, column = self.y)
            checar()

    def checar():
        if jogo.checarBingo():
            for b in botoes:
                b.botao["state"] = "disabled"

            for t in textos:
                t.destroy()

            sortearnumero.destroy()
            texto = Label(abaPrincipal, text = "BINGO!")
            texto.grid(row = 7, column = 2)
            jogardenovo = Button(abaPrincipal, text = "Gerar novo jogo", command = novoJogo)
            jogardenovo.grid(row = 8, column = 0, columnspan = 5)
            meio["state"] = "disabled"

    def novoJogo():
        abaPrincipal.destroy()
        interface()
    
    def sortear():
        num = Sorteador.sortear(1, 75)

        if len(sorteados) == 75:
            sortearnumero.destroy()
            numero = Label(abaPrincipal, text = f"Todos os números foram sorteados")
            numero.grid(row = 8, column = 0, columnspan = 5)
            textos.append(numero)
        
        elif num not in sorteados:
            sorteados.append(num)
            numero = Label(abaPrincipal, text = f"Número: {num}")
            numero.grid(row = 8, column = 0, columnspan = 5)
            textos.append(numero)

        else:
            sortear()

    for i in range(5):
        texto = Label(abaPrincipal, text = "BINGO"[i], padx = 20, pady = 20)
        texto.grid(row = 0, column = i)

        for x in range(5):
            if jogo.cartela[i][x] != "X":
                botao = Botao(jogo.cartela[i][x], i, x) 
                botoes.append(botao) 
                    
    meio = Label(abaPrincipal, text = "BINGO", state = "active")
    meio.grid(row = 3, column = 2)
    sortearnumero = Button(abaPrincipal, text = "Sortear número", command = sortear)
    sortearnumero.grid(row = 7, column = 0, columnspan = 5)
    
    abaPrincipal.mainloop()

interface()