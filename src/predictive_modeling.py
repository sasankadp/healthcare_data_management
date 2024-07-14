import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_predictive_model(patient_data):
    patient_df = pd.DataFrame(patient_data)

    # Feature selection
    X = patient_df[['age', 'gender']]
    y = patient_df['outcome']

    # Convert categorical variables to numerical
    X = pd.get_dummies(X, columns=['gender'], drop_first=True)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    return model

def predict_outcome(model, patient_data):
    X = pd.DataFrame([patient_data])
    X = pd.get_dummies(X, columns=['gender'], drop_first=True)
    outcome = model.predict(X)
    return outcome
