from threading import Event, Lock, Thread

import numpy as np
from numpy.random import binomial, normal


class StationSimulator:
    """Class for weather station simulation.

    After the simulation begins, measures are updated repeatedly
    after a number of seconds given in simulation_interval.
    However, measures correspond to those provided by sensors each hour.
    The sole purpose of simulation_interval is to implicitly control the
    simulation rate.
    Default values correspond to climate data for Bergen in May
    from 1981 to 2010, see Wikipedia.

    Parameters
    ----------
    location
        Name of the location.
    month
        Month.
    avg_high_temp
        Average high °C
    avg_low_temp
        Average low °C
    avg_precipitation
        Average precipitation mm
    avg_precipitation_days
        Average precipitation days
    simulation_interval
        Elapsed time between simulations in seconds.
        Default value is 3600 (1h)."""

    _days_of_month = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    def __init__(self,
                 location: str = "Bergen",
                 month: str = "May",
                 avg_high_temp: int = 15,
                 avg_low_temp: int = 7,
                 avg_precipitation: int = 105,
                 avg_precipitation_days: int = 12,
                 simulation_interval: int = 3600) -> None:

        self._location = location
        self._month = month

        # Initialize temperature parameters
        self._temp_interval = (avg_high_temp - avg_low_temp) / 2
        self._avg_temp = (avg_high_temp + avg_low_temp) / 2

        # Initialize precipitation parameters
        self._prob_rainy_day = avg_precipitation_days / \
            self._days_of_month[month]
        self._avg_precipitation_rainy_day = avg_precipitation / \
            (12 * avg_precipitation_days)

        self._simulation_interval = simulation_interval

        # Internal reading of the sensors. It is assumed that the sensors
        # need at least one hour to provide accurate measures.
        self._temperature = 0
        self._rain = 0

        # Lock to avoid races for self._temperature and self._rain
        self._lock = Lock()

    def _simulate(self):

        temperature = (self._avg_temp + self._temp_interval *
                       np.sin(np.pi * self._hour / 12 - np.pi / 2) + normal())
        rain = max(normal(self._avg_precipitation_rainy_day),
                   0) if self._is_rainy_day else 0

        with self._lock:
            self._temperature = temperature
            self._rain = rain

    def _update(self):

        while not self._shutting_down.wait(self._simulation_interval):
            self._simulate()
            self._hour = (self._hour + 1) % 24
            if not self._hour:
                self._is_rainy_day = binomial(1, self._prob_rainy_day)

    def turn_on(self, starting_hour: int = 0):
        """Starts the simulation.

        Parameter
        ---------
        starting_hour
            The hour at which the simulation starts."""

        self._shutting_down = Event()
        self._is_rainy_day = 0
        self._hour = starting_hour

        Thread(target=self._update).start()

    def shut_down(self):
        """Stops the simulation."""
        self._shutting_down.set()

    @property
    def location(self):
        """
        Location
        """
        return self._location

    @property
    def month(self):
        """
        Month
        """
        return self._month

    @property
    def temperature(self):
        """Current temperature."""
        with self._lock:
            return round(self._temperature, 2)

    @property
    def rain(self):
        """Current rain."""
        with self._lock:
            return round(self._rain, 2)
