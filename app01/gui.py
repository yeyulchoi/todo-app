
import functions
import PySimpleGUI as sg


label = sg.Text("Type in a To-Do")
input_box= sg.InputText(tooltip="Enter ToDo", key='todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(functions.get_todos(), key="todos",
                      enable_events=True, size=[45,12])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label],[input_box,add_button],
                            [list_box,edit_button]],
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
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = windowValues['todos'][0]
            substitute=windowValues['todo']
            todos = functions.get_todos()
            myIndex=todos.index(todo_to_edit)
            todos[myIndex]=substitute +"\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=windowValues['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
