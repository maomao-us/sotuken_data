import csv
from os import write
import numpy as np
import pandas as pd
import statistics
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["2x", "3x", "4x", "5x"]
ly = ["2y", "3y", "4y", "5y"]
lz = ["2z", "3z", "4z", "5z"]
lxyz = ["2xyz", "3xyz", "4xyz", "5xyz"]

# Euclid(ユークリッド距離)
##################################################################################################################################################
##################################################################################################################################################
def Euclid():
    for a in range(8):
        print(name[a])
        Max = []
        for z in range(0,4):
            file_x = "Threshold/"+ name[a] + "/" + "test_" + lx[z] + ".csv"
            file_y = "Threshold/"+ name[a] + "/" + "test_" + ly[z] + ".csv"
            file_z = "Threshold/"+ name[a] + "/" + "test_" + lz[z] + ".csv"

            df_x = pd.read_csv(file_x, header=None, engine = "python")
            df_y = pd.read_csv(file_y, header=None, engine = "python")
            df_z = pd.read_csv(file_z, header=None, engine = "python")

            for b in range(len(df_x)):
                    if b == 0:
                        with open("Threshold/" + name[a] + "/" + "test_" + lxyz[z] + ".csv", "w", newline = "") as f:
                            writer = csv.writer(f)
                            writer.writerow(df_x.values[b] + df_y.values[b] + df_z.values[b])
                    else:
                        with open("Threshold/" + name[a] + "/" + "test_" + lxyz[z] + ".csv", "a", newline = "") as f:
                            writer = csv.writer(f)
                            writer.writerow(df_x.values[b] + df_y.values[b] + df_z.values[b])
Euclid()