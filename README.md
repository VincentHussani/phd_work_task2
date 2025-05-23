# PhD position @ BTH coding Assignment
This is my, Vincent Honar's, solution to the coding task. I decided to approach it using two methods:
  1. Using a purely statistical approach
  2. Using a generator and a more AI-aligned method.

During the implementation of this task, the following assumption(s) were made:
  1. The independence of the variables was known (could be determined easily using covariance. In a scenario where I am unaware of the distribution, data exploration would naturally be the first step)

# Evaluation method
To evaluate the models, statistical tests and visual aids were employed. A Shapiro-Wilk test and Levene's test are conducted on the two continuous variables to decide whether a parametric or non-parametric test is used. Levene's test has a null hypothesis that states that the populations have equal variance. Therefore, a p-value less than 0.05 means that there is unequal variance. A p-value of less than 0.05 for the Shapiro-Wilk test would reject the null hypothesis that the data is normally distributed. If either of these null hypotheses is rejected, then a parametric Kolmogorov-Smirnov test is employed. In the case where neither null hypothesis is rejected, a t-test is used. 

The categorical variable Category1 is tested using the Chi-square test. 

All models are tested 1000 times, and their results are presented in aggregate. The model outputs are visualised through two histograms and one bar plot. 
# Results
Both the Monte Carlo simulation and GMM manage to replicate the data successfully. 
## GMM
Only one out of a thousand GMM models fail in passing either the parametric or non-parametric test. 

### Table 1. Summary Statistics for the GMM.

| Metric            | Value1_shapiro_p | Value1_levene_p | Value1_p | Value2_shapiro_p | Value2_levene_p | Value2_p | Category1_p |
|------------------|------------------------|------------------|----------|------------------------|------------------|----------|-------------|
| **count**        | 1000                   | 1000             | 1000     | 1000                   | 1000             | 1000     | 1000        |
| **mean**         | 0.0652                 | 0.6597           | 0.7098   | 0.2577                 | 0.5861           | 0.6145   | 0.6277      |
| **std**          | 0.1201                 | 0.2249           | 0.2302   | 0.2615                 | 0.2539           | 0.2393   | 0.2424      |
| **min**          | 0.0000                 | 0.0161           | 0.0621   | 0.0001                 | 0.0116           | 0.0301   | 0.0531      |
| **25%**          | 0.0019                 | 0.4941           | 0.5639   | 0.0414                 | 0.3924           | 0.4343   | 0.4506      |
| **50%**          | 0.0143                 | 0.6852           | 0.7495   | 0.1606                 | 0.5945           | 0.6341   | 0.6517      |
| **75%**          | 0.0702                 | 0.8514           | 0.9028   | 0.4124                 | 0.8117           | 0.8184   | 0.8384      |
| **max**          | 0.9433                 | 0.9991           | 0.9996   | 0.9972                 | 0.9989           | 0.9994   | 0.9996      |

---

### Table 2. Number of Fails (p < 0.05) for the GMM.

| Test                    | Fails |
|-------------------------|--------|
| Value1_shapiro_gen_p    | 700    |
| Value1_levene_p         | 1      |
| Value1_p                | 0      |
| Value2_shapiro_gen_p    | 274    |
| Value2_levene_p         | 3      |
| Value2_p                | 1      |
| Category1_p              | 0      |

## Montecarlo
The Monte Carlo method performed marginally worse with a total of four distinct trials failing to pass their statistical tests. 
### Table 3. Summary Statistics for the Monte Carlo simulation.

| Metric    | Value1_shapiro_p | Value1_levene_p | Value1_p | Value2_shapiro_p | Value2_levene_p | Value2_p | Category1_p |
|-----------|-----------------------|------------------|----------|------------------------|------------------|----------|-------------|
| **count** | 1000.0000             | 1000.0000        | 1000.0000 | 1000.0000              | 1000.0000        | 1000.0000 | 1000.0000   |
| **mean**  | 0.1411                | 0.3909           | 0.6763   | 0.1829                 | 0.3866           | 0.6651   | 0.8380      |
| **std**   | 0.1942                | 0.2523           | 0.2280   | 0.1890                 | 0.2610           | 0.2344   | 0.1531      |
| **min**   | 0.0000                | 0.0080           | 0.0126   | 0.0000                 | 0.0018           | 0.0447   | 0.2347      |
| **25%**   | 0.0087                | 0.1820           | 0.5246   | 0.0419                 | 0.1640           | 0.5006   | 0.7669      |
| **50%**   | 0.0526                | 0.3403           | 0.7147   | 0.1176                 | 0.3360           | 0.7006   | 0.8875      |
| **75%**   | 0.1947                | 0.5626           | 0.8810   | 0.2566                 | 0.5594           | 0.8680   | 0.9548      |
| **max**   | 0.9658                | 0.9999           | 0.9995   | 0.9804                 | 0.9979           | 0.9999   | 0.9970      |

---

### Table 4. Number of Fails (p < 0.05) for the Montecarlo simulation.

| Test                   | Fails |
|------------------------|--------|
| Value1_shapiro_gen_p   | 492    |
| Value1_levene_p        | 31     |
| Value1_p               | 4      |
| Value2_shapiro_gen_p   | 281    |
| Value2_levene_p        | 39     |
| Value2_p               | 1      |
| Category1_p             | 0      |

## Visual aid 

![Figure 1. Results of generation methods](Figure_1.png)
Figure 1. Results of the generation methods. 

While the distributions are marginally visually dissimilar, the shape of the original data is assumed with a slight preference towards values in the lower bounds. Both models overrepresent category C while underrepresenting A and B. The Monte Carlo samples E more frequently while the GMM has a similar tendency for D. 

# Conclusion
Both approaches capture the nature of the data, with the GMM outperforming the Monte Carlo-based simulation.
