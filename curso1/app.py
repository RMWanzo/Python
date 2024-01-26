import os

restaurantes = [{'nome':'Niwa sushi', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizzaria Tropical', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cucina Italiana', 'categoria':'Italiano', 'ativo':False}]

def nome_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print("""𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
      """) # https://fsymbols.com/

def opcoes():
    '''Função para mostrar as opções de menu do programa.'''

    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar/Desativar Restaurante')
    print('4. exit\n')

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('Encerrando programa...')

def opcao_invalida():
    '''Função para mensagem de erro quando a opção for inválida'''
    
    print('Opção Invalida!')
    voltar_menu()

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''

    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_menu():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''

    input('\nDigite Enter para voltar ao Menu Principal. ')      
    main()

def cadastrar_restaurante():
    '''
    Essa função é responsavel por Cadastar um novo Restaurante
    
    INPUTs:
        - Nome do restaurante
        - Categoria
    OUTPUTs:
        - Adiciona o novo Restaurante na lista de Restaurantes
    '''
    
    exibir_subtitulo('Cadastro De Restaurantes')
    nome_do_restaurante = input('Digite o nome do Restaurante:\n')
    categoria = input(f'Digite a Categoria do Restaurante {nome_do_restaurante}:\n')
    dados_restaurante = {'nome':nome_do_restaurante,'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O Restaurante {nome_do_restaurante} foi cadastrado!')
    voltar_menu()

def listar_restaurantes():
    '''Essa função é responsavel por Listar os Restaurantes'''

    exibir_subtitulo('Listando Restaurantes')
    print(f'{'Nome do Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Situação'}\n')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)}  | {categoria.ljust(20)} | {ativo}')

    voltar_menu()

def estado_restaurante():
    '''
    Essa função é responsavel por Ativar ou Desativar um Restaurante
    
    INPUTs:
        - Nome do Restaurante
        - Situação (Ativar/Desativar)
    
    OUTPUTs:
        - Altera a situação do Restaurante na lista de Restaurantes
    '''

    exibir_subtitulo('ALterando estado do Restaurante\n')
    nome_restaurante = input('Digite o nome do Restaurante que deseja alterar o estado:\n')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_menu()

def escolher_opcao():
    '''
    Função para ler a opção escolhida pelo usuário no menu principal
    
    Retorna:
        - Executa opção escolhida pelo usuário como int
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicia o programa '''

    os.system('cls')
    nome_programa()
    opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
