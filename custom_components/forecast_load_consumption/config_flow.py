import voluptuous as vol
from homeassistant import config_entries

from .const import CONF_NAME, DOMAIN


class ForecastLoadConsumptionConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Forecast Load Consumption."""

    def __init__(self) -> None:
        super().__init__()
        self._name = "Forecast Load Consumption"

    async def async_step_user(self, user_input=None):
        """Handle the initial step of the config flow."""
        if user_input is None:
            return self.async_show_form(
                step_id="user",
                data_schema=vol.Schema({vol.Optional(CONF_NAME, default=self._name): str}),
            )

        self._name = user_input.get(CONF_NAME, self._name)
        return self.async_create_entry(
            title=self._name,
            data=user_input,
        )
