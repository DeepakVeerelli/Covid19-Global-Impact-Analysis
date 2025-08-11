# Covid19-Global-Impact-Analysis

This project analyzes the global impact of COVID-19 by processing, transforming, and visualizing pandemic data using Python and Power BI. It covers data loading, cleaning, transformation, and a series of insightful visualizations that help uncover trends, correlations, and the effect of government policies.

---

## Table of Contents

- [Overview](#overview)
- [Data Sources](#data-sources)
- [Python Workflow](#python-workflow)
  - [Loading Data](#loading-data)
  - [Cleaning Data](#cleaning-data)
  - [Transforming Data](#transforming-data)
- [Python Visualizations](#python-visualizations)
- [Power BI Visualizations](#power-bi-visualizations)
  - [Cases & Deaths Area Chart](#cases--deaths-area-chart)
  - [Total Cases Stacked Column Chart](#total-cases-stacked-column-chart)
  - [Policy Intensity Heatmap](#policy-intensity-heatmap)
  - [Vaccination Rate vs Case Rate Scatterplot](#vaccination-rate-vs-case-rate-scatterplot)
- [How to Run](#how-to-run)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Covid19-Global-Impact-Analysis provides a comprehensive examination of the COVID-19 pandemic using global datasets. The workflow involves Python-based data wrangling and visualization, followed by advanced analytics and dashboards in Power BI.

---

## Data Source

- **owid_covid_data** https://github.com/owid/covid-19-data/tree/master/public/data

---

## Python Workflow

The initial data analysis phase is performed in Python, which includes loading, cleaning, and transforming the raw data.

### Loading Data

```python
import pandas as pd

# Load dataset
df = pd.read_csv('data/owid_covid_data.csv')
```

### Cleaning Data

```python
# Remove missing and duplicate values
cases_df.dropna(inplace=True)
cases_df.drop_duplicates(inplace=True)

# Example: Standardize country names
df['country'] = cases_df['country'].str.strip().str.title()
```

### Transforming Data

```python
# Create new features
df['vaccination_rate'] = (df['people_fully_vaccinated'] / df['population']) * 100
df['deaths_per_100k'] = (df['total_deaths'] / df['population']) * 100000
```

---

## Python Visualizations

Use Matplotlib for initial exploration and visualization.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='stringency_index', bins=30, kde=True)
plt.title('Distribution of Stringency Index')
plt.xlabel('Stringency Index')
plt.ylabel('Frequency')
plt.show()
```

---

## Power BI Visualizations

After transforming and exporting the data (`owid_covid_data`), import it into Power BI for advanced analysis.

### Cases & Deaths Area Chart

- Visualizes daily and cumulative cases and deaths over time for selected countries.

### Total Cases Stacked Column Chart

- Shows total cases per country, stacked by continent or other demographic segments.

### Policy Intensity matrix

- Uses OxCGRT policy indices to represent government response intensity over time and across countries.

### Vaccination Rate vs Case Rate Scatterplot

- Plots vaccination rate against case rate to explore trends and correlations, helping track the impact of vaccination campaigns.

---

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/DeepakVeerelli/Covid19-Global-Impact-Analysis.git
   cd Covid19-Global-Impact-Analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Python scripts**
   ```bash
   python scripts/data_processing.py
   python scripts/visualization.py
   ```

4. **Open Power BI**
   - Import `output/cleaned_data.csv`.
   - Use the provided Power BI template (`powerbi/Covid19_Impact.pbix`) to view and customize dashboards.

---

## Dependencies

- Python 3.7+
- pandas
- matplotlib
- Power BI Desktop

See `requirements.txt` for full Python dependencies.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new visualizations.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
