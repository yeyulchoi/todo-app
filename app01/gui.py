
import functions
import PySimpleGUI as sg


label = sg.Text("Type in a To-Do")
input_box= sg.InputText(tooltip="Enter ToDo", key='todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(functions.get_todos(), key="todos",
                      enable_events=True, size=[45,12])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button=sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label],[input_box,add_button],
                            [list_box,edit_button,complete_button],
                           [exit_button]],
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
            substitute=windowValues['todo']+ "\n"
            todos = functions.get_todos()
            myIndex=todos.index(todo_to_edit)
            todos[myIndex]=substitute
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Complete':
            todo_to_complete = windowValues['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value=' ')
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=windowValues['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
