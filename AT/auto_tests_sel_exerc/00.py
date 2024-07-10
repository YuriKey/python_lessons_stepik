# application = Application(backend="uia").start("explorer.exe").top_window()

# from pywinauto import Application
# from pywinauto.application import Application
#
# app = Application(backend="uia").start(r"C:\Users\User\AppData\Local\Programs\AISMK\AISMK.exe")
#

from pywinauto.application import Application

app = Application().start("notepad.exe")

app.UntitledNotepad.menu_select("Справка->О программе")
app.AboutNotepad.OK.click()
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces=True)
