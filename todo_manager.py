# === Header ===
WIDTH = 35
TITLE = "To-Do List"
HEADER = "\n".join(["=" * WIDTH, TITLE.center(WIDTH), "=" * WIDTH])
print(HEADER) 

# === Variables === 
todos = ["clean", "read", "cook"]

# === Display Todos ===
def show_list():
    for i, todo in enumerate(todos):
        print(f"{i + 1}. {todo}")
    print(f"\nTotal tasks: {len(todos)}") 
    
    
# === Display Menu === 
def main():
    
    while True:
        show_list()
        
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Exit")
        choice = input("\nSelect: ").strip() 
        
        if choice == "3":
            print("Quitting the program. Goodby!")
            break
        elif choice not in ("1", "2"):
            print("Please choose a valid menu option.")
            continue 
        
        try: 
            if choice == "1":
                todos.append(input("Enter new task name "))
            elif choice == "2":
                task_number = int(input("Enter task number: "))
                if not 1 <= task_number <= len(todos): 
                    raise IndexError
                todos.pop(task_number -1) 
        except ValueError:
            print("Please choose a valid task number.")
        except IndexError:
            print("That task number does not exist.")
        else:
            print("\nUpdated List:")
            show_list()
                     
                         
if __name__ == "__main__":
    main() 
            
                
                
        
    
    



