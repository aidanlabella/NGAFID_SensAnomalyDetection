import pandas as pd
import random
import sys
import os

def create_noise(file, column, l, n):
    df = pd.read_csv(file)
    indicies = []

    for i in range(0, n):
        l_df = len(df)

        # If only python had do-while :(
        start_index = random.choice(range(0, l_df))
        while (start_index in indicies) or (start_index + l >= l_df) or (start_index - l <= 0):
            start_index = random.choice(range(0, l_df))

        indicies.append(start_index)

        for j in range(start_index, start_index + l):
            # We can change this to whatever we want the "noise" to be
            df.set_value(j, column, 0)

    return df

input_dir = sys.argv[1]
output_dir = sys.argv[2]
column = sys.argv[3]
rand_l = int(sys.argv[4])
rand_n = int(sys.argv[5])

for file in os.listdir(input_dir):
    df = create_noise(file, column, rand_l, rand_n)
    print(df)
