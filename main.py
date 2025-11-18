def login(usuario, senha):
    if not (4 <= len(usuario) <= 12):
        return "Erro: usuário deve ter entre 4 e 12 caracteres."

    if not (6 <= len(senha) <= 10):
        return "Erro: senha deve ter entre 6 e 10 caracteres."

    # BANCON DE DADOS: SIMULADO
    usuario_valido = "admin"
    senha_valida = "123456"

    if usuario == usuario_valido and senha == senha_valida:
        return "Login realizado com sucesso!"
    else:
        return "Erro: credenciais inválidas."


# -------------------------------
# TESTES: PARTICIONAMENTO
# -------------------------------
print("\n=== TESTES - PARTICIONAMENTO DE EQUIVALÊNCIA ===\n")

testes_particionamento = [
    ("abc", "123456"),                
    ("admin123", "123"),              
    ("usuarioMuitoGrande123", "123456"),  
    ("admin", "senhaMuitoGrande123"), 
    ("admin", "123456"),              
    ("admin", "999999"),              
]

for usuario, senha in testes_particionamento:
    print(f"Teste → Usuário: {usuario}, Senha: {senha}")
    print("Resultado:", login(usuario, senha))
    print("-" * 50)

# -------------------------------
# TESTES: VALOR LIMITE
# -------------------------------
print("\n=== TESTES - ANÁLISE DE VALOR LIMITE ===\n")

testes_limite = [
    ("abc", "123456"),                 
    ("abcd", "123456"),                
    ("abcdefghijkl", "123456"),        
    ("abcdefghijklm", "123456"),        
    ("admin", "12345"),                
    ("admin", "123456"),               
    ("admin", "1234567890"),            
    ("admin", "12345678901"),           
]

for usuario, senha in testes_limite:
    print(f"Teste → Usuário: {usuario}, Senha: {senha}")
    print("Resultado:", login(usuario, senha))
    print("-" * 50)
