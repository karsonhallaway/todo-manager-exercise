# === Header ===
WIDTH = 35
TITLE = "My To-Do Lists"
HEADER = "\n".join(["=" * WIDTH, TITLE.center(WIDTH), "=" * WIDTH])
print(HEADER) 

# === Variables === 
todos = ["clean", "read", "cook"]

# === Display Todos ===

for i, todo in enumerate(todos):
    print(f"{i + 1}: {todo}") 


