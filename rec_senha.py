import random
import string

# Banco de dados fictício para armazenar tokens e senhas
user_data = {}

# Função para gerar uma senha forte
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    strong_password = ''.join(random.choice(characters) for _ in range(length))
    return strong_password

# Função para gerar um token de recuperação de senha
def generate_token(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Função para simular o envio de e-mail de recuperação de senha
def send_recovery_email(email, token):
    print(f'Um e-mail de recuperação foi enviado para {email}.')
    print(f'Token de recuperação: {token}')

# Simulação de solicitação de recuperação de senha
def request_password_reset(email):
    token = generate_token()
    user_data[email] = token  # Atualiza o token na base de dados fictícia
    send_recovery_email(email, token)

# Simulação de redefinição de senha
def reset_password(email, token, new_password):
    # Simulação: verificando se o token é válido
    if user_data.get(email) == token:
        # Atualiza a senha na base de dados fictícia
        user_data[email] = new_password
        print('Sua senha foi redefinida com sucesso.')
    else:
        print('Token inválido.')

# Simulação do processo de recuperação de senha
def simulate_password_recovery():
    email = input("Insira o seu endereço de e-mail: ")

    # Simula a solicitação de recuperação de senha
    request_password_reset(email)

    # Solicitação do token
    token = input("Por favor insira o token recebido por e-mail: ")

    # Simula a redefinição de senha
    print("""\nSugestão para nova senha:
- Pelo menos um caractere maiúsculo.
- Pelo menos um caractere minúsculo.
- Pelo menos oito caracteres.
- Pelo menos um caractere especial, como !@#$%^&*()_-+=.\n""")
    new_password = input("Insira a nova senha: ")
    confirm_password = input("Confirme a nova senha: ")

    if new_password != confirm_password:
        print("As senhas não coincidem.")
    elif len(new_password) < 8:
        print("A senha é muito curta. Deve ter pelo menos 8 caracteres.")
    elif not any(char.isupper() for char in new_password):
        print("A senha deve incluir pelo menos um caractere maiúsculo.")
    elif not any(char.islower() for char in new_password):
        print("A senha deve incluir pelo menos um caractere minúsculo.")
    elif not any(char.isdigit() for char in new_password):
        print("A senha deve incluir pelo menos um dígito.")
    elif not any(char in string.punctuation for char in new_password):
        print("A senha deve incluir pelo menos um caractere especial.")
    else:
        reset_password(email, token, new_password)

# Executa a simulação
simulate_password_recovery()
