import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import db
import os
import sys

def get_flights(db):
    sql = "SELECT DISTINCT flight_id FROM msl_diff"
    result = db.query(sql)
    return result

def plot_flight(flight_id):
    pred_vals = db.get_timeseries_arr("msl_predictions", "predicted_AltMSL", flight_id)
    exp_vals = db.get_timeseries_arr("msl_predictions", "expected_AltMSL", flight_id)

    x = np.arange(0, len(pred_vals))
    y0 = np.array(pred_vals)
    y1 = np.array(exp_vals)

    plt.plot(x, y0, color ="blue")
    plt.plot(x, y1, color ="red")
    plt.show()

def plot_all_flights():
    flights = get_flights(db)

    i = 0
    for flight in flights:
        if i == 1:
            break

        plot_flight(int(flight[0]))

        i += 1


db_name = sys.argv[1]
flight_id = int(sys.argv[2])

db.init(db_name)

print(f"Plotting flight {flight_id} from db: {db_name}")
plot_flight(int(sys.argv[2]))
