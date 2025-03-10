import ttkbootstrap as ttk
from gui import AcupunturaGUI

if __name__ == "__main__":
    root = ttk.Window(themename="flatly")
    app = AcupunturaGUI(root)
    
    root.mainloop()