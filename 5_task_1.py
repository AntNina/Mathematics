import random

import plotly
import plotly.graph_objs as go

startmoney = 1000000

c1 = 0.001

win = 0
loose = 0

games = 0

balance1 = []
games1 = []

money = startmoney
while money > 0:
    bet = startmoney * c1
    if bet > money:
        bet = money
    money -= bet

    balance1.append(money)
    games1.append(len(games1) + 1)

    ball = random.randint(1, 37)
    if ball in range(1, 19):
        money += bet * 2
        win += 1
    else:
        loose += 1
games = win + loose
print("Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). " + " Проиграно ставок: " + str(
    loose) + " (" + str(loose / games * 100) + "%). ")
