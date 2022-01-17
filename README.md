# farm-sprayer-kalman
Simulation of Kalman Filter for measuring position and velocity of herbicide droplet.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/aschneer/farm-sprayer-kalman/HEAD)

**Goal:**

Model a distance sensor and velocity sensor measuring a droplet of herbicide as it is sprayed downward toward the ground. Use a Kalman Filter to improve the measurement, and compare the results of the Kalman filter with the raw measurements.

**Assumptions:**

- All Kalman Filter error matrices are set to zero (except measurement error).
