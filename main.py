import tkinter as tk
import random

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.user = "X"
        self.robot = "O"
        self.current_player = random.choice([self.user, self.robot])
        
        self.create_widgets()
        if self.current_player == self.robot:
            self.robot_move()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=" ", font=("Arial", 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.user_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

        self.status_label = tk.Label(self.root, text="Your turn" if self.current_player == self.user else "Robot's turn",
                                     font=("Arial", 16))
        self.status_label.grid(row=3, column=0, columnspan=3)

        # Play Again Button
        self.play_again_button = tk.Button(self.root, text="Play Again", font=("Arial", 16), command=self.reset_game)
        self.play_again_button.grid(row=4, column=0, columnspan=3)
        self.play_again_button.config(state="disabled")

    def user_move(self, row, col):
        if self.board[row][col] == " " and self.current_player == self.user:
            self.board[row][col] = self.user
            self.buttons[row][col].config(text=self.user, state="disabled")
            if self.check_win(self.user):
                self.end_game("You win!")
            elif self.check_draw():
                self.end_game("It's a draw!")
            else:
                self.current_player = self.robot
                self.status_label.config(text="Robot's turn")
                self.root.after(500, self.robot_move)

    def robot_move(self):
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = self.robot
            self.buttons[row][col].config(text=self.robot, state="disabled")
            if self.check_win(self.robot):
                self.end_game("The robot wins!")
            elif self.check_draw():
                self.end_game("It's a draw!")
            else:
                self.current_player = self.user
                self.status_label.config(text="Your turn")

    def check_win(self, player):
        for i in range(3):
            if all([self.board[i][j] == player for j in range(3)]):  # Rows
                return True
            if all([self.board[j][i] == player for j in range(3)]):  # Columns
                return True
        # Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def check_draw(self):
        return all([self.board[row][col] != " " for row in range(3) for col in range(3)])

    def end_game(self, result):
        self.status_label.config(text=result)
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state="disabled")
        self.play_again_button.config(state="normal")  # Enable Play Again button

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = random.choice([self.user, self.robot])
        self.status_label.config(text="Your turn" if self.current_player == self.user else "Robot's turn")

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ", state="normal")

        self.play_again_button.config(state="disabled")  # Disable Play Again button
        if self.current_player == self.robot:
            self.root.after(500, self.robot_move)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
