import mysql.connector

# 1. Inicialize as variáveis de conexão como None
conexao = None
cursor = None

try:
    # 2. Conecte-se ao banco de dados.
    # !!! IMPORTANTE: COLOQUE A SENHA CORRETA DO SEU USUÁRIO 'root' AQUI !!!
    conexao = mysql.connector.connect(
        host="localhost",
        database="etecbd",
        user="root",
        password="",  # <--- TENTE PRIMEIRO COM A SENHA VAZIA SE USAR XAMPP, OU COLOQUE A SUA SENHA
        port=3306
    )
    
    # Se a conexão foi bem-sucedida, o código continua
    print("Conexão estabelecida com sucesso!")
    cursor = conexao.cursor()

    while True:
        # Leitura dos dados do usuário
        nome = input("Digite o nome do Cliente: ")
        estado = input("Digite o Estado (UF): ")
        sexo = input("Digite o Sexo (M/F): ").upper()
        status = input("Digite o Status: ")

        # Inserção no banco de dados
        try:
            # 3. CORREÇÃO: Usando a tabela 'Clientes' e a variável 'nome'
            sql = "INSERT INTO Clientes (Cliente, Estado, Sexo, Status) VALUES (%s, %s, %s, %s)"
            valores = (nome, estado, sexo, status)
            
            cursor.execute(sql, valores)
            conexao.commit()  # Confirma a inserção no banco
            print(f"Cliente '{nome}' inserido com sucesso! ID: {cursor.lastrowid}")

        except mysql.connector.Error as err:
            print(f"Erro ao inserir dados: {err}")
            conexao.rollback() # Desfaz a operação em caso de erro

        continuar = input("Deseja inserir outro cliente? (s/n): ")
        if continuar.lower() != "s":
            break

    # Consulta dos dados (após o loop de inserção)
    print("\n--- Exibindo todos os clientes cadastrados ---")
    cursor.execute("SELECT * FROM Clientes")
    registros = cursor.fetchall()

    for row in registros:
        # 4. CORREÇÃO: Ajustando os índices para a tabela Clientes
        print(f"ID = {row[0]}, Cliente = {row[1]}, Estado = {row[2]}, Sexo = {row[3]}, Status = {row[4]}\n")

except mysql.connector.Error as err:
    # Captura erros de conexão ou de operações SQL
    print(f"Erro de conexão/operação com o banco de dados: {err}")

finally:
    # 5. CORREÇÃO: O bloco finally agora funciona corretamente
    # Garante que o cursor e a conexão sejam fechados
    print("Finalizando o programa.")
    if cursor:
        cursor.close()
    if conexao and conexao.is_connected():
        conexao.close()
