import pandas as pd
import random
import sys
import os


def create_noise(file, column, l, n):
    df = pd.read_csv(file)
    indicies = []

    index = 0

    for i in range(0, n):
        l_df = len(df)

        # If only python had do-while :(
        start_index = random.choice(range(0, l_df))
        while (start_index in indicies) or (start_index + l >= l_df) or (start_index - l <= 0):
            start_index = random.choice(range(0, l_df))

        indicies.append(start_index)

        for j in range(start_index, start_index + l):
            # We can change this to whatever we want the "noise" to be
            # print(f"idx: {j}: {df.at[j, column]}")
            df.loc[j, column] = 0.0
            # print(f"updated idx: {j}: {df.at[j, column]}")
            index = j

    # df.update(df)
    return df, index

input_dir = sys.argv[1]
output_dir = sys.argv[2]
column = sys.argv[3]
rand_l = int(sys.argv[4])
rand_n = int(sys.argv[5])

for file in os.listdir(input_dir):
    if file.lower().endswith(".csv"):
        df, index = create_noise(file, column, rand_l, rand_n)
        df.to_csv(f"{output_dir}/{file}")

        sz_df = len(df)
        print(f"Wrote {sz_df} lines of noise-ified infile {file}. At idx[{index}]:{df.at[index, column]}")
