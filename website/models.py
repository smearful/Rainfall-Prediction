from django.db import models

class WeatherPrediction(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    predicted_rainfall = models.FloatField()  # Store ML prediction result
    date_recorded = models.DateTimeField(auto_now_add=True)  # Auto adds timestamp
