import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

columns = [
"Pregnancies","Glucose","BloodPressure",
"SkinThickness","Insulin","BMI",
"DiabetesPedigreeFunction","Age","Outcome"
]

data = pd.read_csv("dataset/diabetes.csv", names=columns)

X = data.drop("Outcome", axis=1)
y = data["Outcome"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
X,y,test_size=0.2,random_state=42
)

model = RandomForestClassifier()
model.fit(X_train,y_train)

pickle.dump(model,open("models/disease_model.pkl","wb"))
pickle.dump(scaler,open("models/scaler.pkl","wb"))

print("Model trained successfully")