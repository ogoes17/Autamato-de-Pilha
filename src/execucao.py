class Algoz:

    def __init__(self, entrada, pilha, estado_inicial, epsilon):

        self.epsilon = epsilon
        self.entrada = entrada # entrada já é um vetor
        self.pilha = pilha
        self.estado_atual = estado_inicial


    def get_pilha(self):
        return self.pilha

    def get_entrada(self):
        return self.entrada[0]

    def shift(self):
        self.entrada = self.entrada[1:]

    def get_estado(self):
        return self.estado_atual

    def is_finished(self): 
        if self.estado_atual.is_final():
            return 1
    
        if self.pilha.is_empty() and len(self.entrada) == 0:
            return 1
    
    def execute(self, transicao):

        simbolo = transicao.get_simbolo_fita()
        if simbolo != self.epsilon:
            self.shift()

        pilha_pop = transicao.get_simbolos_pilha()
        if self.epsilon in pilha_pop:
            pilha_pop.remove(self.epsilon)
                
        for i in pilha_pop:
            self.pilha.pop()

        self.estado_atual = transicao.get_novo_estado()

        pilha_push = transicao.get_novos_simbolos_pilha()
        if self.epsilon in pilha_push:
            pilha_push.remove(self.epsilon)

        self.pilha.push(pilha_push)