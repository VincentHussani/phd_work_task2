import numpy as np
import pandas as pd
from typing import Callable
from scipy.stats import shapiro, levene, ttest_ind,ks_2samp, chi2_contingency


# Function to decide which test to run for continuous data
def test_cont(orig: pd.DataFrame, gen: pd.DataFrame, col: str):
    # Shapiro wilks test is done to assess normality
    shapiro_orig_p = shapiro(orig[col]).pvalue
    shapiro_gen_p = shapiro(gen[col]).pvalue
    normal = shapiro_orig_p > 0.05 and shapiro_gen_p > 0.05

    # Levene’s test for equal variances
    levene_p = levene(orig[col], gen[col]).pvalue
    equal_var = levene_p > 0.05

    print(f"{col} - Shapiro p-values: orig={shapiro_orig_p}, gen={shapiro_gen_p}, Levene p={levene_p:.3f}")

    if normal:
        t_stat, t_p = ttest_ind(orig[col], gen[col], equal_var=equal_var)
        result = "The distributions are similar (desired result)" if t_p > 0.05 else "Different distributions (not good)"
        print(f"t-test {col}:\np-value = {t_p}\n{result}\n")
    else:
        ks_stat, ks_p = ks_2samp(orig[col], gen[col])
        result = "The distributions are similar (desired result)" if ks_p > 0.05 else "Different distributions (not good)"
        print(f"KS test {col}:\np-value = {ks_p}\n{result}\n")


# Chi-Squared Test for Category1
def chi_squared_test(orig, gen, column):
    orig_counts = orig[column].value_counts().sort_index()
    gen_counts = gen[column].value_counts().reindex(orig_counts.index, fill_value=0)
    contingency = pd.DataFrame({"orig": orig_counts, "gen": gen_counts})
    stat, p, _, _ = chi2_contingency(contingency.T)
    result = "The distributions are similar (desired result)" if p > 0.05 else "Different distributions (not good)"
    print(f"Chi-Squared Test {column}: \nChi2-statistic = {stat}, p-value = {p}\n{result}" )


def test_n(df: pd.DataFrame, gen: Callable[[], pd.DataFrame], n: int = 1000):
    results = []

    for i in range(n):
        df_gen = gen()
        row = {}

        for col in ["Value1", "Value2"]:
            shapiro_orig_p = shapiro(df[col]).pvalue
            shapiro_gen_p = shapiro(df_gen[col]).pvalue
            normal = shapiro_orig_p > 0.05 and shapiro_gen_p > 0.05
            row[f"{col}_shapiro_gen_p"] = shapiro_gen_p

            levene_p = levene(df[col], df_gen[col]).pvalue
            row[f"{col}_levene_p"] = levene_p

            if normal:
                t_p = ttest_ind(df[col], df_gen[col], equal_var=levene_p > 0.05).pvalue
                row[f"{col}_p"] = t_p
            else:
                ks_p = ks_2samp(df[col], df_gen[col]).pvalue
                row[f"{col}_p"] = ks_p

        # Chi-squared test for Category1
        cat_orig = df["Category1"].value_counts().sort_index()
        cat_gen = df_gen["Category1"].value_counts().reindex(cat_orig.index, fill_value=0)
        chi2_p = chi2_contingency(pd.DataFrame([cat_orig, cat_gen]))[1]
        row["Category1p"] = chi2_p

        results.append(row)

    results_df = pd.DataFrame(results)
    print("Summary statistics:")
    print(results_df.describe())

    print("\nNumber of fails (p < 0.05):")
    fail_counts = (results_df < 0.05).sum()
    print(fail_counts)

    return results_df
