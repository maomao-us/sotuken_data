import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lxyz = ["2xyz", "3xyz", "4xyz", "5xyz"]

##################################################################################################################################################
##################################################################################################################################################
def Euclid():
    for a in range(0, 8):
        print(name[a])
        for z in range(0, 4):
            Authentication = []

            file_test = "Threshold/" + name[a] + "/" + "test_" + lxyz[z] + ".csv"
            df_test = pd.read_csv(file_test, header=None, engine = "python")

            threshold = "Threshold/" + name[a] + "/" + "Threshold_" + lxyz[z] + ".csv"
            df_threshold = pd.read_csv(threshold, header=None, engine = "python")
            # print(df_threshold.values[len(df_threshold) - 1, 0])

            for b in range(8):  
                count = 0.0
                if a == b:
                    for c in range(len(df_test.columns)):
                        if df_threshold.values[len(df_threshold) - 1, 0] < df_test.values[b, c]:
                            count += 0.1
                    Authentication.append(format(count, "1f"))
                    count = 0
                else:
                    for c in range(len(df_test.columns)):
                        if df_test.values[b, c] < df_threshold.values[len(df_threshold) - 1, 0]:
                            count += 0.1
                    Authentication.append(format(count, "1f"))
                    count = 0

            if z == 0:
                with open("Threshold/Authentication/xyz/" + name[a] + ".csv", "w", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(Authentication)
            else:
                with open("Threshold/Authentication/xyz/" + name[a] + ".csv", "a", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(Authentication)
Euclid()
