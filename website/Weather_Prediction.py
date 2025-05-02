import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def train_model():
    data = {
        'temperature_hi': [30.67, 29, 28.67, 27.67, 26, 28.67, 28.67, 28.34, 27, 23.67, 24.67, 28, 26.34, 24.67, 24],
        'temperature_low': [26, 25, 25.67, 24.67, 24.34, 25.67, 26.34, 25.67, 25, 23, 24, 25.67, 24.67, 24, 23.34],
        'humidity': [68.67, 77.67, 69.67, 81, 84.34, 74, 73.34, 75, 80.67, 91.34, 89.67, 76.34, 82.67, 86.67, 89.67],
        'pressure': [1008, 1006.67, 1006.34, 1004, 1003, 1003.67, 1005.67, 1005, 1004, 1005.34, 1005.34, 1007, 1007.67, 1005.34, 1004],
        'rain': [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1]
    }
    
    df = pd.DataFrame(data)
    X = df[['temperature_hi', 'temperature_low', 'humidity', 'pressure']]
    y = df['rain']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    return model, X.columns