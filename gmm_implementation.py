import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import LabelEncoder, StandardScaler
from statistical_tests import *

# I put it in a function to ease multiple testing
def generate_samples_gmm(gmm, scaler, label_encoder, n):
    samples_scaled, _ = gmm.sample(n)
    samples = scaler.inverse_transform(samples_scaled)

    category_sampled = np.clip(np.round(samples[:, 0]), 0, len(label_encoder.classes_) - 1).astype(int)
    category_decoded = label_encoder.inverse_transform(category_sampled)

    df_gmm = pd.DataFrame({
        "Category1": category_decoded,
        "Value1": samples[:, 1],
        "Value2": samples[:, 2]
    })

    df_gmm["Value1"] = df_gmm["Value1"].astype(float)
    df_gmm["Value2"] = df_gmm["Value2"].astype(float)
    return df_gmm

if __name__ == '__main__':
    df = pd.read_csv("dataset.csv", sep=";")
    # We need to encode Category1 as integers
    label_encoder = LabelEncoder()
    df["Category_encoded"] = label_encoder.fit_transform(df["Category1"])

    # Stack all features: the model will learn the full joint distribution
    X = df[["Category_encoded", "Value1", "Value2"]].values

    # GMM is sensitive to scale :)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    gmm = GaussianMixture(n_components=6, covariance_type='full')
    gmm.fit(X_scaled)
    df_gmm = generate_samples_gmm(gmm,scaler,label_encoder,500)
    df_gmm.to_csv('gmm_generated.csv',sep=';',index=False)
    test_cont(df, df_gmm, "Value1")
    test_cont(df, df_gmm, "Value2")
    chi_squared_test(df, df_gmm, "Category1")
    test_n(df,lambda: generate_samples_gmm(gmm,scaler,label_encoder,1000))
