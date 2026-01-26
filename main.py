while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case 'add':
            todo = input("Add a task: ") + "\n"
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            todos.append(todo)
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case 'show':
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            #new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Enter a number of todos to edit: "))
            number = number - 1
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Enter a number of todos to complete: "))
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} has been completed."
            print(message)
        case 'exit':
            print("Goodbye")
            break
        case _:
            print("Invalid input")