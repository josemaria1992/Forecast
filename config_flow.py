from homeassistant import config_entries
from homeassistant.const import CONF_NAME
import logging

_LOGGER = logging.getLogger(__name__)

class ForecastLoadConsumptionConfigFlow(config_entries.ConfigFlow):
    """Handle a config flow for Forecast Load Consumption."""

    def __init__(self):
        self._name = "Forecast Load Consumption"

    async def async_step_user(self, user_input=None):
        """Handle the initial step of the config flow."""
        if user_input is None:
            return self.async_show_form(step_id="user")
        
        return self.async_create_entry(
            title=self._name,
            data=user_input
        )
