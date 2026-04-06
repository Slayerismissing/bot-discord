# ============== DEFINIR AS COISAS =====================
#origem e classe
classes_validas = ["combatente", "ocultista", "especialista"]
origens_validas = ["lutador", "academico", "policial"]

#vida base e por nex

vidas_base = {
    "combatente":20,
    "ocultista":15,
    "especialista":18
}
vida_por_nex = {
    "combatente":5,
    "ocultista":3,
    "especialista":4
}


# perícias por classe
pericias_classe = {
    "combatente": ["luta", "fortitude"],
    "ocultista": ["ocultismo", "vontade"],
    "especialista": ["pontaria", "reflexos"]
}
pericias_origem = {
    "lutador": ["atletismo", "intimidação"],
    "acadêmico": ["investigação", "ciências"],
    "policial": ["percepção", "pontaria"]
}


# ================= FUNÇÕES ========================
def perguntar_opcao(mensagem, opcoes_validas):
    while True:
        print("\nOpções disponíveis: ")
        for opcao in opcoes_validas:
            print("-", opcao)
        
        escolha = input(mensagem)

        if escolha.lower() in opcoes_validas:
            return escolha.lower()
        else:
            print("Opção inválida. Tente novamente.")



def calcular_vida(classe, nex):
    base = vidas_base[classe]
    incremento = vida_por_nex[classe]

    return base + (nex * incremento)


def calcular_pericias(classe, origem):
    lista_classe = pericias_classe[classe]
    lista_origem = pericias_origem[origem]

    todas = lista_classe + lista_origem

    todas = list(set(todas))

    return todas