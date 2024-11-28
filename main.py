# variaveis
usuarios = []
postagens = []
proximo_id_usuario = 1
proximo_id_postagem = 1

# funções
def resetar():
    global proximo_id_usuario
    global proximo_id_postagem
    global usuarios
    global postagens
    usuarios.clear()
    postagens.clear()
    proximo_id_usuario = 1
    proximo_id_postagem = 1

def criar_usuario(nome):
    global proximo_id_usuario
    if nome == '':
        raise Exception
    usuario = {
        'id':proximo_id_usuario,
        'nome':nome,
        'seguidores':[],
        'seguindo':[]
    }  
    usuarios.append(usuario)
    proximo_id_usuario += 1


def criar_postagem(usuario, texto):
    global proximo_id_postagem

    if texto == "":
        raise Exception

    try:
        encontrar_usuario_por_id(usuario)
        postagem = {
            'id': proximo_id_postagem,
            'usuario': usuario,
            'mensagem': texto,
            'curtidores':[]
        }
        postagens.append(postagem)
        proximo_id_postagem += 1
    except IndexError as error:
        raise IndexError

    
def seguir_usuario(usuario_seguidor, usuario_a_seguir):
    if usuario_seguidor == usuario_a_seguir:
        raise Exception

    encontrar_usuario_por_id(usuario_seguidor)['seguindo'].append(usuario_a_seguir)
    encontrar_usuario_por_id(usuario_a_seguir)['seguidores'].append(usuario_seguidor)

def curtir_postagem(usuario, postagem):
    if postagem <= 0 or postagem > len(postagens):
        raise IndexError("Postagem inexistente.") 
    postagem_obj = encontrar_postagem_por_id(postagem)
    if usuario in postagem_obj['curtidores']:
        raise Exception("Usuário já curtiu esta postagem.") 
    postagem_obj['curtidores'].append(usuario)

def comentar_postagem(usuario, postagem, texto):
    if postagem <= 0 or postagem > len(postagens):
        raise IndexError("Postagem inexistente.")
    if texto.strip() == "":
        raise ValueError("Texto do comentário não pode ser vazio.")
    
    postagem_obj = encontrar_postagem_por_id(postagem)
    if 'comentarios' not in postagem_obj:
        postagem_obj['comentarios'] = []
    postagem_obj['comentarios'].append({'usuario': usuario, 'texto': texto})

def encontrar_usuario_por_id(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            return usuario
    raise IndexError

def encontrar_postagem_por_id(post_id):
    return postagens[post_id - 1]

def excluir_usuario(user_id):
    global usuarios, postagens
    usuario = encontrar_usuario_por_id(user_id)
    usuarios[:] = [u for u in usuarios if u['id'] != user_id]
    postagens[:] = [p for p in postagens if p['usuario'] != user_id]
    for postagem in postagens:
        postagem['curtidores'] = [curtidor for curtidor in postagem['curtidores'] if curtidor != user_id]
        if 'comentarios' in postagem:
            postagem['comentarios'] = [comentario for comentario in postagem['comentarios'] if comentario['usuario'] != user_id]
# menu
def exibir_menu():
    while True:
        print("\n--- Menu ---")
        print("1. Criar Usuário")
        print("2. Criar Postagem")
        print("3. Seguir Usuário")
        print("4. Curtir Postagem")
        print("5. Comentar em Postagem")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            criar_usuario(nome)
            print("Usuário criado com sucesso!")
        
        elif opcao == "2":
            user_id = int(input("Digite o ID do autor da postagem: "))
            # usuario = encontrar_usuario_por_id(user_id)
            texto = input("Digite o texto da postagem: ")
            # criar_postagem(usuario, texto)
            print("Postagem criada com sucesso!")
        
        elif opcao == "3":
            user_id = int(input("Digite o seu ID: "))
            target_id = int(input("Digite o ID do usuário que deseja seguir: "))
            # seguir_usuario(user_id, target_id)
            print("Usuário seguido com sucesso!")
        
        elif opcao == "4":
            user_id = int(input("Digite o seu ID: "))
            post_id = int(input("Digite o ID da postagem que deseja curtir: "))
            # curtir_postagem(user_id, post_id)
            print("Postagem curtida com sucesso!")
        
        elif opcao == "5":
            user_id = int(input("Digite o seu ID: "))
            post_id = int(input("Digite o ID da postagem que deseja comentar: "))
            texto = input("Digite o texto do comentário: ")
            # comentar_postagem(user_id, post_id, texto)
            print("Comentário adicionado com sucesso!")
        
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


#exibir_menu()