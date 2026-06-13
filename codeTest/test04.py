from pywinauto.application import Application

app = Application(backend='uia').connect(process=5092)
win = app.window(best_match="Untitled• - Typora")

print(win.print_control_identifiers())

