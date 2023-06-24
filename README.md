# NGAFID Sensor Anomaly Detection
* This work is for detecting anomalous readings from NGAFID data using RNNs

## Experimental Design
* Using `N` evolved RNNs, we will attempt to predict the following **ENGINE** parameters:
    1. `E1_OilP`
    2. `E1_OilT`
    3. `...`

* We can use `N` evolved RNNs to predice the following **FLIGHT** parameters:
    1. `AltMSL`
        * Inputs: `AltB, AltGPS, Pitch, VSpd`
