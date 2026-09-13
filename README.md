# Airbnb Data Analysis and Visualization

An end-to-end **Data Science and Data Visualization** project that analyzes Airbnb listing data and presents the results through an interactive Streamlit dashboard.

## Project Overview

This project uses a supplied Airbnb listings dataset containing information about listings, hosts, locations, prices, ratings, reviews, guest capacity, beds, bedrooms, bathrooms, amenities, rules, and check-in/check-out information.

The project has two main deliverables:

1. **Jupyter Notebook** — complete data cleaning, exploratory data analysis (EDA), statistics, visualizations, and findings.
2. **Streamlit Dashboard** — interactive filtering and visualization for exploring the dataset.

> **Price/currency note:** The dataset contains a `price` column but does not contain a currency field. Therefore, this project reports price as **dataset price units** and does not assume that the values are USD.

## Objectives

- Inspect and understand the Airbnb dataset.
- Clean inconsistent data types and missing values.
- Convert rating and review fields into analysis-ready numeric values.
- Analyze listing distribution by country.
- Study price distribution and price outliers.
- Analyze ratings and review activity.
- Compare prices by guest capacity and property characteristics.
- Build an interactive dashboard.
- Produce clear business-oriented findings and recommendations.

## Key Features

### Notebook
- Dataset loading and inspection
- Missing-value analysis
- Data cleaning and type conversion
- Descriptive statistics
- Country-level listing analysis
- Price distribution
- Rating distribution
- Guest-capacity analysis
- Correlation analysis
- Country-level price comparison
- Findings, limitations, and future work

### Dashboard
- Country filter
- Guest-capacity filter
- Price-range filter
- Rated/New listing filter
- KPI cards
- Top-country chart
- Price distribution chart
- Median price by guest capacity
- Country summary table
- Filtered listing explorer
- CSV download for filtered data

## Technologies Used

- **Python**
- **Pandas** — data manipulation
- **NumPy** — numerical operations
- **Matplotlib** — visualizations
- **Jupyter Notebook** — analysis and documentation
- **Streamlit** — interactive dashboard
- **Git/GitHub** — version control and project hosting

## Project Structure

```text
Airbnb-Data-Analysis-and-Visualization/
│
├── airbnb.csv
├── Airbnb_Analysis.ipynb
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── outputs/
    ├── top_countries.png
    ├── price_distribution.png
    ├── ratings.png
    └── price_by_guests.png
```

## Dataset

The project uses the supplied `airbnb.csv` file.

The original dataset contains **12,805 rows and 23 columns**. Important fields include:

- `id`
- `name`
- `rating`
- `reviews`
- `host_name`
- `host_id`
- `address`
- `features`
- `amenities`
- `safety_rules`
- `hourse_rules`
- `price`
- `country`
- `bathrooms`
- `beds`
- `guests`
- `toiles`
- `bedrooms`
- `studios`
- `checkin`
- `checkout`

## Data Cleaning

The notebook and dashboard apply the following cleaning steps:

1. Remove the exported `Unnamed: 0` index column.
2. Convert `rating` to numeric. The value `New` becomes missing (`NaN`) for numerical analysis.
3. Convert `reviews` to numeric and use 0 where conversion results in missing values.
4. Convert property and price fields to numeric.
5. Strip unnecessary whitespace from country names.
6. Replace missing host names with `Unknown`.
7. Create `rating_status` with two categories:
   - `Rated`
   - `New`

### Missing values

The original dataset contains missing values mainly in:

- `checkout`
- `checkin`
- `host_name`

The analysis does not require check-in/check-out values, so those fields are retained for exploration but are not used as core numerical features.

## System Workflow / Architecture

```text
                +----------------------+
                |     airbnb.csv       |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Data Loading       |
                |     Pandas           |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Data Cleaning        |
                | Types / Missing Data |
                | Feature Preparation  |
                +----------+-----------+
                           |
                           v
              +------------+-------------+
              |                          |
              v                          v
    +-------------------+       +-------------------+
    | Jupyter Notebook  |       | Streamlit App     |
    | EDA & Statistics  |       | Interactive UI    |
    +---------+---------+       +---------+---------+
              |                           |
              v                           v
    +-------------------+       +-------------------+
    | Charts & Findings |       | Filters / KPIs    |
    +---------+---------+       | Charts / Tables   |
              |                 +---------+---------+
              v                           |
       +-------------+                     v
       | Final       |             +---------------+
       | Insights    |             | CSV Download  |
       +-------------+             +---------------+
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Airbnb-Data-Analysis-and-Visualization
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL after creating the repository.

### 2. Create a virtual environment (recommended)

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
Airbnb_Analysis.ipynb
```

Run all cells from top to bottom.

### 5. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The terminal will provide a local address, normally:

```text
http://localhost:8501
```

Open that address in your browser.

## Dashboard Usage

1. Start the Streamlit application.
2. Use the sidebar to select one or more countries.
3. Adjust the guest-capacity range.
4. Adjust the price range.
5. Select `All`, `Rated`, or `New`.
6. Review the KPI cards.
7. Explore charts in the **Overview** tab.
8. Use **Market Analysis** for country and capacity comparisons.
9. Use **Data Explorer** to inspect filtered listings.
10. Click **Download filtered CSV** when you need the filtered data.

