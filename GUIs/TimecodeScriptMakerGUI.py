"""
Code to extract translation from an LDS script
Author: Dallin Frank

Build executable:
py -m PyInstaller -w --onefile "Timecode Generator.py"
"""

import PySimpleGUI as sg
from timecode import enhance_script 

def main() -> None:
    layout = [  [sg.T("")], \
                [sg.Text("Choose LDS Translation: ")], \
                [sg.Input(), sg.FileBrowse(key="trans")], \
                [sg.T("")], \
                [sg.Text("Choose Timecode File: ")], \
                [sg.Input(), sg.FileBrowse(key="time")], \
                [sg.T("")], \
                [sg.Text("Choose Destination Folder: ")], \
                [sg.Input(), sg.FolderBrowse(key="dest")], \
                [sg.T("")], \
                [sg.Text("Choose Timecode Word Document Name: ")], \
                [sg.Input(key="filename"), sg.Text(".docx")], \
                [sg.T("")], \
                [sg.Button("Submit")]]

    # Create the window
    window = sg.Window('Voices Now Timecode Generator', layout, size=(500,500))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Submit":
            trans, time, dest, filename = values["trans"], values["time"], values["dest"], values["filename"]
            if trans == "" or time == "" or dest == "" or filename == "":
                sg.popup_ok("Please enter a value in all fields")
                continue
            else:
                try:
                    enhance_script(trans, time, dest + "/" + filename + ".docx")
                except FileNotFoundError:
                    sg.popup_error_with_traceback("File not found")
                except Exception as e:
                    sg.popup_error_with_traceback("Something went wrong :/")
                    print(str(e))
            break

    window.close()

if __name__ == "__main__":
    main()