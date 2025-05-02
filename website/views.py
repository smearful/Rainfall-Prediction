from django.shortcuts import redirect, render
import pandas as pd
from .Weather_Prediction import train_model

def home(request):
    return render(request, 'website/index.html')

def redirect_to_home(request):
    return redirect("home")

def data(request):
    return render(request, 'website/data.html')

# Train the model once at startup
model, feature_names = train_model()

def predict_rainfall(request):
    prediction = None

    if request.method == "POST":
        # Get user input safely
        hi_temp = request.POST.get("temperature_hi", "").strip()
        low_temp = request.POST.get("temperature_low", "").strip()
        humidity = request.POST.get("humidity", "").strip()
        pressure = request.POST.get("pressure", "").strip()

        # Assign default values if fields are empty
        hi_temp = float(hi_temp) if hi_temp else 27.5
        low_temp = float(low_temp) if low_temp else 25.0
        humidity = float(humidity) if humidity else 50.0
        pressure = float(pressure) if pressure else 1003.0

        # Prepare input for prediction
        input_data = pd.DataFrame({
            'temperature_hi': [hi_temp],
            'temperature_low': [low_temp],
            'humidity': [humidity],
            'pressure': [pressure]
        })

        # Run the model's prediction
        prediction = model.predict(input_data)[0]
        prediction_text = "It is likely to rain today!" if prediction == 1 else "It is unlikely to rain today!"

        return render(request, "website/data.html", {"prediction": prediction_text, "input_data": input_data})

    return render(request, "website/index.html", {"prediction": "Please fill in all fields."})