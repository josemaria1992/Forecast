import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def train_arima_model(training_data):
    """Train the ARIMA model."""
    model = ARIMA(training_data, order=(1, 1, 1))  # Simple ARIMA model
    model_fit = model.fit()
    return model_fit

def get_forecast(model_fit, steps=96):
    """Generate a forecast using the trained ARIMA model."""
    forecast = model_fit.forecast(steps=steps)
    return forecast

def get_latest_forecast():
    """Get the most recent forecast."""
    # In reality, you would use the trained ARIMA model here
    forecast = [2149.7, 2165.9, 2177.1, 2185.0, 2190.5]  # Example forecast data
    return forecast
