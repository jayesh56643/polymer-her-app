
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Step 1: Sample Data
data = {
    'Polymer': ['P1', 'P2', 'P3', 'P4', 'P5'],
    'Bandgap_eV': [2.3, 1.8, 2.5, 2.0, 1.6],
    'Stability': [8.5, 6.5, 9.0, 7.0, 5.5],
    'Surface_Area': [125, 110, 140, 115, 105],
    'HER': [300, 150, 350, 200, 100]  # µmol/h/g
}

df = pd.DataFrame(data)

# Step 2: Features and Target
X = df[['Bandgap_eV', 'Stability', 'Surface_Area']]
y = df['HER']

# Step 3: Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Test MSE: {mse:.2f}")

# Step 6: Save Model
joblib.dump(model, 'polymer_her_predictor.pkl')
print("✅ Model saved as 'polymer_her_predictor.pkl'")
