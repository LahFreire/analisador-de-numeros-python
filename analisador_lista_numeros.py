

# função que recebe a lista de números do usuário

def obter_lista_numeros():
    
    while True:
        entrada = input("Digite uma sequência de números separados por vírgula: ")

        try:
            lista = list(map(int, entrada.split(",")))
            if not lista:
                    print("Você inseriu uma lista vazia. Tente novamente:")
                    continue
            return lista
            break  # se der certo, sai do loop
        except ValueError:
                print("⚠️ Entrada inválida! Certifique-se de digitar apenas números separados por vírgula, como: 10,20,30")

# função que recebe a referência de média do usuário

def obter_ref_media():

    while True:
        entrada_2 = input("Digite agora um valor de referência para o que você acredita ser a média dos números: ")
        
        try:
            referencia = float(entrada_2)
            return referencia
            break
        except ValueError:
            print("⚠️ Entrada inválida! Certifique-se de digitar um número inteiro ou decimal")

# função que vai extrair e calcular estatísticas

def calcula_estatisticas(lista):
    
    maior = max(lista)
    menor = min(lista)
    media = float(sum(lista) / len(lista))
    soma = sum(lista)
    
    return (maior, menor, media, soma)

# função que compara o valor de referência com a média calculada e retorna uma mensagem para o usuário

def verifica_referencia(media, referencia):
    
    if (referencia > media):
        resultado = "você errou, seu valor de referência é maior que a média"
    elif (referencia < media):
        resultado = "você errou, seu valor de referência é menor que a média"
    else: 
        resultado = "você acertou em cheio, seu valor de referência é a média!"
        
    return (resultado)

# função que printa as estatísticas no prompt
        
def exibe_estatisticas(maior, menor, media, soma, referencia, resultado):

    print(f"""""
          Maior número = {maior}
          Menor número = {menor}
          Média = {media}
          Soma total = {soma}
          Referência da média = {referencia}
          """"")
    
    print("Quanto à média: " + resultado)
          

# função principal que executa o código e chama as funções auiliares
        
def main():
   while True:
       lista = obter_lista_numeros()
       referencia = obter_ref_media()
       maior, menor, media, soma = calcula_estatisticas(lista)
       resultado = verifica_referencia(media, referencia)
       exibe_estatisticas(maior, menor, media, soma, referencia, resultado)
       
       repetir = input("Deseja analisar outra lista? (s/n): ").strip().lower()
       if repetir != 's':
            print("👋 Programa encerrado. Até mais!")
            break
        
# inicia o programa

main()
    
