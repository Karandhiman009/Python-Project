import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.board = [""] * 9 
        self.current_player = "X"  
        self.buttons = []  

        self.create_board()

    def create_board(self):
        """Creates the 3x3 grid of buttons"""
        row = 0
        col = 0

        for i in range(9):
            button = tk.Button(self.root, text="", width=10, height=3, font=("Arial", 24),
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=row, column=col)
            self.buttons.append(button)

            col += 1
            if col > 2:
                col = 0
                row += 1

    def on_button_click(self, index):
        """Handles the click event on a button"""
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(self.current_player):
                self.show_winner(self.current_player)
            elif all(spot != "" for spot in self.board):  
                self.show_winner("Draw")
            else:
                self.switch_player()

    def switch_player(self):
        """Switches the current player"""
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        """Checks if the given player has won the game"""
        win_conditions = [
            [0, 1, 2],  
            [3, 4, 5], 
            [6, 7, 8],  
            [0, 3, 6],  
            [1, 4, 7],  
            [2, 5, 8],  
            [0, 4, 8],  
            [2, 4, 6],  
        ]

        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def show_winner(self, winner):
        """Displays a messagebox showing who won the game"""
        if winner == "Draw":
            messagebox.showinfo("Game Over", "It's a Draw!")
        else:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset_game()

    def reset_game(self):
        """Resets the game for a new round"""
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
