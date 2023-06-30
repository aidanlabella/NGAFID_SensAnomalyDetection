import sys
import os
import pandas as pd
import db

columns = ["flight_id", "timestep", "E1_CHT1", "E1_CHT2", "E1_CHT3", "E1_CHT4",
           "E1_EGT1", "E1_EGT2", "E1_EGT3", "E1_EGT4", "E1_FFlow", "E1_OilP",
           "E1_OilT", "E1_RPM", "volt1", "volt2", "amp1", "AltMSL", "AltB",
           "AltGPS", "Pitch", "VSpd"]


# Will insert the columns specified in the columns parameter
# plus the base flight columns
# Insert the csv files using a SQL INSERT, hence the name insert
def insert_csvs(directory, table_name):
    col_names = ",".join(columns)
    col_name_placeholders = ','.join(['?'] * len(columns))

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

        dat = pd.read_csv(directory + "/" + csv)

        values = []

        for i, j in dat.iterrows():
            rvals = [flight_id, i]
            for ii in range(2, len(columns)):
                key = columns[ii]

                if key not in j:
                    print(f"{key} not found in {j}!")
                    rvals.append(j["#" + columns[ii]])
                else:
                    rvals.append(j[columns[ii]])

            values.append(rvals)

        db.preset_insert_many(values)

        print(f"Inserted {len(dat)} rows for flight {flight_id}")


if __name__ == "__main__":
    database = sys.argv[1]
    directory = sys.argv[2]
    table_name = sys.argv[3]

    # The rest of the arguments are the predicted columns for the CSV files
    # We generate the predicted/expected versions of these so they get into the database
    for i in range(4, len(sys.argv)):
        param = sys.argv[i]

    print(f"Importing CSVs from files in directory: {directory} to database file {database}")

    db.init(database)

    # expected_columns = os.getenv("EXAMM_INPUT_PARAMETERS").split(" ")
    insert_csvs(directory, table_name)
