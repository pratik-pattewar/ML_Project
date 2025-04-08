from sklearn.preprocessing import LabelEncoder
import pandas as pd
df=pd.read_csv('diabetes_prediction_dataset.csv')
print(df.select_dtypes(include=['object']).columns)
label_encoder = LabelEncoder()

# Apply Label Encoding to all object (categorical) columns
for col in df.select_dtypes(include=['object']).columns:
    df[col] = label_encoder.fit_transform(df[col])
print(df.head)
df.to_csv('diabetes.csv',index=False)