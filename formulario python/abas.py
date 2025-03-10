import ttkbootstrap as ttk

def criar_area_resultados(gui):
    gui.tree.delete(*gui.tree.get_children())

def atualizar_interface(gui):
    for widget in gui.frame_resultados.winfo_children():
        widget.destroy()
    
    gui.tree = ttk.Treeview(gui.frame_resultados, columns=("Código", "Funções"), show="headings")
    gui.tree.heading("Código", text="Código")
    gui.tree.heading("Funções", text="Funções Principais")
    gui.tree.pack(fill="both", expand=True)
    
    gui.tree.bind("<<TreeviewSelect>>", gui.mostrar_detalhes)

# Testes
if __name__ == "__main__":
    class MockGUI:
        def __init__(self):
            self.root = ttk.Window(themename="flatly")
            self.frame_resultados = ttk.Labelframe(self.root, text="Resultados", bootstyle="primary")
            self.frame_resultados.pack(pady=10, padx=10, fill="both", expand=True)
            self.tree = ttk.Treeview(self.frame_resultados, columns=("Código", "Funções"), show="headings")
    
    gui = MockGUI()
    criar_area_resultados(gui)
    assert not gui.tree.get_children(), "Área de resultados não foi limpa"
    print("Teste de criar_area_resultados passou!")
    
    atualizar_interface(gui)
    assert gui.tree.winfo_ismapped(), "Interface não foi atualizada corretamente"
    print("Teste de atualizar_interface passou!")
