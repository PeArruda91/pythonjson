import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from utils import carregar_dados, salvar_dados
from menu import criar_menu
from janela_edicao import janela_edicao_ponto

class AcupunturaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Pontos de Acupuntura")
        self.root.geometry("800x600")
        self.dados = None
        self.tema_atual = "flatly"
        
        criar_menu(self)
        self.criar_interface()
    
    def importar_json(self):
        caminho = filedialog.askopenfilename(
            title="Selecione o arquivo JSON",
            filetypes=(("JSON files", "*.json"), ("All files", "*.*"))
        )
        
        if caminho:
            self.dados = carregar_dados(caminho)
            if self.dados:
                self.carregar_todos_pontos()
                Messagebox.show_info("Sucesso", "Dados carregados com sucesso!")
    
    def criar_interface(self):
        self.frame_resultados = ttk.Labelframe(self.root, text="Resultados", bootstyle="primary")
        self.frame_resultados.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.tree = ttk.Treeview(self.frame_resultados, columns=("Código", "Funções"), show="headings", bootstyle="info")
        self.tree.heading("Código", text="Código")
        self.tree.heading("Funções", text="Funções Principais")
        self.tree.pack(fill="both", expand=True)
        
        frame_botoes = ttk.Frame(self.root)
        frame_botoes.pack(pady=10, padx=10, fill="x")
        
        ttk.Button(frame_botoes, text="Carregar JSON", command=self.importar_json, bootstyle="info-outline").pack(side="left", padx=5)
        ttk.Button(frame_botoes, text="Adicionar Ponto", command=self.adicionar_ponto, bootstyle="success-outline").pack(side="left", padx=5)
        ttk.Button(frame_botoes, text="Editar Ponto", command=self.editar_ponto, bootstyle="warning-outline").pack(side="left", padx=5)
        ttk.Button(frame_botoes, text="Salvar JSON", command=self.salvar_dados, bootstyle="primary-outline").pack(side="left", padx=5)
        
        self.detalhes_text = ttk.Text(self.root, height=8, wrap="word", state="disabled")
        self.detalhes_text.pack(pady=10, padx=10, fill="x")
        
        self.image_label = ttk.Label(self.root)
        self.image_label.pack(pady=10, padx=10)
        
        self.tree.bind("<<TreeviewSelect>>", self.mostrar_detalhes)
    
    def carregar_todos_pontos(self):
        todos_pontos = []
        for regiao, pontos in self.dados['pontos_acupuntura'].items():
            todos_pontos.extend(pontos)
        self.atualizar_resultados(todos_pontos)
    
    def atualizar_resultados(self, pontos):
        self.tree.delete(*self.tree.get_children())
        for ponto in pontos:
            self.tree.insert("", "end", text=ponto['nome'], 
                            values=(ponto['codigo'], ", ".join(ponto['funcoes'][:2])))
    
    def mostrar_detalhes(self, event):
        if not self.dados:
            return
        
        item = self.tree.selection()[0]
        nome = self.tree.item(item, "text")
        codigo = self.tree.item(item, "values")[0]
        
        ponto = None
        for regiao, pontos in self.dados['pontos_acupuntura'].items():
            for p in pontos:
                if p['nome'] == nome and p['codigo'] == codigo:
                    ponto = p
                    break
        
        if ponto:
            detalhes = f"Nome: {ponto['nome']} ({ponto['codigo']})\n"
            detalhes += f"Localização: {ponto['localizacao']}\n"
            detalhes += "Funções: " + ", ".join(ponto['funcoes']) + "\n"
            if 'precaucoes' in ponto:
                detalhes += "Precauções: " + ", ".join(ponto['precaucoes']) + "\n"
            detalhes += f"Imagem: {ponto['imagem']}"
            
            self.detalhes_text.config(state="normal")
            self.detalhes_text.delete(1.0, "end")
            self.detalhes_text.insert("end", detalhes)
            self.detalhes_text.config(state="disabled")
            
            if ponto['imagem']:
                try:
                    imagem = Image.open(ponto['imagem'])
                except:
                    imagem = Image.open("placeholder.png")
            else:
                imagem = Image.open("placeholder.png")
            
            imagem.thumbnail((200, 200))
            imagem_tk = ImageTk.PhotoImage(imagem)
            self.image_label.config(image=imagem_tk)
            self.image_label.image = imagem_tk
    
    def adicionar_ponto(self):
        janela_edicao_ponto(self, novo=True)
    
    def editar_ponto(self):
        item = self.tree.selection()
        if not item:
            Messagebox.show_warning("Seleção necessária", "Selecione um ponto para editar.")
            return
        item = item[0]
        nome = self.tree.item(item, "text")
        codigo = self.tree.item(item, "values")[0]
        
        ponto = None
        for regiao, pontos in self.dados['pontos_acupuntura'].items():
            for p in pontos:
                if p['nome'] == nome and p['codigo'] == codigo:
                    ponto = p
                    break
        
        if ponto:
            janela_edicao_ponto(self, ponto=ponto)
    
    def salvar_dados(self):
        caminho = filedialog.asksaveasfilename(
            title="Salvar arquivo JSON",
            defaultextension=".json",
            filetypes=(("JSON files", "*.json"), ("All files", "*.*"))
        )
        if caminho:
            salvar_dados(caminho, self.dados)
            Messagebox.show_info("Sucesso", "Dados salvos com sucesso!")

if __name__ == "__main__":
    root = ttk.Window(themename="flatly")
    app = AcupunturaGUI(root)
    assert app.root.title() == "Sistema de Pontos de Acupuntura"
    print("Teste de AcupunturaGUI passou!")
    root.mainloop()
