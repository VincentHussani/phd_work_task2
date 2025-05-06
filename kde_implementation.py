import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde
from statistical_tests import *
# Monte carlo simulation, I decided to use functions to utilise test_n and get a better assessment of the simulation's abilities.
def sample_continuous_kde(series, n):
    kde = gaussian_kde(series)
    return kde.resample(n).flatten()

def monte_carlo_generate(df, n_samples=1000):
    probs = df["Category1"].value_counts(normalize=True).sort_index()
    cat1_samples = np.random.choice(probs.index, size=n_samples, p=probs.values)
    val1_samples = sample_continuous_kde(df["Value1"], n_samples)
    val2_samples = sample_continuous_kde(df["Value2"], n_samples)

    df_new = pd.DataFrame({
        "Category1": cat1_samples,
        "Value1": val1_samples,
        "Value2": val2_samples
    })
    return df_new

if __name__ == '__main__':
    df = pd.read_csv("dataset.csv", sep=";")
    df_generated = monte_carlo_generate(df, n_samples=500)
    df_generated.to_csv("montecarlo_generated.csv", sep=";", index=False)
    test_cont(df, df_generated, "Value1")
    test_cont(df, df_generated, "Value2")
    chi_squared_test(df, df_generated, "Category1")
    test_n(df,lambda: monte_carlo_generate(df, n_samples=1000))
