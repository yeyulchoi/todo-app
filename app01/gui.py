
import functions
import PySimpleGUI as sg


label = sg.Text("Type in a To-Do")
input_box= sg.InputText(tooltip="Enter ToDo", key='todo')
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label],[input_box,add_button]],
                   font =('Helvetica',15))
while True:
    event, windowValues = window.read()
    print(event)
    print(windowValues)
    match event:
        case 'Add':
            todos=functions.get_todos()
            new_todos=windowValues["todo"] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
