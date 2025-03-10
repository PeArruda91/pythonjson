import ttkbootstrap as ttk
from tkinter import filedialog

def janela_edicao_ponto(gui, ponto=None, novo=False):
    janela = ttk.Toplevel(gui.root)
    janela.title("Adicionar Ponto" if novo else "Editar Ponto")
    
    ttk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
    nome_var = ttk.StringVar(value=ponto['nome'] if ponto else "")
    ttk.Entry(janela, textvariable=nome_var).grid(row=0, column=1, padx=10, pady=5)
    
    ttk.Label(janela, text="Código:").grid(row=1, column=0, padx=10, pady=5)
    codigo_var = ttk.StringVar(value=ponto['codigo'] if ponto else "")
    ttk.Entry(janela, textvariable=codigo_var).grid(row=1, column=1, padx=10, pady=5)
    
    ttk.Label(janela, text="Localização:").grid(row=2, column=0, padx=10, pady=5)
    localizacao_var = ttk.StringVar(value=ponto['localizacao'] if ponto else "")
    ttk.Entry(janela, textvariable=localizacao_var).grid(row=2, column=1, padx=10, pady=5)
    
    ttk.Label(janela, text="Funções:").grid(row=3, column=0, padx=10, pady=5)
    funcoes_var = ttk.StringVar(value=", ".join(ponto['funcoes']) if ponto else "")
    ttk.Entry(janela, textvariable=funcoes_var).grid(row=3, column=1, padx=10, pady=5)
    
    ttk.Label(janela, text="Precauções:").grid(row=4, column=0, padx=10, pady=5)
    precaucoes_var = ttk.StringVar(value=", ".join(ponto.get('precaucoes', [])) if ponto else "")
    ttk.Entry(janela, textvariable=precaucoes_var).grid(row=4, column=1, padx=10, pady=5)
    
    ttk.Label(janela, text="Imagem:").grid(row=5, column=0, padx=10, pady=5)
    imagem_var = ttk.StringVar(value=ponto['imagem'] if ponto else "")
    ttk.Entry(janela, textvariable=imagem_var, state="disabled").grid(row=5, column=1, padx=10, pady=5)
    def carregar_imagem():
        caminho_imagem = filedialog.askopenfilename(
            title="Selecione a imagem",
            filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.gif"), ("All files", "*.*"))
        )
        if caminho_imagem:
            imagem_var.set(caminho_imagem)
    ttk.Button(janela, text="Carregar Imagem", command=carregar_imagem).grid(row=5, column=2, padx=10, pady=5)
    
    ttk.Label(janela, text="Região:").grid(row=6, column=0, padx=10, pady=5)
    regioes = list(gui.dados['pontos_acupuntura'].keys())
    regiao_var = ttk.StringVar(value=ponto['regiao'] if ponto else "")
    regiao_combobox = ttk.Combobox(janela, values=regioes, textvariable=regiao_var)
    regiao_combobox.grid(row=6, column=1, padx=10, pady=5)
    
    def salvar_ponto():
        novo_ponto = {
            "nome": nome_var.get(),
            "codigo": codigo_var.get(),
            "localizacao": localizacao_var.get(),
            "funcoes": [func.strip() for func in funcoes_var.get().split(",")],
            "precaucoes": [prec.strip() for prec in precaucoes_var.get().split(",")],
            "imagem": imagem_var.get(),
            "regiao": regiao_var.get().lower()
        }
        regiao = regiao_var.get().lower()
        if gui.dados is None:
            gui.dados = {'pontos_acupuntura': {}}
        if regiao not in gui.dados['pontos_acupuntura']:
            gui.dados['pontos_acupuntura'][regiao] = []
        if novo:
            gui.dados['pontos_acupuntura'][regiao].append(novo_ponto)
        else:
            for regiao, pontos in gui.dados['pontos_acupuntura'].items():
                for i, p in enumerate(pontos):
                    if p['codigo'] == ponto['codigo']:
                        gui.dados['pontos_acupuntura'][regiao][i] = novo_ponto
                        break
        gui.atualizar_interface()
        janela.destroy()
    
    ttk.Button(janela, text="Adicionar" if novo else "Salvar", command=salvar_ponto, bootstyle="success-outline").grid(row=7, column=0, columnspan=2, pady=10)

# Testes
if __name__ == "__main__":
    class MockGUI:
        def __init__(self):
            self.root = ttk.Window(themename="flatly")
            self.dados = {'pontos_acupuntura': {}}
    
    gui = MockGUI()
    janela_edicao_ponto(gui, novo=True)
    assert gui.root.winfo_children(), "Janela de edição não foi criada"
    print("Teste de janela_edicao_ponto passou!")
