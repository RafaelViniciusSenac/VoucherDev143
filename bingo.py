from sorteio import Sorteador

class Bingo:
    def __init__(self):
        numeros = [[], [], [], [], []]

        for i in range(5):
            linha = []
            intervalos = [[1, 15], [16, 30], [31, 45], [46, 60], [61, 75]]
            
            if i != 2:
                while len(linha) != 5:
                    num = Sorteador.sortear(intervalos[i][0], intervalos[i][1])

                    if num not in linha:
                        linha.append(num)

            else:
                while len(linha) != 4:
                    num = Sorteador.sortear(intervalos[i][0], intervalos[i][1])

                    if num not in linha:
                        linha.append(num)
                
                linha.insert(2, "X")

            for x in range(5):
                numeros[x].insert(i, linha[x])

        self.cartela = numeros

    def marcarNumero(self, numero):
        for i in range(5):
            for x in range(5):
                if self.cartela[i][x] == numero:
                    self.cartela[i][x] = "X"
                    return
        
    def checarBingo(self):
        countD1 = 0
        countD2 = 0
        indice = 0

        for i in range(5):
            countL = 0
            countC = 0

            for x in range(5):
                if self.cartela[i][x] == "X":
                    countL += 1
                
                if self.cartela[x][i] == "X":
                    countC += 1
            
            if countL == 5 or countC == 5:
                return True
            
        for h in range(5):
            if self.cartela[h][h] == "X":
                countD1 += 1
            
            if countD1 == 5:
                return True
        
        for k in range(4, -1, -1):
            if self.cartela[k][indice] == "X":
                countD2 += 1

            if countD2 == 5:
                return True
            
            indice += 1
