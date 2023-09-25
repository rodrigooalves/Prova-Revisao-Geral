# Inicializa a lista vazia para armazenar os produtos
lista_de_compras = []
totalProdutos = 0

# Função para adicionar um produto à lista
def adicionar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    valor_unitario = float(input("Valor unitário: "))
    
    # Calcula o valor total do produto
    total_produto = quantidade * valor_unitario
    
    # Adiciona o produto à lista
    lista_de_compras.append({"produto": nome, "valor": valor_unitario, "quantidade": quantidade, "total": total_produto})
    
    # Atualiza o valor total de todos os produtos
    global totalProdutos
    totalProdutos += total_produto
    
    print(f"{nome} foi adicionado à lista.")

# Função para ver a lista de produtos
def ver_lista_de_produtos():
    if not lista_de_compras:
        print("A lista de compras está vazia.")
    else:
        print("Lista de produtos:")
        for produto in lista_de_compras:
            print(f"Produto: {produto['produto']}, Quantidade: {produto['quantidade']}, Valor unitário: {produto['valor']}, Total: {produto['total']}")
        print(f"Valor total de todos os produtos: {totalProdutos}")

# Função para atualizar informações de um produto
def atualizar_produto():
    nome = input("Nome do produto que deseja atualizar: ")
    
    for produto in lista_de_compras:
        if produto['produto'] == nome:
            quantidade = int(input("Nova quantidade: "))
            valor_unitario = float(input("Novo valor unitário: "))
            
            # Calcula o novo valor total do produto
            total_produto = quantidade * valor_unitario
            
            # Atualiza as informações do produto
            produto['quantidade'] = quantidade
            produto['valor'] = valor_unitario
            produto['total'] = total_produto
            
            # Atualiza o valor total de todos os produtos
            global totalProdutos
            totalProdutos -= produto['total']
            totalProdutos += total_produto
            
            print(f"As informações de {nome} foram atualizadas.")
            return
    print(f"Produto {nome} não encontrado na lista.")

# Função para remover um produto da lista
def remover_produto():
    nome = input("Nome do produto que deseja remover: ")
    
    for produto in lista_de_compras:
        if produto['produto'] == nome:
            global totalProdutos
            totalProdutos -= produto['total']
            lista_de_compras.remove(produto)
            print(f"{nome} foi removido da lista.")
            return
    print(f"Produto {nome} não encontrado na lista.")

# Loop principal do programa
while True:
    print("\nOpções:")
    print("1. Adicionar produtos")
    print("2. Ver a lista de produtos")
    print("3. Atualizar produtos")
    print("4. Remover produto")
    print("5. Encerrar programa")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        ver_lista_de_produtos()
    elif opcao == '3':
        atualizar_produto()
    elif opcao == '4':
        remover_produto()
    elif opcao == '5':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
