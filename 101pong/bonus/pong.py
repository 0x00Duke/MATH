#!/usr/bin/env python3

from tkinter import*
import random


def move_bat_right_up(event):                  # movement of the bats
    play_area.move(right_bat, 0, -15)          # movement of the bats
    play_area.move(right_bat, 0, -15)          # movement of the bats


def move_bat_right_down(event):                # movement of the bats
    play_area.move(right_bat, 0, 15)           # movement of the bats
    play_area.move(right_bat, 0, 15)           # movement of the bats


def move_bat_left_up(event):                   # movement of the bats
    play_area.move(left_bat, 0, -10)           # movement of the bats
    play_area.move(left_bat, 0, -10)           # movement of the bats


def move_bat_left_down(event):                 # movement of the bats
    play_area.move(left_bat, 0, 15)            # movement of the bats
    play_area.move(left_bat, 0, 15)            # movement of the bats


def side_of_start():
    i = random.randint(0, 1)
    if i == 0:
        x = -8
    else:
        x = 8
    return x


def ball_movement():
    global dx, dy
    global score_left, score_right
    global sc_txt_left, sc_txt_right
    play_area.move(ball, dx, dy)
    # bounce top / bottom
    if play_area.coords(ball)[1] <= 0 or play_area.coords(ball)[3] >= 600:
        dy = -dy
    # bounce on left bat
    if play_area.coords(ball)[0] <= play_area.coords(left_bat)[2] + 2 and \
            (play_area.coords(ball)[1] <= play_area.coords(left_bat)[3]) and \
            (play_area.coords(ball)[3] >= play_area.coords(left_bat)[1]):
        dx = -dx
    # bounce on right bat
    if play_area.coords(ball)[2] >= play_area.coords(right_bat)[0] - 2 and \
            (play_area.coords(ball)[1] <= play_area.coords(right_bat)[3]) and \
            (play_area.coords(ball)[3] >= play_area.coords(right_bat)[1]):
        dx = -dx
    # right win a point
    if play_area.coords(ball)[0] < 20:
        score_right += 1
        play_area.coords(ball, 1070 / 2 - 15, 600 / 2 - 15, 1070 / 2 + 15, 600 / 2 + 15)
        dx = side_of_start()
        dy = random.choice([-4, -3, -2, 2, 3, 4])
        # sc_txt_right.destroy()
        # sc_txt_left.destroy()
        text_area.itemconfig(sc_txt_right, text=score_right)
        return()
    # left win a point
    if play_area.coords(ball)[0] > 1025:
        score_left += 1
        play_area.coords(ball, 1070 / 2 - 15, 600 / 2 - 15, 1070 / 2 + 15, 600 / 2 + 15)
        dx = side_of_start()
        dy = random.choice([-4, -3.5, -3, -2.5, -2, 2, 2.5, 3, 3.5, 4])
        # sc_txt_right.destroy()
        # sc_txt_left.destroy()
        text_area.itemconfig(sc_txt_left, text=score_left)
        return()
    sc_txt_left = text_area.create_text(900, 50, text=score_left, fill="white")
    sc_txt_right = text_area.create_text(950, 50, text=score_right, fill="white")
    window.after(15, ball_movement)


def start_game(event):
    ball_movement()


window = Tk()                               #
window.geometry("1080x720")                 #
window.minsize(1080, 720)                   # window creation
window.maxsize(1080, 720)                   #
window.config(background="black")           #

play_area = Canvas(window, width=1070, height=600, bd=5, bg="black", relief=SUNKEN)   # creation of two area

text_area = Canvas(window, width=1070, height=100, bd=5, bg="black", relief=SUNKEN)   # one that is the game space
play_area.pack(padx=10, pady=7)                                                       # the other to say how to play
text_area.pack(padx=10, pady=7)                                                       #

img = PhotoImage(file='img.gif')                                  # image in center
play_area.create_image(1070/2, 600/2, image=img)

left_bat = play_area.create_rectangle(20, 265, 35, 385, fill="blue")                   # creation of the two bat
right_bat = play_area.create_rectangle(1025, 265, 1040, 385, fill="red")             # creation of the two bat

ball = play_area.create_oval(1070/2 - 15, 600/2 - 15, 1070/2 + 15, 600/2 + 15, fill="white")            # ball creation

explain = text_area.create_text(65, 20, text="HOW TO PLAY:", fill="white")
explain_run_game = text_area.create_text(550, 20, text="HOW TO START THE GAME:", fill="white")            # explication
run_the_game_key = text_area.create_text(725, 45, text="PRESS THE SPACE BAR", fill="grey")                # text
touch_user_red = text_area.create_text(185, 45, text="USE W TO GO UP\nS TO GO DOWN", fill="blue")
touch_user_blue = text_area.create_text(350, 45, text="USE UP arrow TO GO UP\nDOWN arrow TO GO DOWN", fill="red")
score_text = text_area.create_text(850, 20, text="SCORE:", fill="white")

play_area.bind_all('<Up>', move_bat_right_up)
play_area.bind_all('<Down>', move_bat_right_down)

play_area.bind_all('<w>', move_bat_left_up)
play_area.bind_all('<s>', move_bat_left_down)


dx = side_of_start()
dy = random.choice([-4, -3, -2, 2, 3, 4])

score_left = 0
score_right = 0

play_area.bind_all('<space>', start_game)

window.mainloop()
