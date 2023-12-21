
import functions
import PySimpleGUI as sg
import time

sg.theme("DarkPurple6")

clock = sg.Text('',key='clock')
label = sg.Text("Type in a To-Do")
input_box= sg.InputText(tooltip="Enter ToDo", key='todo')
add_button = sg.Button("Add",size=6)

list_box = sg.Listbox(functions.get_todos(), key="todos",
                      enable_events=True, size=[44,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button=sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                            [label],[input_box,add_button],
                            [list_box,edit_button,complete_button],
                           [exit_button]],
                   font =('Helvetica',20))
while True:
    event, windowValues = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos=functions.get_todos()
            new_todos=windowValues["todo"] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = windowValues['todos'][0]
                substitute=windowValues['todo']+ "\n"
                todos = functions.get_todos()
                myIndex=todos.index(todo_to_edit)
                todos[myIndex]=substitute
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica",20))
        case 'Complete':
            try:
                todo_to_complete = windowValues['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value=' ')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica",20))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=windowValues['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
