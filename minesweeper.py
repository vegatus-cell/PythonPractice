import tkinter as tk
from tkinter import messagebox
import random

class Minesweeper:
    def __init__(self, master):
        self.master = master
        self.master.title("지뢰찾기")
        self.rows = 10
        self.cols = 10
        self.num_mines = 10
        
        self.board = []
        self.buttons = []
        self.mines = set()
        self.game_over = False
        self.flags = 0
        
        self.header_frame = tk.Frame(self.master, padx=10, pady=10)
        self.header_frame.pack(fill=tk.X)
        
        self.status_label = tk.Label(self.header_frame, text=f"남은 지뢰: {self.num_mines}", font=('Arial', 12, 'bold'))
        self.status_label.pack(side=tk.LEFT)
        
        self.restart_btn = tk.Button(self.header_frame, text="😊 처음부터", font=('Arial', 12), command=self.reset_game)
        self.restart_btn.pack(side=tk.RIGHT)
        
        self.grid_frame = tk.Frame(self.master, padx=10, pady=10)
        self.grid_frame.pack()
        
        self.reset_game()
        
    def reset_game(self):
        self.game_over = False
        self.mines.clear()
        self.flags = 0
        self.status_label.config(text=f"남은 지뢰: {self.num_mines}")
        self.restart_btn.config(text="😊 처음부터")
        
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.state = [['hidden' for _ in range(self.cols)] for _ in range(self.rows)] # 'hidden', 'revealed', 'flagged'
        
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
            
        self.buttons = []
        
        # 1. 지뢰 배치
        while len(self.mines) < self.num_mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            self.mines.add((r, c))
            self.board[r][c] = -1
            
        # 2. 주변 지뢰 개수 계산
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    continue
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols and self.board[nr][nc] == -1:
                            count += 1
                self.board[r][c] = count
                
        # 3. 버튼 생성
        for r in range(self.rows):
            row_btns = []
            for c in range(self.cols):
                btn = tk.Button(self.grid_frame, width=2, height=1, font=('Arial', 12, 'bold'), cursor="hand2")
                btn.grid(row=r, column=c, padx=1, pady=1)
                
                # 마우스 이벤트 바인딩
                btn.bind('<Button-1>', lambda e, r=r, c=c: self.on_left_click(r, c)) # 좌클릭
                btn.bind('<Button-3>', lambda e, r=r, c=c: self.on_right_click(r, c)) # 우클릭
                
                # 양쪽 클릭 구현 (한쪽 버튼을 누른 상태에서 다른 쪽 클릭)
                btn.bind('<B1-Button-3>', lambda e, r=r, c=c: self.on_chord(r, c))
                btn.bind('<B3-Button-1>', lambda e, r=r, c=c: self.on_chord(r, c))

                row_btns.append(btn)
            self.buttons.append(row_btns)
            
    def on_left_click(self, r, c):
        if self.game_over or self.state[r][c] == 'flagged':
            return
            
        # 이미 열린 숫자 위에서 좌클릭을 해도 양쪽 클릭과 같은 효과 발동 (편의성)
        if self.state[r][c] == 'revealed':
            self.on_chord(r, c)
            return

        if self.board[r][c] == -1:
            # 지뢰를 밟은 경우
            self.game_over = True
            self.restart_btn.config(text="💀 다시 시작!")
            self.reveal_all(False, clicked_mine=(r, c))
            messagebox.showinfo("게임 오버", "지뢰를 밟았습니다!")
        else:
            self.reveal(r, c)
            self.check_win()
            
    def on_right_click(self, r, c):
        if self.game_over or self.state[r][c] == 'revealed':
            return
            
        if self.state[r][c] == 'hidden':
            self.state[r][c] = 'flagged'
            self.buttons[r][c].config(text='🚩', fg='red')
            self.flags += 1
        elif self.state[r][c] == 'flagged':
            self.state[r][c] = 'hidden'
            self.buttons[r][c].config(text='')
            self.flags -= 1
            
        self.status_label.config(text=f"남은 지뢰: {self.num_mines - self.flags}")

    def on_chord(self, r, c):
        """양쪽 클릭 기능: 주변에 표시된 깃발 수가 현재 칸의 숫자와 일치하면 나머지 주변 칸 열기"""
        if self.game_over or self.state[r][c] != 'revealed':
            return
            
        # 주변 깃발 개수 확인
        flag_count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.state[nr][nc] == 'flagged':
                        flag_count += 1
                        
        # 깃발 개수와 주변 지뢰 개수가 같으면 나머지 칸 열기
        if flag_count == self.board[r][c]:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        if self.state[nr][nc] == 'hidden':
                            if self.board[nr][nc] == -1:
                                # 잘못된 깃발 예측으로 지뢰를 밟음
                                self.game_over = True
                                self.restart_btn.config(text="💀 다시 시작!")
                                self.reveal_all(False, clicked_mine=(nr, nc))
                                messagebox.showinfo("게임 오버", "잘못된 곳에 깃발을 꽂아 지뢰가 터졌습니다!")
                                return
                            else:
                                self.reveal(nr, nc)
            self.check_win()

    def reveal(self, r, c):
        if not (0 <= r < self.rows and 0 <= c < self.cols) or self.state[r][c] != 'hidden':
            return
            
        self.state[r][c] = 'revealed'
        val = self.board[r][c]
        
        # 지뢰찾기 숫자별 특징적인 색상
        colors = {1: 'blue', 2: 'green', 3: 'red', 4: 'navy', 5: 'maroon', 6: 'teal', 7: 'black', 8: 'gray'}
        
        if val == 0:
            self.buttons[r][c].config(text='', relief=tk.SUNKEN, bg='#E0E0E0', activebackground='#E0E0E0')
            # 주변 8칸도 연쇄적으로 열기
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    self.reveal(r + dr, c + dc)
        else:
            self.buttons[r][c].config(
                text=str(val), 
                fg=colors.get(val, 'black'), 
                relief=tk.SUNKEN, 
                bg='#E0E0E0', 
                activebackground='#E0E0E0'
            )
            
    def reveal_all(self, won, clicked_mine=None):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    if self.state[r][c] == 'flagged':
                        self.buttons[r][c].config(text='🚩', fg='green' if won else 'red')
                    else:
                        bg_color = 'red' if clicked_mine == (r, c) else 'darkgray'
                        self.buttons[r][c].config(text='💣', fg='black', bg=bg_color)
                elif self.state[r][c] == 'flagged' and not won:
                    # 지뢰가 아닌데 깃발을 꽂은 곳 (X 표시)
                    self.buttons[r][c].config(text='❌', fg='black', bg='pink')

    def check_win(self):
        if self.game_over:
            return
        
        revealed_count = sum(1 for r in range(self.rows) for c in range(self.cols) if self.state[r][c] == 'revealed')
        # 열린 칸 수가 (전체 칸 수 - 지뢰 수)와 같으면 승리
        if revealed_count == self.rows * self.cols - self.num_mines:
            self.game_over = True
            self.restart_btn.config(text="😎 승리!")
            self.reveal_all(True)
            messagebox.showinfo("승리!", "지뢰를 모두 찾았습니다. 축하합니다!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Minesweeper(root)
    
    # 윈도우를 화면 중앙에 배치
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
    root.mainloop()
