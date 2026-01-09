from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_NAME
import logging

_LOGGER = logging.getLogger(__name__)

class ForecastLoadConsumptionSensor(Entity):
    """Representation of the forecasted load consumption sensor."""

    def __init__(self, name, forecast_data):
        self._name = name
        self._forecast_data = forecast_data

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._forecast_data

    async def async_update(self):
        """Update the sensor state with the latest forecast."""
        _LOGGER.info("Updating forecast load consumption sensor.")
        # Here you would fetch the latest forecast and update the state
        self._forecast_data = get_latest_forecast()
