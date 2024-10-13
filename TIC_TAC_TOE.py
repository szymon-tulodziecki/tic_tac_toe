import tkinter as tk
import random as rnd


def check_winner(symbol):
    for row in range(3):
        if all(buttons[row][col]["text"] == symbol for col in range(3)):
            return True
    for col in range(3):
        if all(buttons[row][col]["text"] == symbol for row in range(3)):
            return True
    if all(buttons[i][i]["text"] == symbol for i in range(3)) or \
       all(buttons[i][2 - i]["text"] == symbol for i in range(3)):
        return True
    return False


def is_board_full():
    return all(buttons[row][col]["text"] != "" for row in range(3) for col in range(3))


def reset_board():
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            buttons[row][col].config(state="normal")  # Upewnij się, że buttons[row][col] jest zainicjowane


def computer_move():
    empty_cells = [(row, col) for row in range(3) for col in range(3) if buttons[row][col]["text"] == ""]
    if empty_cells:
        row, col = rnd.choice(empty_cells)
        buttons[row][col]["text"] = "O"
        buttons[row][col].config(state="disabled")

        if check_winner("O"):
            show_winner("AI wins!")
        elif is_board_full():
            show_winner("It's a tie!")


def show_winner(message):
    result_window = tk.Toplevel()
    result_window.title("Game Over")
    result_window.geometry("400x300")
    label = tk.Label(result_window, text=message, font=('Helvetica', 20))
    label.pack(pady=20)
    button = tk.Button(result_window, text="Play Again", command=lambda: [reset_board(), result_window.destroy()])
    button.pack(pady=10)


def on_click(row, col):
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = "X"
        buttons[row][col].config(state="disabled")
        if check_winner("X"):
            show_winner("Player wins!")
        elif is_board_full():
            show_winner("It's a tie!")
        else:
            computer_move()


def make_window():
    global buttons
    window = tk.Tk()
    window.title('TIC TAC TOE')

    buttons = [[None for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            buttons[row][col] = tk.Button(window, text="", width=10, height=3, font=('Helvetica', 20),
                                          command=lambda r=row, c=col: on_click(r, c))
            buttons[row][col].grid(row=row, column=col)

    window.mainloop()


if __name__ == '__main__':
    make_window()
