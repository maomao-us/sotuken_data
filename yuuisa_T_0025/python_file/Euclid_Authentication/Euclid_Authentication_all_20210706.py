import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["2x", "3x", "4x", "5x"]
ly = ["2y", "3y", "4y", "5y"]
lz = ["2z", "3z", "4z", "5z"]

##################################################################################################################################################
##################################################################################################################################################
def Euclid():
    for a in range(0, 8):
        print(name[a])
        for z in range(0, 4):
            Authentication = []

            test_x = "Threshold/" + name[a] + "/" + "test_" + lx[z] + ".csv"
            test_y = "Threshold/" + name[a] + "/" + "test_" + ly[z] + ".csv"
            test_z = "Threshold/" + name[a] + "/" + "test_" + lz[z] + ".csv"
            df_test_x = pd.read_csv(test_x, header=None, engine = "python")
            df_test_y = pd.read_csv(test_y, header=None, engine = "python")
            df_test_z = pd.read_csv(test_z, header=None, engine = "python")

            threshold_x = "Threshold/" + name[a] + "/" + "Threshold_" + lx[z] + ".csv"
            threshold_y = "Threshold/" + name[a] + "/" + "Threshold_" + ly[z] + ".csv"        
            threshold_z = "Threshold/" + name[a] + "/" + "Threshold_" + lz[z] + ".csv"
            df_threshold_x = pd.read_csv(threshold_x, header=None, engine = "python")
            df_threshold_y = pd.read_csv(threshold_y, header=None, engine = "python")
            df_threshold_z = pd.read_csv(threshold_z, header=None, engine = "python")

            for b in range(8):

                counter_x = 0.0
                counter_y = 0.0
                counter_z = 0.0
                count = 0.0

                if a == b:
                    for c in range(len(df_test_x.columns)):
                        if df_threshold_x.values[len(df_threshold_x) - 1, 0] < df_test_x.values[b, c]:
                            counter_x += 1
                        if df_threshold_y.values[len(df_threshold_y) - 1, 0] < df_test_y.values[b, c]:
                            counter_y += 1
                        if df_threshold_y.values[len(df_threshold_z) - 1, 0] < df_test_z.values[b, c]:
                            counter_z += 1
                        if 0.5 <= (counter_x + counter_y + counter_z) / 3:
                            count += 0.1
                        counter_x = 0.0
                        counter_y = 0.0
                        counter_z = 0.0
                    Authentication.append(format(count, "1f"))
                    count = 0.0
                else:
                    for c in range(len(df_test_x.columns)):
                        if df_test_x.values[b, c] < df_threshold_x.values[len(df_threshold_x) - 1, 0]:
                            counter_x += 1
                        if df_test_y.values[b, c] < df_threshold_y.values[len(df_threshold_y) - 1, 0]:
                            counter_y += 1
                        if df_test_z.values[b, c] < df_threshold_z.values[len(df_threshold_z) - 1, 0]:
                            counter_z += 1
                        if 0.5 <= (counter_x + counter_y + counter_z) / 3:
                            count += 0.1
                        counter_x = 0.0
                        counter_y = 0.0
                        counter_z = 0.0
                    Authentication.append(format(count, "1f"))
                    count = 0.0

            if z == 0:
                with open("Threshold/Authentication/all/" + name[a] + ".csv", "w", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(Authentication)
            else:
                with open("Threshold/Authentication/all/" + name[a] + ".csv", "a", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow(Authentication)
Euclid()
