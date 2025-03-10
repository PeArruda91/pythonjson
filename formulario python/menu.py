import ttkbootstrap as ttk

def criar_menu(gui):
    menubar = ttk.Menu(gui.root)
    file_menu = ttk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Sair", command=gui.root.quit)
    menubar.add_cascade(label="Arquivo", menu=file_menu)
    gui.root.config(menu=menubar)

# Testes
if __name__ == "__main__":
    class MockGUI:
        def __init__(self):
            self.root = ttk.Window(themename="flatly")
    
    gui = MockGUI()
    criar_menu(gui)
    assert isinstance(gui.root['menu'], ttk.Menu)
    print("Teste de criar_menu passou!")
