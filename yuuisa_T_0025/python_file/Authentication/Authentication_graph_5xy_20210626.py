import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import math

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["5x", "5y", "5z"]
label_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
color_list =["r", "b", "g", "c", "m", "y", "k", '#f781bf']
# x_memory = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
# y_memory = [0, 10, 20, 30, 40, 50, 60, 70 ,80, 90, 100]
x_memory = [0, 0.4, 0.8, 1.2, 1.6, 2.0]
y_memory = [0, 20, 40, 60, 80, 100]

##################################################################################################################################################
##################################################################################################################################################
def Authentication_graph():
    x = []
    for a in range(0, 8):
        print(name[a])
        fig = plt.figure(figsize=(6, 6))
        mpl.rcParams['axes.xmargin'] = 0
        mpl.rcParams['axes.ymargin'] = 0
        for b in range(8):
            file_FRR = "5xy_Authentication/" + name[a] + "/" + name[b] + "_FRR.csv"
            file_FAR = "5xy_Authentication/" + name[a] + "/" + name[b] + "_FAR.csv"

            if a == b:
                df_FRR = pd.read_csv(file_FRR, header=None, engine = "python")
                for c in range(len(df_FRR.columns)):
                    x.append(c*0.01)
                plt.plot(x, df_FRR.values[len(df_FRR) - 1] * 100, color = color_list[6])
                x.clear()
            else:
                df_FAR = pd.read_csv(file_FAR, header=None, engine = "python")
                for c in range(len(df_FAR.columns)):
                    x.append(c*0.01)
                plt.plot(x, df_FAR.values[len(df_FAR) - 1] * 100, color = color_list[6])
                x.clear()
        
        # plt.title("User " + label_list[a], {"fontsize":20})
        # plt.xlabel("t", {"fontsize":20})
        # plt.ylabel("%", {"fontsize":20})
        plt.xticks(fontsize=24)
        plt.xticks(x_memory)
        plt.yticks(fontsize=24)
        plt.yticks(y_memory)

        plt.grid()
        # plt.legend()
        plt.show()
        # fig.savefig("graph_Authentication/" + name[a] + "/" + label_list[a] + "_5xy.png")
        plt.close()

Authentication_graph()