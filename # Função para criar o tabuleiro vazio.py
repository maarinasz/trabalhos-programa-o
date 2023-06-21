import tkinter as tk
from tkinter import messagebox
import random

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"
        self.jogadas = 0

        self.janela = tk.Tk()
        self.janela.title("Jogo da Velha")

        self.botoes = []
        for linha in range(3):
            linha_botoes = []
            for coluna in range(3):
                botao = tk.Button(self.janela, text=" ", width=10, height=5,
                                 command=lambda linha=linha, coluna=coluna: self.realizar_jogada(linha, coluna))
                botao.grid(row=linha, column=coluna)
                linha_botoes.append(botao)
            self.botoes.append(linha_botoes)

    def exibir_tabuleiro(self):
        for linha in range(3):
            for coluna in range(3):
                self.botoes[linha][coluna].config(text=self.tabuleiro[linha][coluna])

    def verificar_vitoria(self, jogador):
        # Verificar linhas
        for linha in self.tabuleiro:
            if linha.count(jogador) == 3:
                return True

        # Verificar colunas
        for coluna in range(3):
            if [self.tabuleiro[linha][coluna] for linha in range(3)].count(jogador) == 3:
                return True

        # Verificar diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == jogador:
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == jogador:
            return True

        return False

    def realizar_jogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jogadas += 1

            self.exibir_tabuleiro()

            if self.verificar_vitoria(self.jogador_atual):
                messagebox.showinfo("Fim de jogo", f"O jogador {self.jogador_atual} venceu!")
                self.janela.quit()
            elif self.jogadas == 9:
                messagebox.showinfo("Fim de jogo", "Empate!")
                self.janela.quit()
            else:
                self.jogador_atual = "O"
                self.realizar_jogada_bot()

    def realizar_jogada_bot(self):
        # Encontra uma posição vazia aleatória
        posicoes_vazias = []
        for linha in range(3):
            for coluna in range(3):
                if self.tabuleiro[linha][coluna] == " ":
                    posicoes_vazias.append((linha, coluna))

        linha, coluna = random.choice(posicoes_vazias)
        self.tabuleiro[linha][coluna] = self.jogador_atual
        self.jogadas += 1

        self.exibir_tabuleiro()

        if self.verificar_vitoria(self.jogador_atual):
            messagebox.showinfo("Fim de jogo" #código não completo, adicionar a função realizar_jogada_bot para que adversário controlado pelo computador faça sua jogada. 
                                    #depois encontramos todas as posições vazias no tabuleiro e armazenamos em posicoes_vazias
                                         #Em seguida, selecionamos aleatoriamente uma posição vazia usando random.choice(posicoes_vazias)
            #Em seguida, verificamos se o jogador atual venceu com a função verificar_vitoria. Se o jogador venceu, exibimos uma mensagem de fim de jogo informando o jogador vencedor. 
            # Caso contrário, verificamos se ocorreu um empate (todas as posições estão preenchidas e ninguém venceu). Se ocorreu um empate, exibimos uma mensagem informando o empate.