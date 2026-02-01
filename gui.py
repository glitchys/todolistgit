from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do item: ")
input_box = sg.InputText(tooltip="Enter todolist item")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout = [[label], [input_box, add_button]])
window.read()
window.close()