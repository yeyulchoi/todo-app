#from functions import get_todos, write_todos
import functions


while True:
    user_input =input("Choose : 'add','show', 'complete'. 'edit' or 'exit' : ").lower().strip()

    if user_input.startswith("add"):
        todo= user_input[4:] +"\n"

        todos = functions.get_todos()

        todos.append(""+todo)

        functions.write_todos(todos)


    elif user_input.startswith("show"):

        todos = functions.get_todos()

        for index,thing in enumerate(todos):
            thing=thing.title().strip('\n')
            row = (f'{index+1}- {thing}')
            print(row)
    elif user_input.startswith("edit"):
        try:
            number=int(user_input[5:])
            number-=1
            functions.get_todos()

            new_todo=input("Enter new todo: ")
            todos[number]=new_todo+"\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is invalid")
            continue
    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:])
            index = number -1

            todos = functions.get_todos()

            removed_item = todos.pop(index)

            functions.write_todos(todos)

            message =f"Todo '{removed_item}' was removed from this list"
            print(message)
        except :
            print("value error")
            continue
    elif user_input.startswith("exit"):
        break
    else:
        print("It is not valid")
print('bye')



