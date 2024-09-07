import tkinter as tk
import random
import pyautogui
def turn_card() :
    for i in range(16) :
        buttons[i].config(text=f"{imgs[i]}")
    root.after(2000,turn_card_back)
def turn_card_back() :
    for i in range(16) :
        a = 0
        if len(try1) > 0 :
            for j in try1 :
                if j == i :
                    a = 1
        if a > 0 :
            continue
        else :
            buttons[i].config(text= " ")
def game_start():
    score.place(x = 90, y = 30)
    root.geometry("320x400")
    jotaro.place(x = 160, y =30)
    # Disable buttons to prevent interaction during the game setup
    start.destroy()
    rank1.destroy()
    rank2.destroy()
    rank3.destroy()
    rank4.destroy()
    rank5.destroy()
    
    global score1, click, buttons, imgs, photo, first_num, the_world, try1, rank
    score1 = 0
    click = 0
    first_num = None
    the_world = 0
    try1 = []
    buttons = []
    imgs = []

    # Load image
    try:
        photo = tk.PhotoImage(file="C:/Users/user/Desktop/images/default_img.gif")
    except tk.TclError:
        print("Image file not found. Ensure the path is correct.")
        return
    
    # Initialize and shuffle image indices
    for i in range(1, 9):
        imgs.append(i)
        imgs.append(i)
    
    random.shuffle(imgs)

    # Create buttons and assign them to grid
    btn_num = 0
    for r in range(1,5):
        for c in range(4):
            btn_num += 1
            btn = tk.Button(root, text="      ", command=lambda btn_num=btn_num: click_btn(btn_num))
            btn.config(width=10, height=5)
            buttons.append(btn)
            btn.place(x = 80*c, y = 80*r )
    
    # Start the timer
    root.after(1000, time)
    turn_card()
def time():
    global the_world
    the_world += 1
    jotaro.config(text=f"time: {the_world}")

    if the_world >= 60:
        nn = pyautogui.prompt(title='Nickname', text="Enter your nickname")
        rank6 = [nn, score1]
        rank.append(rank6)
        sorted_rank = sorted(rank, key=lambda x: x[1], reverse=True)
        
        with open('C:/Users/user/Desktop/images/score_board.txt', 'w') as f:
            for i in range(min(5, len(sorted_rank))):
                f.write(f"{sorted_rank[i][0]}\n{sorted_rank[i][1]}\n")

        root.destroy()
    else:
        root.after(1000, time)

def clear_t(n, m):
    buttons[n].config(text="      ")
    buttons[m].config(text="      ")

def click_btn(num):
    global click, first_num, score1

    if len(try1) > 0 and num - 1 in try1:
        return

    if click == 0:
        buttons[num - 1].config(text=f"{imgs[num - 1]}")
        first_num = num - 1
        click = 1
        try1.append(first_num)
    else:
        buttons[num - 1].config(text=f"{imgs[num - 1]}")
        try1.append(num - 1)
        if imgs[first_num] == imgs[num - 1]:
            score1 += 100
            if len(try1) == 16:
                for i in range(16):
                    buttons[i].config(text="      ")
                random.shuffle(imgs)
                try1.clear()
                turn_card()
        else:
            score1 += 50
            root.after(300, lambda: clear_t(num - 1, first_num))
            try1.remove(first_num)
            try1.remove(num - 1)
        score.config(text=f"score: {score1}")
        click = 0

# Initialize main window
root = tk.Tk()
root.title("Card Matching Game")
root.geometry("320x130")
root.configure(bg='blue')

title = tk.Label(root, text="Card Matching Game")
title.place(x = 90,y = 0)

start = tk.Button(root, text="Start", command=game_start)
start.place(x = 125, y =60)

# Load ranks from file
rank = []
try:
    with open('C:/Users/user/Desktop/images/score_board.txt', 'r') as f:
        while True:
            a = f.readline().strip()
            b = f.readline().strip()
            if not a or not b:
                break
            rank.append([a, int(b)])
except FileNotFoundError:
    print("Score board file not found. Starting with an empty leaderboard.")

# Create rank labels
rank1 = tk.Label(root, text=f"1: {rank[0][0] if len(rank) > 0 else '-'} {rank[0][1] if len(rank) > 0 else '-'}")
rank2 = tk.Label(root, text=f"2: {rank[1][0] if len(rank) > 1 else '-'} {rank[1][1] if len(rank) > 1 else '-'}")
rank3 = tk.Label(root, text=f"3: {rank[2][0] if len(rank) > 2 else '-'} {rank[2][1] if len(rank) > 2 else '-'}")
rank4 = tk.Label(root, text=f"4: {rank[3][0] if len(rank) > 3 else '-'} {rank[3][1] if len(rank) > 3 else '-'}")
rank5 = tk.Label(root, text=f"5: {rank[4][0] if len(rank) > 4 else '-'} {rank[4][1] if len(rank) > 4 else '-'}")
jotaro = tk.Label(root, text="time: 0")
rank1.place(x = 165, y = 30)
rank2.place(x = 165, y = 50)
rank3.place(x = 165, y = 70)
rank4.place(x = 165, y = 90)
rank5.place(x = 165, y = 110)
score = tk.Label(root, text="score: 0")
# Initialize score and time labels
jotaro = tk.Label(root, text="time: 0")
# Start the Tkinter event loop
root.mainloop()