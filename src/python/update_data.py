import sys
import os
import pandas as pd
import db

# TODO: change this to update the flight ts data!

if __name__ == "__main__":
    database = sys.argv[1]
    directory = sys.argv[2]
    table_name = sys.argv[3]
    add_params = []

    # The rest of the arguments are the predicted columns for the CSV files
    # We generate the predicted/expected versions of these so they get into the database
    for i in range(4, len(sys.argv)):
        param = sys.argv[i]
        add_params.append("expected_" + param)
        add_params.append("predicted_" + param)

    print(f"Updating predicted params from CSV files in directory: {directory} to database file {database}")

    db.init(database)

    expected_columns = os.getenv("EXAMM_INPUT_PARAMETERS").split(" ")
    expected_columns = ["flight_id", "timestep"] + expected_columns + add_params
