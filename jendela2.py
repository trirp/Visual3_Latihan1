import PySimpleGUI as sg
window = sg.Window(title="Profile",
                   layout=[
                       [sg.Text("NPM       : 2210010569")],
                       [sg.Text("Nama      : Tri Rahmayati Putri")],
                       [sg.Text("Kelas     : 5A TI Nonreg Banjarmasin")],
                       [sg.Text("Matkul    : Pemrograman Visual 3")]
                       ],
                    size=(400,200))
window()
window.close()