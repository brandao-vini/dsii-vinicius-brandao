import tkinter as tk
from tkinter import messagebox
import mysql.connector

# --- CONFIGURAÇÃO DO BANCO DE DADOS (Corrigido Host e Senha) ---
DB_CONFIG = {
    # Host deve ser 'localhost' ou o IP do seu servidor MySQL
    "host": "localhost", 
    "user": "root", 
    # Insira sua senha real ou use "" se não tiver senha
    "password": "", 
    "database": "cadastro_db"
}
# -----------------------------------------------------------------

def salvar_cadastro():
    """Função para coletar e salvar os dados no MySQL."""
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    idade = entry_idade.get()
    sexo = var_sexo.get()
    conexao = None # Inicializa a conexão para garantir que o finally a encontre
    
    # 1. Validação Simples
    if not all([nome, sobrenome, idade, sexo]):
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    try:
        idade_int = int(idade)
    except ValueError:
        messagebox.showerror("Erro", "A idade deve ser um número inteiro.")
        return

    # 2. Conexão e Inserção no Banco de Dados
    try:
        # Conecta ao banco de dados MySQL
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()

        # Comando SQL para inserção de dados
        sql = "INSERT INTO usuarios (nome, sobrenome, idade, sexo) VALUES (%s, %s, %s, %s)"
        valores = (nome, sobrenome, idade_int, sexo)

        # Executa o comando
        cursor.execute(sql, valores)

        # Confirma a transação
        conexao.commit()

        messagebox.showinfo("Sucesso", f"Usuário {nome} {sobrenome} cadastrado com sucesso!")
        
        # Opcional: Limpar os campos do formulário
        entry_nome.set("")
        entry_sobrenome.set("")
        entry_idade.set("")
        var_sexo.set("")
        
    except mysql.connector.Error as err:
        # Exibe qualquer erro de conexão ou SQL
        messagebox.showerror("Erro no DB", f"Ocorreu um erro ao salvar: {err}")
    finally:
        # Garante que a conexão seja fechada
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

# --- FUNÇÃO MOVIDA PARA O NÍVEL PRINCIPAL (CORRIGIDO) ---
def visualizar_cadastros():
    """Busca e exibe todos os registros da tabela usuarios."""
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()

        # Comando SQL para selecionar todos os dados
        sql_select = "SELECT nome, sobrenome, idade, sexo FROM usuarios"
        cursor.execute(sql_select)

        # Recebe todos os resultados da consulta
        resultados = cursor.fetchall()
        
        # Formata os dados para exibição
        if resultados:
            lista_cadastros = "--- Usuários Cadastrados ---\n"
            for nome, sobrenome, idade, sexo in resultados:
                lista_cadastros += f"{nome} {sobrenome} | Idade: {idade} | Sexo: {sexo}\n"
            
            messagebox.showinfo("Cadastros", lista_cadastros)
        else:
            messagebox.showinfo("Cadastros", "Nenhum usuário cadastrado ainda.")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro no DB", f"Ocorreu um erro ao buscar: {err}")
    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()
# -----------------------------------------------------------------


# --- Configuração da Janela Principal ---
janela = tk.Tk()
janela.title("Formulário de Cadastro")

# --- Variáveis para armazenar os dados ---
entry_nome = tk.StringVar()
entry_sobrenome = tk.StringVar()
entry_idade = tk.StringVar()
var_sexo = tk.StringVar()

# --- Componentes da Interface (Widgets) ---

# Rótulo e Campo para Nome
label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")
input_nome = tk.Entry(janela, textvariable=entry_nome)
input_nome.grid(row=0, column=1, padx=10, pady=5)

# Rótulo e Campo para Sobrenome
label_sobrenome = tk.Label(janela, text="Sobrenome:")
label_sobrenome.grid(row=1, column=0, padx=10, pady=5, sticky="w")
input_sobrenome = tk.Entry(janela, textvariable=entry_sobrenome)
input_sobrenome.grid(row=1, column=1, padx=10, pady=5)

# Rótulo e Campo para Idade
label_idade = tk.Label(janela, text="Idade:")
label_idade.grid(row=2, column=0, padx=10, pady=5, sticky="w")
input_idade = tk.Entry(janela, textvariable=entry_idade)
input_idade.grid(row=2, column=1, padx=10, pady=5)

# Rótulo para Sexo
label_sexo = tk.Label(janela, text="Sexo:")
label_sexo.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Radiobuttons para Sexo
radio_masc = tk.Radiobutton(janela, text="Masculino", variable=var_sexo, value="Masculino")
radio_masc.grid(row=3, column=1, padx=10, pady=5, sticky="w")
radio_fem = tk.Radiobutton(janela, text="Feminino", variable=var_sexo, value="Feminino")
radio_fem.grid(row=4, column=1, padx=10, pady=5, sticky="w")
radio_outro = tk.Radiobutton(janela, text="Outro", variable=var_sexo, value="Outro")
radio_outro.grid(row=5, column=1, padx=10, pady=5, sticky="w")


# Botão de Cadastro
botao_salvar = tk.Button(janela, text="Cadastrar", command=salvar_cadastro)
botao_salvar.grid(row=6, column=0, columnspan=2, pady=20)

# Botão para Visualizar Cadastros
botao_visualizar = tk.Button(janela, text="Visualizar Cadastros", command=visualizar_cadastros)
botao_visualizar.grid(row=7, column=0, columnspan=2, pady=10)

# --- Inicia o Loop Principal da Janela ---
janela.mainloop()