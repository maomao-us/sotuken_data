import csv
import numpy as np
import pandas as pd
import statistics
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["2y", "3y", "4y", "5y"]

# Euclid(ユークリッド距離)
##################################################################################################################################################
##################################################################################################################################################
def Euclid():
    for a in range(8):
        print(name[a])
        Max = []
        for z in range(0,4):
            file_train = "train_data/" + name[a] + "/" + name[a] + "_" + lx[z] + ".csv"
            df_train = pd.read_csv(file_train, header=None, engine = "python")

            for b in range(8):
                file_test = "train/" + name[b] + "/" + name[b] + "_train_" + lx[z] + ".csv"
                df_test = pd.read_csv(file_test, header=None, engine = "python")

                data_Euclid = []
                sum = 0

                for c in range(len(df_test)):
                    for d in range(len(df_test.columns)):
                        sum += (df_test.values[c, d] - df_train.values[0, d])**2 / df_train.values[1, d]
                    data_Euclid.append(sum)
                    sum = 0

                if a == b:
                    max_value = max(data_Euclid)
                    max_value = Decimal(str(max_value)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
                    max_value = float(max_value)
                    if max_value < max(data_Euclid):
                        max_value = max_value + 0.001
                        max_value = Decimal(str(max_value)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
                        max_value = float(max_value)
                    Max.append(max_value)

                if b == 0:
                    with open("Threshold/" + name[a] + "/" + "Threshold_" + lx[z] + ".csv", "w", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_Euclid)

                else:
                    with open("Threshold/" + name[a] + "/" + "Threshold_" + lx[z] + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_Euclid)

            # df1 = pd.read_csv("Euclid/" + name[a] + "/" + name[a] + "_Euclid_ev_" + lx[z] + ".csv", header=None, engine = "python")
            # df2 = pd.read_csv("Euclid/" + name[a] + "/" + name[a] + "_Euclid_step_" + lx[z] + ".csv", header=None, engine = "python")

            # df1 = df1.T
            # df2 = df2.T

            # df1.to_csv("Euclid/" + name[a] + "/" + name[a] + "_Euclid_ev_" + lx[z] + ".csv", header=None, index = False)
            # df2.to_csv("Euclid/" + name[a] + "/" + name[a] + "_Euclid_step_" + lx[z] + ".csv", header=None, index = False)
            # min_data = []
            # min_data.append(min(Max))
        
            with open("Threshold/" + name[a] + "/" + "Threshold_" + lx[z] + ".csv", "a", newline = "") as f:
                writer = csv.writer(f)
                writer.writerow(Max)
            Max.clear()
Euclid()
