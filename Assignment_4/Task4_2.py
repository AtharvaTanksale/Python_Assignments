def fileoperations(file_name):
    try:
        w1 = input("Enter text to write: ")
        with open(file_name, "w") as f:
            f.write(w1)
        print(f"File {file_name} has been written")
    except IOError as e:
        print(f"Error writing to file: {e}")
        return
    try:
        a1 = input("Enter text to append: ")
        with open(file_name, "a") as f:
            f.write("\n"+ a1)
        print(f"File {file_name} has been appended")
    except IOError as e:
        print(f"Error appending to file: {e}")
        return
    print(f"\nFinal Content of {file_name}:")
    try:
        with open(file_name, "r") as f:
            content = print(f.read())
            print(content)
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
    except IOError as e:
        print(f"Error reading file: {e}")

fileoperations("task_2.txt")
