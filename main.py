from sistema import perguntar_opcao, classes_validas, origens_validas, calcular_vida
from gerar_pdf import gerar_pdf


nome = input("Digite o nome do jogador: ")


personagem = input("\nDigite o nome do seu personagem: ")


classe = perguntar_opcao(
    "Digite a classe do personagem: ", #parâmetro MENSAGEM
    classes_validas #parâmetro OPÇÃO VALIDA
)


origem = perguntar_opcao(
    "Digite a origem do personagem: ", #parâmetro MENSAGEM
    origens_validas #parâmetro OPÇÃO VALIDA
)
while True:
    try:
        nex = int(input("\nDigite o NEX do personagem (múltiplo de 5): "))
        if nex % 5 == 0:
            break
        else:
            print("O NEX precisa ser múltiplo de 5.")
    except ValueError:
        print("Digite apenas números.")


vida = calcular_vida(classe, nex)


dados = {
    "untitled130":classe,
    "untitled129":origem,
    "untitled1":personagem,
    "untitled2":nome,
    "untitled134":vida,
    "untitled131":nex
}

gerar_pdf(dados)

