-- This is the "base" info for the flights

CREATE TABLE flights (
    flight_id INT,
    timestep INT,
    E1_CHT1 REAL,
    E1_CHT2 REAL,
    E1_CHT3 REAL,
    E1_CHT4 REAL,
    E1_EGT1 REAL,
    E1_EGT2 REAL,
    E1_EGT3 REAL,
    E1_EGT4 REAL,
    E1_FFlow REAL,
    E1_OilP REAL,
    E1_OilT REAL,
    E1_RPM REAL,
    PRIMARY KEY(flight_id, timestep)
)

-- We will create a new table for all of our new parameter predictions

-- Oil Pressure Predictions
CREATE TABLE oilp_predictions (
    flight_id INT,
    genome_id INT,
    timestep INT,
    expected_E1_OilP REAL,
    predicted_E1_OilP REAL,

    PRIMARY KEY(flight_id, genome_id, timestep)
);

-- Oil Temp Predictions
CREATE TABLE oilt_predictions (
    flight_id INT,
    genome_id INT,
    timestep INT,
    expected_E1_OilT REAL,
    predicted_E1_OilT REAL,

    PRIMARY KEY(flight_id, genome_id, timestep)
);
