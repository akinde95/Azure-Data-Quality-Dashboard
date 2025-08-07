# Azure Data Quality Dashboard

In an effort to replicate some similar work I have done at previous employers without using company data or IP, I built this project as a data quality dashboard using the Titanic dataset from Kaggle, analyzing missing values, duplicates, and outliers.

## Project Details
- **Dataset**: Titanic (train.csv), ~891 rows.
- **Tools**: Python, Pandas, Plotly, GitHub.
- **Metrics**:
  - Missing Values: e.g., ~19.8% in Age, ~77.1% in Cabin.
  - Duplicates: 0 full-row duplicates.
  - Outliers: e.g., 38 in Fare (>131.6).
- **Visualizations**: Bar chart (missing values), scatter plot (outliers).

## Setup
1. Clone this repo: `git clone https://github.com/akinde95/Azure-Data-Quality-Dashboard.git`.
2. Install dependencies: `pip install pandas plotly`.
3. Run `python data_quality.py` to generate metrics and charts.

## Notes
- Initial dataset (Air Quality) had low variance, leading to a switch to Titanic.
- Charts are in the `templates/` folder.
- `.DS_Store` is a macOS metadata file, safely ignorable.

## Future Work
- Deploy to Azure (Week 3).
- Add interactive features (Week 5).