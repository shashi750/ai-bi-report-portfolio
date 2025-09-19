import pandas as pd
from sklearn.cluster import KMeans
import joblib

# Load dataset
df = pd.read_csv("data_sample/customers_sample1.csv")

# Select numeric features
numeric_features = ["Income"]

# One-hot encode categorical features
categorical_features = ["Education", "Marital_Status"]
df_encoded = pd.get_dummies(df[categorical_features])

# Combine numeric + encoded categorical features
X = pd.concat([df[numeric_features], df_encoded], axis=1)

# Drop rows with missing values in X
X_clean = X.dropna()

# Train clustering model
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_clean)

# Assign clusters back to original df
df.loc[X_clean.index, "Cluster"] = clusters

# Save model
joblib.dump(kmeans, "customer_segmentation_model.pkl")

# Save clustered data
df.to_csv("data_sample/customers_clustered.csv", index=False)

print("✅ Model trained with categorical features and clustered data saved!")
