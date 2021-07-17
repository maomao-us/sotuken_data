import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["2z", "3z", "4z", "5z"]

# Euclid(ユークリッド距離)
##################################################################################################################################################
##################################################################################################################################################
def Euclid():
    for a in range(8):
        print(name[a])
        min_Euclid = []
        for z in range(0,4):
            file_train = "train_data/" + name[a] + "/" + name[a] + "_" + lx[z] + ".csv"
            df_train = pd.read_csv(file_train, header=None, engine = "python")

            for b in range(8):
                file_test = "test/" + name[b] + "/" + name[b] + "_test_" + lx[z] + ".csv"
                df_test = pd.read_csv(file_test, header=None, engine = "python")

                data_Euclid = []
                sum = 0

                for c in range(len(df_test)):
                    for d in range(len(df_test.columns)):
                        sum += (df_test.values[c, d] - df_train.values[0, d])**2 / df_train.values[1, d]
                    data_Euclid.append(sum)
                    sum = 0

                if a != b:
                    min_Euclid.append(min(data_Euclid))

                if b == 0:
                    with open("Threshold/" + name[a] + "/" + "test_" + lx[z] + ".csv", "w", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_Euclid)

                else:
                    with open("Threshold/" + name[a] + "/" + "test_" + lx[z] + ".csv", "a", newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow(data_Euclid)

            # with open("Threshold/" + name[a] + "/" + "test_" + lx[z] + ".csv", "a", newline = "") as f:
            #     writer = csv.writer(f)
            #     writer.writerow(min_Euclid)
            # min_Euclid.clear()
Euclid()