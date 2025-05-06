import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

if __name__ == '__main__':
    original_df = pd.read_csv('dataset.csv', sep=';')
    original_df.drop('Unnamed: 0', axis=1, inplace=True)
    montecarlo_df = pd.read_csv('montecarlo_generated.csv', sep=';')
    gmm_df = pd.read_csv('gmm_generated.csv', sep=';')
    datasets = [original_df, montecarlo_df, gmm_df]
    labels = ['Original', 'Montecarlo', 'GMM']
    colors = ['cyan', 'magenta', 'yellow']

    plt.figure(figsize=(15, 9)) # golden ratio-ish :)

    #Value 1
    plt.subplot(1, 3, 1)
    for df, label, color in zip(datasets, labels, colors):
        sns.kdeplot(df['Value1'], label=label, color=color, fill=True, alpha=0.4, linewidth=1.5)
    plt.title('Distribution of Value1')
    plt.xlabel('Value1')
    plt.ylabel('Density')
    plt.legend()
    #Value 2
    plt.subplot(1, 3, 2)
    for df, label, color in zip(datasets, labels, colors):
        sns.kdeplot(df['Value2'], label=label, color=color, fill=True, alpha=0.4, linewidth=1.5)
    plt.title('Distribution of Value2')
    plt.xlabel('Value2')
    plt.ylabel('Density')
    plt.legend()

    # Category1
    plt.subplot(1, 3, 3)
    categories = set().union(*(df['Category1'].unique() for df in datasets))
    x = range(len(categories))
    category_list = sorted(categories)

    bar_width = 0.25
    for i in range(len(datasets)):
        df = datasets[i]
        label = labels[i]
        color = colors[i]

        counts = df['Category1'].value_counts()
        normalized_values = []
        for category in category_list:
            count = counts.get(category, 0)
            proportion = count / len(df)
            normalized_values.append(proportion)

        # Compute bar positions
        positions = [j + i * bar_width for j in x]

        # Plot bars
        plt.bar(
            positions,
            normalized_values,
            width=bar_width,
            label=label,
            color=color,
            edgecolor='black'
        )

    plt.xticks([p + bar_width for p in x], category_list)
    plt.title('Category1 Distribution')
    plt.xlabel('Category')
    plt.ylabel('Proportion')
    plt.legend()

    plt.tight_layout()
    plt.show()
