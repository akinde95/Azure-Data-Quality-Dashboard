# Azure Data Quality Dashboard

In an effort to replicate similar work I have done, I built this data quality dashboard project using the Titanic dataset from Kaggle. It analyzes missing values, duplicates, and outliers.

## Project Details
- **Dataset**: Titanic (train.csv), ~891 rows.
- **Tools**: Python, Pandas, Plotly, GitHub, Azure Static Web Apps.
- **Metrics**:
  - Missing Values: e.g., ~19.8% in Age, ~77.1% in Cabin.
  - Duplicates: 0 full-row duplicates.
  - Outliers: e.g., 38 in Fare (>131.6).
- **Visualizations**: Bar chart (missing values), scatter plot (outliers).

## Setup
1. Clone this repo: `git clone https://github.com/akinde95/Azure-Data-Quality-Dashboard.git`.
2. Install dependencies: `pip install pandas plotly`.
3. Run `python data_quality.py` to generate metrics and charts.

## Deployment
- Live at: [Titanic Dashboard](https://gray-island-05a9a2e10.1.azurestaticapps.net)

## Notes
- Initial dataset (Air Quality) had low variance, leading to a switch to Titanic, dataset was provided by Kaggle.
- Charts are in the `templates/` folder.
