
import tkinter as tk
import ast
import operator

root = tk.Tk()
root.title("My Calculator")
root.geometry("340x480")
root.configure(bg="#171717")
root.resizable(False, False)

def button_click(value):
    display.insert(tk.END, value)

def clear_display():
    display.delete(0, tk.END)

def delete_last():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

def calculate():
    expression = display.get()

    try:
        tree = ast.parse(expression, mode="eval")

        def solve(node):
            if isinstance(node, ast.Expression):
                return solve(node.body)

            if isinstance(node, ast.Constant):
                if type(node.value) in (int, float):
                    return node.value
                raise ValueError()

            if isinstance(node, ast.BinOp):
                operations = {
                    ast.Add: operator.add,
                    ast.Sub: operator.sub,
                    ast.Mult: operator.mul,
                    ast.Div: operator.truediv
                }

                operation = operations.get(type(node.op))
                if operation is None:
                    raise ValueError()

                return operation(solve(node.left), solve(node.right))

            if isinstance(node, ast.UnaryOp):
                if isinstance(node.op, ast.USub):
                    return -solve(node.operand)
                if isinstance(node.op, ast.UAdd):
                    return solve(node.operand)

            raise ValueError()

        result = solve(tree)
        display.delete(0, tk.END)
        display.insert(0, str(result))

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Cannot divide by 0")

    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def keyboard_action(event):
    if event.keysym in ("Return", "KP_Enter"):
        calculate()
        return "break"
    elif event.keysym == "Escape":
        clear_display()
        return "break"

# Display
display = tk.Entry(
    root,
    font=("Arial", 28),
    justify="right",
    bg="#252525",
    fg="white",
    insertbackground="white",
    bd=0
)
display.grid(row=0, column=0, columnspan=4,
             padx=12, pady=20, ipady=18, sticky="nsew")

# Buttons
buttons = [
    ["C", "⌫", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "."],
    ["0", "="]
]

for r, row in enumerate(buttons):
    for c, value in enumerate(row):

        if value == "C":
            command = clear_display
        elif value == "⌫":
            command = delete_last
        elif value == "=":
            command = calculate
        else:
            command = lambda v=value: button_click(v)

        if value in ["/", "*", "-", "+", "="]:
            bg_color = "#ff9500"
        elif value in ["C", "⌫"]:
            bg_color = "#555555"
        else:
            bg_color = "#303030"

        if value == "=":
            button = tk.Button(
                root, text=value, font=("Arial", 20, "bold"),
                bg=bg_color, fg="white", bd=0,
                activebackground="#e08400",
                command=command
            )
            button.grid(row=r + 1, column=0,
                        columnspan=4, padx=6, pady=6,
                        sticky="nsew")
        else:
            button = tk.Button(
                root, text=value, font=("Arial", 18),
                bg=bg_color, fg="white", bd=0,
                activebackground="#666666",
                command=command
            )
            button.grid(row=r + 1, column=c,
                        padx=6, pady=6, sticky="nsew")

for c in range(4):
    root.grid_columnconfigure(c, weight=1)

for r in range(1, 6):
    root.grid_rowconfigure(r, weight=1)

root.bind("<Return>", keyboard_action)
root.bind("<KP_Enter>", keyboard_action)
root.bind("<Escape>", keyboard_action)

display.focus_set()
root.mainloop()
