import tkinter as tk

def gravar_saida():
    # Obter os valores dos campos de entrada
    valor1 = campo1.get()
    valor2 = campo2.get()
    valor3 = campo3.get()
    valor4 = campo4.get()

    # Concatenar os valores em uma string
    resultado = f"Campo 1: {valor1}\nCampo 2: {valor2}\nCampo 3: {valor3}\nCampo 4: {valor4}"

    # Limpar o conteúdo atual da caixa de texto
    caixa_texto.delete(1.0, tk.END)

    # Adicionar o resultado à caixa de texto
    caixa_texto.insert(tk.END, resultado)
    return (valor1, valor2, valor3, valor4)

# Criar a janela principal
janela = tk.Tk()
janela.title("Exemplo Tkinter")

# Criar e posicionar os rótulos e campos de entrada
rotulo1 = tk.Label(janela, text="HOST:")
rotulo1.pack(pady=5)
campo1 = tk.Entry(janela)
campo1.pack(pady=5)

rotulo2 = tk.Label(janela, text="USER:")
rotulo2.pack(pady=5)
campo2 = tk.Entry(janela)
campo2.pack(pady=5)

rotulo3 = tk.Label(janela, text="PASSWORD:")
rotulo3.pack(pady=5)
campo3 = tk.Entry(janela)
campo3.pack(pady=5)

rotulo4 = tk.Label(janela, text="DATABASE:")
rotulo4.pack(pady=5)
campo4 = tk.Entry(janela)
campo4.pack(pady=5)

# Criar o botão e associá-lo à função gravar_saida
botao = tk.Button(janela, text="Gravar Saída", command=gravar_saida)
botao.pack(pady=10)

# Criar a caixa de texto para exibir a saída
caixa_texto = tk.Text(janela, height=10, width=40)
caixa_texto.pack(pady=10)

# Iniciar o loop principal da interface gráfica
janela.mainloop()