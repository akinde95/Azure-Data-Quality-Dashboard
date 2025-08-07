import pandas as pd
import os

try:
    import plotly.express as px
except ImportError:
    print("Plotly Express not found. Please install it with 'pip install plotly' and rerun.")
    exit()

# Load dataset
df = pd.read_csv('titanic.csv')
print(f"Original row count: {len(df)}")
print(f"First few rows:\n", df.head())

# Debug column types
print("Column data types:\n", df.dtypes)
print("Non-missing counts per column:\n", df.notnull().sum())

# Select only true numerical columns (exclude objects)
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
print(f"Numerical columns: {numerical_cols}")

# Calculate data quality metrics
missing_values = df.isnull().sum() / len(df) * 100
duplicates = df.duplicated(keep=False).sum()
print(f"Total duplicates (including first occurrences): {duplicates}")

# Outlier detection for numerical columns only
accuracy_metrics = {}
for col in numerical_cols:
    mean = df[col].mean()
    std = df[col].std()
    if pd.notna(std) and std > 0:
        outliers = len(df[df[col] > mean + 2 * std])
        if outliers > 0:
            accuracy_metrics[col] = {'outliers': outliers, 'mean': mean, 'std': std}
print(f"Accuracy Metrics: {accuracy_metrics}")

# Filter out 100% missing columns
missing_values = missing_values[missing_values < 100]
metrics = []
values = []
if not missing_values.empty:
    metrics.extend(['Missing_%_' + col for col in missing_values.index])
    values.extend(missing_values.tolist())
if duplicates is not None and duplicates > 0:
    metrics.append('Duplicates')
    values.append(duplicates)
for col in accuracy_metrics:
    metrics.append('Outliers_' + col)
    values.append(accuracy_metrics[col]['outliers'])

if metrics and values:
    metrics_df = pd.DataFrame({'Metric': metrics, 'Value': values})
    metrics_df.to_csv('metrics.csv', index=False)
    print("Metrics saved to metrics.csv")
else:
    print("No valid metrics to save due to empty data or no duplicates/outliers")

# Generate Plotly visualizations
if not os.path.exists('templates'):
    os.makedirs('templates')

# Bar chart for missing values
if not missing_values.empty:
    fig1 = px.bar(x=missing_values.index, y=missing_values, title="Missing Values (%)",
                  labels={'x': 'Columns', 'y': 'Percentage Missing'},
                  color=missing_values, color_continuous_scale='Viridis')
    fig1.write_html('templates/missing_values.html')
    print("Missing Values chart generated.")

# Pie chart for duplicates
if duplicates is not None and duplicates > 0:
    fig2 = px.pie(values=[len(df) - duplicates, duplicates], names=['Unique Rows', 'Duplicates'],
                  title="Duplicate Rows", color_discrete_sequence=['#1f77b4', '#ff7f0e'])
    fig2.write_html('templates/duplicates.html')
    print("Duplicates chart generated.")

# Scatter plot for outliers (using Fare if present)
if 'Fare' in numerical_cols and 'Fare' in accuracy_metrics and accuracy_metrics['Fare']['outliers'] > 0:
    fig3 = px.scatter(df, x=df.index, y='Fare', title="Outliers in Fare",
                      color=(df['Fare'] > df['Fare'].mean() + 2 * df['Fare'].std()),
                      color_discrete_map={True: '#ff0000', False: '#0000ff'})
    fig3.write_html('templates/outliers.html')
    print("Outliers chart generated.")
else:
    print("No scatter plot generated: 'Fare' missing, no outliers, or not numerical.")

# Print results
print("Missing Values (%):", missing_values)
print("Duplicates:", duplicates)
print("Accuracy Metrics:", accuracy_metrics)
