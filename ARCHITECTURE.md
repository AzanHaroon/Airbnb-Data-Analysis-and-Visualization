# System Workflow / Architecture

```text
airbnb.csv
   |
   v
Pandas data loading
   |
   v
Cleaning + type conversion + feature preparation
   |
   +--------------------------+
   |                          |
   v                          v
Jupyter Notebook          Streamlit Dashboard
   |                          |
   v                          v
EDA / statistics          Filters / KPIs
charts / findings         charts / tables
   |                          |
   +------------+-------------+
                v
        Business Insights
                |
                v
       Documentation / Demo
```

## Main Components

- `airbnb.csv`: source dataset.
- `Airbnb_Analysis.ipynb`: reproducible analysis.
- `app.py`: interactive dashboard.
- `outputs/`: example analysis charts.
- `README.md`: complete project documentation.
