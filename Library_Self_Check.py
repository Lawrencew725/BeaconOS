try: #OS File Check
    import Console_Delcear as Console_Delcear
    import Messages_Declear as Messages_Declear
except ModuleNotFoundError:
    print(Messages_Declear.OSLibraryError)
try: #OS Essencial Module Check
    import time
    import tkinter
    import _tkinter
except ModuleNotFoundError:
    print(Messages_Declear.GraphicsUnsupported)