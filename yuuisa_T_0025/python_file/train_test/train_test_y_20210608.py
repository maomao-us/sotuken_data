import csv
import numpy as np
import pandas as pd

# 定義
##################################################################################################################################################
name = ["inoue", "kawamura", "kisimoto", "kutukake", "takenaka", "horinouti", "matui", "yamanada"]
lx = ["2y", "3y", "4y", "5y"]

# 検定_極値
##################################################################################################################################################
##################################################################################################################################################
def kentei_train():
    for a in range(8):
        for b in range(0,4):
            print(name[a])
            file_name = "train/" + name[a] + "/" + name[a] + "_train_" + lx[b] + ".csv"
            df = pd.read_csv(file_name, header=None, engine = "python")
            df = df.T

            mean = []
            var = []

            for i in range(len(df)):
                mean.append(np.mean(df.values[i]))
                var.append(np.var(df.values[i], ddof = 1))

            # print(mean)
            # print(var)
            # print("\n")

            with open("train_data/" + name[a] + "/" + name[a] + "_" + lx[b] + ".csv", "w", newline = "") as f:
                writer = csv.writer(f)
                writer.writerow(mean)
                writer.writerow(var)

            mean.clear()
            var.clear()

kentei_train()