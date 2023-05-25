import sys
import os
import pandas as pd
import db


# Insert the csv files using a SQL INSERT
# Hence the name insert
def insert_csvs(directory,  table_name):
    col_names = ",".join(expected_columns)
    col_name_placeholders = ','.join(['?'] * len(expected_columns))

    db.set_insert_statement(f"INSERT INTO {table_name} ({col_names}) VALUES({col_name_placeholders})")

    for csv in os.listdir(directory):
        name, exten = os.path.splitext(csv)

        if exten != ".csv":
            continue

        print(f"Filename is:{name}")
        parts = name.split("_")

        if len(parts) < 2:
            continue

        flight_id = int(parts[1])

        dat = pd.read_csv(csv)

        values = []

        for i, j in dat.iterrows():
            rvals = [flight_id, i]
            for ii in range(2, len(expected_columns)):
                key = expected_columns[ii]

                if key not in j:
                    rvals.append(j["#" + expected_columns[ii]])
                else:
                    rvals.append(j[expected_columns[ii]])

            values.append(rvals)

        db.preset_insert_many(values)

        print(f"Inserted {len(dat)} rows for flight {flight_id}")


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

    print(f"Importing CSVs from files in directory: {directory} to database file {database}")

    db.init(database)

    expected_columns = os.getenv("EXAMM_INPUT_PARAMETERS").split(" ")
    expected_columns = ["flight_id", "timestep"] + expected_columns + add_params

    insert_csvs(directory, table_name)
