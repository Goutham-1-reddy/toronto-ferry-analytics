# Real-Time Ferry Ticket Sales & Redemption Analytics for Toronto Island Park

## Abstract
This project analyzes Toronto Island ferry ticket sales and redemptions using 261,538 timestamped observations covering 2015-05-01 through 2025-12-21. The objective is to identify demand patterns, compare ticket sales with redemptions, quantify net passenger movement, and provide an interactive analytics dashboard for operational stakeholders.

## 1. Introduction
Ferry operations require timely understanding of passenger demand. A centralized analytics workflow can help operations teams examine temporal demand, identify recurring peak periods, and compare ticket sales with actual redemptions.

## 2. Dataset
The dataset contains `_id`, `Timestamp`, `Redemption Count`, and `Sales Count`. The analysis covers 2015-05-01 to 2025-12-21. The source file contains 261,538 records.

## 3. Methodology
1. Parse and validate timestamps.
2. Sort records chronologically and check duplicates.
3. Check missing and negative values.
4. Engineer hour, weekday, month, year, season, and weekend/weekday features.
5. Calculate net passenger movement as Sales Count minus Redemption Count.
6. Aggregate activity at 15-minute, hourly, daily, weekly, and seasonal levels.
7. Visualize trends using time-series and categorical charts.
8. Present results through a Streamlit dashboard.

## 4. Data Quality
No missing values were found in the four source columns. No duplicate rows were found. No negative values were found in Sales Count or Redemption Count. The source timestamps span more than ten years.

## 5. Descriptive Results
Total ticket sales in the dataset: **12,972,051**.
Total ticket redemptions: **12,785,293**.
Net difference between sales and redemptions: **186,758**.
Overall redemption-to-sales ratio: **98.56%**.

The highest individual Sales Count record occurred at **2023-08-15 20:15:00**, with **7,229** sales. The highest individual Redemption Count record occurred at **2023-08-15 20:15:00**, with **7,216** redemptions.

The hour with the highest average Sales Count was **12:00**, with an average of approximately **94.52 tickets per source record**.

## 6. Interpretation
The dashboard separates demand by hour, weekday/weekend status, and season. These views allow operational stakeholders to identify recurring demand concentrations rather than relying on individual extreme observations. Sales and redemptions are analyzed separately because a ticket can be sold before the corresponding travel event.

## 7. Recommendations
- Use recurring high-demand periods to inform staffing and queue-management planning.
- Review peak and off-peak patterns separately for weekdays and weekends.
- Use seasonal demand patterns when planning operational capacity.
- Investigate extreme observations before treating them as data errors.
- Continue monitoring the difference between sales and redemptions to understand timing and potential backlog effects.

## 8. Limitations
The dataset does not identify individual ferry routes, passenger demographics, weather conditions, vessel capacity, or transaction-level customer attributes. Therefore, the analysis describes temporal demand patterns but does not establish causal relationships.

## 9. Conclusion
The project provides a reproducible analytics workflow for ferry ticket activity. The combination of data cleaning, feature engineering, KPI calculations, exploratory analysis, and an interactive Streamlit dashboard provides a practical foundation for operational planning and future real-time monitoring.
