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
    print("-" * 35)
    
    
# === Display Menu === 
def main():
    
    show_list()
    
    while True:        
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Exit")
        choice = input("\nChoose an option: ").strip() 
        
        if choice == "3":
            print("Quitting the program. Goodby!")
            break
        elif choice not in ("1", "2"):
            print("Please choose a valid menu option.")
            continue 
        
        try: 
            if choice == "1":
                todos.append(input("Enter new task name "))
                print(f"{todos[-1]} has been added!")
            elif choice == "2":
                task_number = int(input("Enter task number: "))
                if not 1 <= task_number <= len(todos): 
                    raise IndexError
                print(f"{todos.pop(task_number -1)} has been deleted successfully!")  
                if not todos:
                    print("ALL DONE! No more todos.")
        except ValueError:
            print("Please choose a valid task number.")
        except IndexError:
            print("That task number does not exist.")
        else:
            print("-" * 35)
            print("\nCurrent Todo List:")
            show_list() 
                     
                         
if __name__ == "__main__":
    main() 
            
                
                
        
    
    


