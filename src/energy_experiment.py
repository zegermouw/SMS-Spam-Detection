from text_classification import generate_model
from joblib import load
from text_preprocessing import _load_data
from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()
algorithm = "Decision Tree"
raw_data = _load_data()
preprocessed_data = load('output/preprocessed_data.joblib')
classifier, X_train, X_test, y_train, y_test, test_messages =  generate_model(algorithm, raw_data, preprocessed_data)
energy_consumption_kwh = tracker.stop()
energy_consumption = energy_consumption_kwh * 1000 * 3600 #Joules
duration = tracker._last_measured_time - tracker._start_time
print(f"Energy Consumption: {energy_consumption} Joules")
print(f"Duration: {duration} seconds")
    
