import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_data(patient_data, hospital_data, public_health_data):
    patient_df = pd.DataFrame(patient_data)
    hospital_df = pd.DataFrame(hospital_data)
    public_health_df = pd.DataFrame(public_health_data)

    # Example visualizations
    plt.figure(figsize=(10, 6))
    sns.countplot(x='gender', data=patient_df)
    plt.title('Patient Gender Distribution')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(patient_df['age'], bins=20, kde=True)
    plt.title('Patient Age Distribution')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.countplot(x='department', data=hospital_df)
    plt.title('Hospital Department Distribution')
    plt.show()
