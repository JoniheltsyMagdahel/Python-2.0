import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importando o Pillow

# Criando a janela
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("500x500")

# Carregando uma imagem com Pillow
try:
    imagem = Image.open("imagem.jpg")  # Altere o caminho para a sua imagem
    imagem = imagem.resize((100, 100))  # Redimensionando a imagem para caber na janela
    img_tk = ImageTk.PhotoImage(imagem)
    
    # Exibindo a imagem na janela
    label_imagem = tk.Label(janela, image=img_tk)
    label_imagem.pack(pady=10)
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")

# Criando a barra de texto
entrada_tarefa = tk.Entry(janela, width=30)
entrada_tarefa.pack(pady=5)

# Criando a lista
listbox = tk.Listbox(janela)
listbox.pack(pady=10)

# Função para adicionar tarefa
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        listbox.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)

# Função para excluir tarefa
def excluir_tarefa():
    listbox.delete(tk.ANCHOR)

# Função para concluir tarefa
def concluir():
    selecao = listbox.curselection()
    if selecao:
        index = selecao[0]
        item = listbox.get(index)
        listbox.delete(index)
        listbox.insert(index, item + " (Concluído)")
    else:
        print("Selecione uma tarefa para concluir")

# Botões
botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(pady=5)

botao_excluir = tk.Button(janela, text="Excluir Tarefa", command=excluir_tarefa)
botao_excluir.pack(pady=5)

botao_concluir = tk.Button(janela, text="Concluir", command=concluir)
botao_concluir.pack(pady=5)

# Loop da janela
janela.mainloop()
