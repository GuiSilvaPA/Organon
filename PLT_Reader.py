import numpy as np
import pandas as pd

class PLT_Reader():
    
    def __init__(self, path, tipo="Organon"):
        
        self.path = path
        self.tipo = tipo
        
        if self.tipo == "Organon":
            self.rows = 5
            
        if self.tipo == "Anatem":
            self.rows = 6

        self.get_data()
        self.get_values()
        self.get_names()
        
    def get_data(self):
        
        with open(self.path) as f:
            self.lines = f.readlines()
            
        self.var_num = int(self.lines[0].strip())
        self.var_num = int(self.var_num)

        # print("Numero de variaveis: ", self.var_num)

        self.resto = self.var_num % self.rows
        # print("Variaveis na ultima: ", self.resto)

        if self.resto > 0:
            self.num_linhas = int(self.var_num / self.rows) + 1
        else:
            self.num_linhas = int(self.var_num / self.rows)

        # print("Numero de linhas:    ", self.num_linhas)

        self.doc_size = int((len(self.lines) - 1 - self.var_num)/self.num_linhas)
        # print("Tamanho do documento:", self.doc_size)

        self.variaveis = np.zeros((self.var_num, self.doc_size))
        # print("Matriz de variaveis: ", self.variaveis.shape)
        
    def get_values(self):
        
        linha = 1
        cont = 0
        for i in range(self.var_num + 1, len(self.lines)):

            temporaria = self.lines[i].split()

            for e in range(len(temporaria)):
                self.variaveis[e + ((linha - 1)*self.rows), cont] = float(temporaria[e])



            if linha == self.num_linhas:
                linha = 1
                cont += 1
            else:
                linha += 1
        
    def get_names(self):
        
        self.var_dic = {}

        for i in range(1, self.var_num + 1):    
            self.var_dic[self.lines[i].rstrip()] = self.variaveis[i-1]

        # print(self.var_dic.keys())
        