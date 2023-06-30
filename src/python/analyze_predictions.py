import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import db
import plotly.express as px
import plotly.graph_objects as go
import os
import sys

def get_flights(db):
    sql = "SELECT DISTINCT flight_id FROM msl_diff"
    result = db.query(sql)
    return result

def plot_flight(flight_id, genome_id):
    pred_vals = db.get_timeseries_arr("msl_predictions_noise_10_10", "predicted_AltMSL", flight_id, genome_id)
    exp_vals = db.get_timeseries_arr("msl_predictions_noise_10_10", "expected_AltMSL", flight_id, genome_id)

    x = np.arange(0, len(pred_vals))
    y0 = np.array(pred_vals)
    y1 = np.array(exp_vals)

    # plt.set_title(f"")
    # plt.plot(x, y0, color ="blue")
    # plt.plot(x, y1, color ="red")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y0, name="predicted", line_shape='linear'))
    fig.add_trace(go.Scatter(x=x, y=y1, name="expected", line_shape='linear'))
    fig.show()
    # plt.show()

def plot_flight_all_genomes(flight_id, table_name, table_view):
    pred_vals = db.get_timeseries_arr(table_name, "predicted_AltMSL", flight_id, 1)
    exp_vals = db.get_timeseries_arr(table_name, "expected_AltMSL", flight_id, 1)

    x = np.arange(0, len(pred_vals))
    y0 = np.array(pred_vals)
    y1 = np.array(exp_vals)

    # plt.set_title(f"")
    # plt.plot(x, y0, color ="blue")
    # plt.plot(x, y1, color ="red")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y1, name="expected", line_shape='linear'))
    fig.add_trace(go.Scatter(x=x, y=y0, name="predicted_genome_1", line_shape='linear'))

    for i in range(2, 10):
        pred_vals = db.get_timeseries_arr(table_name, "predicted_AltMSL", flight_id, i)
        fig.add_trace(go.Scatter(x=x, y=np.array(pred_vals), name=f"predicted_genome_{i}", line_shape='linear'))

    fig.show()

    # Plot the diffs
    if table_view is not None:
        diff_vals = db.get_timeseries_arr(table_view, "AltMSLDiff", flight_id, 1)

        x = np.arange(0, len(diff_vals))
        y0 = np.array(diff_vals)

        # plt.set_title(f"")
        # plt.plot(x, y0, color ="blue")
        # plt.plot(x, y1, color ="red")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y0, name="diff_genome_1", line_shape='linear'))

        for i in range(2, 10):
            diff_vals = db.get_timeseries_arr(table_view, "AltMSLDiff", flight_id, i)
            fig.add_trace(go.Scatter(x=x, y=np.array(diff_vals), name=f"diff_genome_{i}", line_shape='linear'))

        fig.show()

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
genome_id = int(sys.argv[3])

table_name = "msl_predictions_noise_10_10"
table_view = "msl_diff_noise_10_10"

db.init(db_name)

if genome_id < 0:
    print(f"Plotting flight {flight_id} from db: {db_name} for all genomes")
    plot_flight_all_genomes(flight_id, table_name, table_view)
else:
    print(f"Plotting flight {flight_id} from db: {db_name} and genome_id: {genome_id}")
    plot_flight(flight_id, genome_id)