## Screenshots

Place your final dashboard screenshots in the `screenshots/` folder and update this section after running the application.

Recommended screenshots:

1. Dashboard overview with KPI cards.
2. Country analysis.
3. Market analysis table.
4. Data Explorer with filters applied.

Example Markdown for GitHub:

```markdown
![Dashboard Overview](screenshots/dashboard_overview.png)
![Market Analysis](screenshots/market_analysis.png)
```

## Analysis Results

The supplied dataset contains:

- **12,805 listings**
- A large number of countries/markets
- **8,567 listings with numeric ratings**
- **4,238 listings marked as `New`**
- Mean price of approximately **17,697.80 dataset units**
- Median price of approximately **8,175 dataset units**
- Average rating among rated listings of approximately **4.86**

The difference between mean and median price indicates a strongly right-skewed price distribution, with some very expensive listings influencing the average.

## Key Findings

### 1. Price distribution is highly skewed
The average price is considerably higher than the median price. This means a relatively small number of expensive listings can pull the average upward.

**Recommendation:** Use median price when describing the typical listing and use percentile-based analysis when comparing markets.

### 2. Many listings are new
A significant share of records has `rating = New` rather than a numeric rating.

**Recommendation:** Do not treat `New` as a low rating. Analyze rated listings separately.

### 3. Listing volume varies greatly by country
A small group of countries accounts for a large portion of the available listings, while many countries have only a small number of records.

**Recommendation:** Market comparisons should include both listing count and price statistics rather than using listing count alone.

### 4. Property capacity is useful for price comparison
Guest capacity, beds, bedrooms, and bathrooms provide meaningful dimensions for comparing listing prices.

**Recommendation:** Hosts can compare their property with listings of similar capacity instead of comparing against the entire dataset.

### 5. Currency is a limitation
No currency field is supplied.

**Recommendation:** Before making real financial decisions, the source currency should be identified or standardized.

## Testing and Results

The project was checked using the following tests:

| Test | Expected Result | Status |
|---|---|---|
| CSV loads successfully | Dataset loads without error | Passed |
| Dataset dimensions | 12,805 rows | Passed |
| Numeric conversion | Price/property fields become numeric | Passed |
| Rating conversion | `New` handled as missing numeric rating | Passed |
| Country cleaning | Extra whitespace removed | Passed |
| Dashboard starts | Streamlit app launches | Passed |
| Country filter | Results update | Passed |
| Guest filter | Results update | Passed |
| Price filter | Results update | Passed |
| Rating filter | Rated/New filtering works | Passed |
| CSV download | Filtered dataset downloads | Passed |

## Challenges

### Challenge 1: Rating values
The rating column contains both numeric ratings and the text value `New`.

**Solution:** Convert numeric ratings with `pd.to_numeric(..., errors="coerce")` and analyze `New` listings separately.

### Challenge 2: Price outliers
Some price values are extremely large compared with the majority of observations.

**Solution:** The visualization uses the 99th percentile for a readable distribution while retaining the original data for analysis.

### Challenge 3: Missing currency
The dataset does not identify the currency of prices.

**Solution:** Prices are explicitly labeled as dataset units.

### Challenge 4: Missing values
Some check-in/check-out and host information is missing.

**Solution:** Missing host names are replaced with `Unknown`; check-in/check-out fields are retained but not required for the main numerical analysis.

## Future Improvements

- Deploy the dashboard online.
- Add interactive geographic maps.
- Extract city and region from the address field.
- Add machine-learning price prediction.
- Add feature importance analysis.
- Add review sentiment analysis if review text is available.
- Add historical/time-series analysis with multiple snapshots.
- Add currency normalization if currency information becomes available.
- Add advanced filters for bedrooms, bathrooms, beds, and amenities.
- Add downloadable PDF business reports.

## Conclusion

This project demonstrates a complete beginner-to-intermediate data science workflow: raw data ingestion, cleaning, exploratory analysis, visualization, dashboard development, testing, and business interpretation.

The combination of a documented Jupyter Notebook and an interactive Streamlit dashboard makes the analysis reproducible and easy to demonstrate.

## Video Demonstration Requirement

If a live URL is not available, record a short **2–4 minute screen demonstration** showing:

1. Project/GitHub repository.
2. Running the Streamlit dashboard.
3. KPI cards.
4. Country filtering.
5. Price/guest filtering.
6. Market analysis.
7. Data Explorer.
8. CSV download.
9. Jupyter Notebook and key charts.

Save the video as:

```text
Airbnb_Project_Demo.mp4
```

Upload it to Google Drive, YouTube (Unlisted), or another permitted platform and add the link here:

```text
Demo Video: ADD_YOUR_VIDEO_LINK_HERE
```

## GitHub Repository

After creating your GitHub repository, replace this placeholder:

```text
Repository: YOUR_GITHUB_REPOSITORY_URL
```

## References

- Python Documentation
- Pandas Documentation
- NumPy Documentation
- Matplotlib Documentation
- Jupyter Documentation
- Streamlit Documentation
- The supplied Airbnb CSV dataset

## Author

**Azan Haroon**

Data Science Student

Project: Airbnb Data Analysis and Visualization
