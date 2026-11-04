# === Header ===
WIDTH = 35
TITLE = "To-Do List"
HEADER = "\n".join(["=" * WIDTH, TITLE.center(WIDTH), "=" * WIDTH])
print(HEADER) 

# === Variables === 
todos = ["clean", "read", "cook"]

    
# === User Inputs === 
def display_menu(): 
    
    # === Display Todos ===
    for i, todo in enumerate(todos):
        print(f"{i + 1}: {todo}") 
    
    # === Total numbers of Todos ==== 
    print(f"\nTotal tasks: {len(todos)}")
        
    # === Main Menu === 
    print("-" * WIDTH)
    print("\nWhat would you like to do? ") 
    print("1. Add a task")
    print("2. Remove a task") 
    print("3. Exit") 
        
    
def main():
    while True:
        display_menu()
        
        choice = input("\nEnter options 1 - 3: ").strip()
        
        try: 
            match choice:
                case "1":
                    new_todo = input("Enter task name: ")
                    todos.append(new_todo)
                    print(f"Your todo list has been updated")
                case "2":
                    delete_todo = int(input("Delete task number: "))
                    todos.pop(delete_todo - 1)
                case "3":
                    print("Exiting program now. Goodbye!")
                    break
                case _:
                    print(f"{choice!r} is not a valid option. Try again.")
        except ValueError:
            print("Please enter a valid task number.")
        except IndexError:
            print("That task number does not exist.") 
            
                         
if __name__ == "__main__":
    main() 
            
                
                
        
    
    



