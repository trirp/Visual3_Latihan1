import PySimpleGUI as sg
sg.theme("Dark Green4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial",25,"italic","bold","underline"))],
                       [sg.Text("NPM       : 2210010569")],
                       [sg.Text("Nama      : Tri Rahmayati Putri")],
                       [sg.Text("Kelas     : 5A TI Nonreg Banjarmasin")],
                       [sg.Text("Matkul    : Pemrograman Visual 3")]
                       ],
                    size=(500,200),
                    font=("Times",18))
window()
window.close()