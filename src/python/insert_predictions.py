import sys
import os
import pandas as pd
import db
import insert_data as main

base_columns = main.flight_columns + ['genome_id']


def insert_predictions(directory, table_name, genome_id, columns):
    columns = base_columns + columns

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
            rvals = [flight_id, i, genome_id]
            for ii in range(3, len(columns)):
                key = columns[ii]

                if key not in j:
                    rvals.append(j["#" + columns[ii]])
                else:
                    rvals.append(j[columns[ii]])

            values.append(rvals)

        db.preset_insert_many(values)

        print(f"Inserted {len(dat)} PREDICTION rows for flight {flight_id}")


if __name__ == "__main__":
    database = sys.argv[1]
    directory = sys.argv[2]
    table_name = sys.argv[3]
    genome_id = int(sys.argv[4])

    # The rest of the arguments are the predicted columns for the CSV files
    # We generate the predicted/expected versions of these so they get into the database
    add_params = []
    for i in range(5, len(sys.argv)):
        param = sys.argv[i]
        add_params.append("expected_" + param)
        add_params.append("predicted_" + param)


    db.init(database)

    print(f"Inseting predicted params from genome {genome_id} with CSV files in directory: {directory} to database file {database}")
    insert_predictions(directory, table_name, genome_id, add_params)
