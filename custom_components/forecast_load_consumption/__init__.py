import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the forecast load consumption integration."""
    _LOGGER.info("Setting up forecast load consumption integration")
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the sensor for forecasted load consumption."""
    _LOGGER.info("Setting up forecast load consumption entry")
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload forecast load consumption integration."""
    _LOGGER.info("Unloading forecast load consumption entry")
    return True
