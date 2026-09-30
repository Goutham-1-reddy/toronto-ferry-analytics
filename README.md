# Toronto Island Ferry Ticket Sales & Redemption Analytics

## Dataset
- Records: 261,538
- Date range: 2015-05-01 to 2025-12-21
- Columns: _id, Timestamp, Redemption Count, Sales Count
- Missing values after timestamp validation: 0
- Duplicate rows: 0
- Negative ticket counts: 0

## Project objectives
Analyze historical ticket activity, identify peak/off-peak demand, quantify sales/redemption patterns, and provide an interactive Streamlit dashboard.

## Main KPIs
- Tickets Sold
- Tickets Redeemed
- Net Passenger Movement = Sales Count - Redemption Count
- Redemption Rate = Redemptions / Sales
- Peak demand period
- Seasonal utilization patterns

## Run locally
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Folder structure
- `app.py` — Streamlit dashboard
- `data/toronto_ferry_cleaned.csv` — cleaned and feature-engineered dataset
- `charts/` — generated EDA charts
- `research_paper.md` — research paper draft
- `executive_summary.md` — stakeholder summary
