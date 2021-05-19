from tkinter import *
import tkinter as tk
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
from sklearn.tree import export_text
import requests
import sys
import sys
import sklearn.utils._weight_vector


sys.setrecursionlimit(20000)

sys.setrecursionlimit(20000)

#url = "https://github.com/ScarletAerie/NBA-Project/blob/main/NBA_Decision_Tree_Offensive_Main_2012_Equal_Weight_Class_Outcome.csv?raw=true"
url = "https://github.com/ScarletAerie/NBA-Project/blob/main/2012-2015_NCAA_Data_noblanks.csv?raw=true"
#df = pandas.read_csv("NBA_Decision_Tree_Offensive_Main_2012_Equal_Weight_Class_Outcome.csv")
df = pandas.read_csv(url)
features = ['Points','Assists','FGA','FG','FTAs','FTs', 'Minutes', '3s attempts','3s','turnovers', '2s attempts', '2s', 'usage']


X = df[features]
y = df['Appear_In_NBA']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

Diaman= [[1934,362,1310,584,600,520,3363,630,246,246,680,338,28.6]]

pred_Player = dtree.predict(Diaman)
print(pred_Player)


def calculate():
	player_data = [[int(e2.get()),int(e3.get()), int(e4.get()), int(e5.get()), int(e6.get()), int(e7.get()), int(e8.get()), int(e9.get()), int(e10.get()), int(e11.get()), int(e12.get()), int(e13.get()), float(e14.get()) ]]
	res = dtree.predict(player_data)
	myText.set(res)



root = tk.Tk()
root.title("Will you make it to the NBA?")

valRadio = tk.IntVar()
myText = tk.StringVar()
e1 = tk.StringVar()
e2 = tk.StringVar()
e3 = tk.StringVar()
e4 = tk.StringVar()
e5 = tk.StringVar()
e6 = tk.StringVar()
e7 = tk.StringVar()
e8 = tk.StringVar()
e9 = tk.StringVar()
e10 = tk.StringVar()
e11 = tk.StringVar()
e12 = tk.StringVar()
e13 = tk.StringVar()
e14 = tk.StringVar()


features = ['Points','Assists','FGA','FG','FTAs','FTs', 'Minutes', '3s attempts','3s','turnovers', '2s attempts', '2s', 'usage']


tk.Label(root, text="Will you make it to the NBA?").grid(row = 0, column = 0)
tk.Label( text = "Player Name:").grid(row=1, column =0)
tk.Label( text = "Points:").grid(row=2, column =0)
tk.Label( text = "Assists:").grid(row=3, column =0)
tk.Label( text = "FGA:").grid(row=4, column =0)
tk.Label( text = "FG:").grid(row=5, column =0)
tk.Label( text = "FTAs:").grid(row=6, column =0)
tk.Label( text = "FTs:").grid(row=7, column =0)
tk.Label( text = "Minutes:").grid(row=8, column =0)
tk.Label( text = "3s attempts:").grid(row=9, column =0)
tk.Label( text = "3s:").grid(row=10, column =0)
tk.Label( text = "Turnovers:").grid(row=11, column =0)
tk.Label( text = "2s attempts:").grid(row=12, column =0)
tk.Label( text = "2s:").grid(row=13, column =0)
tk.Label( text = "Usage:").grid(row=14, column =0)






result = tk.Label(text="(result)", textvariable=myText).grid(row=15, column=0)


tk.Entry(textvariable = e1).grid(row=1, column=1)
tk.Entry(textvariable = e2).grid(row=2, column=1)
tk.Entry(textvariable = e3).grid(row=3, column=1)
tk.Entry(textvariable = e4).grid(row=4, column=1)
tk.Entry(textvariable = e5).grid(row=5, column=1)
tk.Entry(textvariable = e6).grid(row=6, column=1)
tk.Entry(textvariable = e7).grid(row=7, column=1)
tk.Entry(textvariable = e8).grid(row=8, column=1)
tk.Entry(textvariable = e9).grid(row=9, column=1)
tk.Entry(textvariable = e10).grid(row=10, column=1)
tk.Entry(textvariable = e11).grid(row=11, column=1)
tk.Entry(textvariable = e12).grid(row=12, column=1)
tk.Entry(textvariable = e13).grid(row=13, column=1)
tk.Entry(textvariable = e14).grid(row=14, column=1)

b= tk.Button(text="Calculate", command=calculate).grid(row=15, column=3)

root.mainloop()