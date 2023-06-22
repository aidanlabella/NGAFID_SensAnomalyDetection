DROP TABLE IF EXISTS flights;
-- DROP TABLE IF EXISTS oilt_predictions; 
-- DROP TABLE IF EXISTS oilp_predictions; 
-- DROP TABLE IF EXISTS amp_predictions; 
-- DROP TABLE IF EXISTS volt_predictions; 
-- DROP TABLE IF EXISTS msl_predictions; 
-- -- This is the "base" info for the flights

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
    volt1 REAL,
    volt2 REAL,
    amp1 REAL,
    amp2 REAL,
    AltMSL REAL,
    AltB REAL,
    AltGPS REAL,
    Pitch REAL,
    VSpd REAL,
    PRIMARY KEY(flight_id, timestep)
);

-- -- We will create a new table for all of our new parameter predictions

-- -- Oil Pressure Predictions
-- CREATE TABLE oilp_predictions (
    -- flight_id INT,
    -- genome_id INT,
    -- timestep INT,
    -- expected_E1_OilP REAL,
    -- predicted_E1_OilP REAL,

    -- PRIMARY KEY(flight_id, genome_id, timestep),
    -- FOREIGN KEY (flight_id, timestep) REFERENCES flights (flight_id, timestep)
-- );

-- -- Oil Temp Predictions
-- CREATE TABLE oilt_predictions (
    -- flight_id INT,
    -- genome_id INT,
    -- timestep INT,
    -- expected_E1_OilT REAL,
    -- predicted_E1_OilT REAL,

    -- PRIMARY KEY(flight_id, genome_id, timestep),
    -- FOREIGN KEY (flight_id, timestep) REFERENCES flights (flight_id, timestep)
-- );

-- -- Current (amp) Predictions
-- CREATE TABLE amp_predictions (
    -- flight_id INT,
    -- genome_id INT,
    -- timestep INT,
    -- expected_amp1 REAL,
    -- predicted_amp1 REAL,
    -- expected_amp2 REAL,
    -- predicted_amp2 REAL,

    -- PRIMARY KEY(flight_id, genome_id, timestep),
    -- FOREIGN KEY (flight_id, timestep) REFERENCES flights (flight_id, timestep)
-- );

-- -- EMF (volt) Predictions
-- CREATE TABLE volt_predictions (
    -- flight_id INT,
    -- genome_id INT,
    -- timestep INT,
    -- expected_volt1 REAL,
    -- predicted_volt1 REAL,
    -- expected_volt2 REAL,
    -- predicted_volt2 REAL,

    -- PRIMARY KEY(flight_id, genome_id, timestep),
    -- FOREIGN KEY (flight_id, timestep) REFERENCES flights (flight_id, timestep)
-- );

-- Altitude (MSL) Predictions
-- CREATE TABLE msl_predictions (
    -- flight_id INT,
    -- genome_id INT,
    -- timestep INT,
    -- expected_AltMSL REAL,
    -- predicted_AltMSL REAL,

    -- PRIMARY KEY(flight_id, genome_id, timestep),
    -- FOREIGN KEY (flight_id, timestep) REFERENCES flights (flight_id, timestep)
-- );

-- VIEW for Altitude diffs
-- Can be a template for other views (diffs)
-- CREATE VIEW msl_diff AS 
    -- SELECT
        -- msl.flight_id AS flight_id,
        -- msl.genome_id AS genome_id,
        -- msl.timestep AS timestep,
        -- msl.expected_AltMSL AS expected_AltMSL,
        -- msl.predicted_AltMSL AS predicted_AltMSL,
        -- flt.AltMSL AS AltMSL,
        -- ABS(msl.expected_AltMSL - msl.predicted_AltMSL) AS AltMSLDiff
    -- FROM 
        -- msl_predictions AS msl
    -- JOIN
        -- flights AS flt
        -- ON
            -- msl.flight_id = flt.flight_id AND msl.timestep = flt.timestep
-- ;
