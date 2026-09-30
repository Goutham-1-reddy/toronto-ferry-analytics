import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Toronto Island Ferry Analytics", page_icon="⛴️", layout="wide")
st.title("⛴️ Toronto Island Ferry Ticket Analytics")
st.caption("Historical and near-real-time style analytics for ticket sales and redemptions")

@st.cache_data
def load_data():
    d = pd.read_csv("data/toronto_ferry_cleaned.csv", parse_dates=["Timestamp"])
    return d.sort_values("Timestamp")

df = load_data()
min_date, max_date = df["Timestamp"].min().date(), df["Timestamp"].max().date()

with st.sidebar:
    st.header("Filters")
    dates = st.date_input("Date range", [min_date, max_date], min_value=min_date, max_value=max_date)
    if isinstance(dates, (list, tuple)) and len(dates) == 2:
        start, end = pd.Timestamp(dates[0]), pd.Timestamp(dates[1]) + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)
        dff = df[(df["Timestamp"] >= start) & (df["Timestamp"] <= end)].copy()
    else:
        dff = df.copy()
    seasons = st.multiselect("Season", sorted(dff["Season"].dropna().unique()), default=sorted(dff["Season"].dropna().unique()))
    if seasons:
        dff = dff[dff["Season"].isin(seasons)]
    days = st.multiselect("Day type", ["Weekday","Weekend"], default=["Weekday","Weekend"])
    dff = dff[dff["Weekend"].isin(days)]

if dff.empty:
    st.warning("No records match the selected filters.")
    st.stop()

total_sales = int(dff["Sales Count"].sum())
total_red = int(dff["Redemption Count"].sum())
net = total_sales - total_red
rate = total_red / total_sales * 100 if total_sales else 0
peak = dff.loc[dff["Sales Count"].idxmax()]

c1,c2,c3,c4 = st.columns(4)
c1.metric("Tickets Sold", f"{total_sales:,}")
c2.metric("Tickets Redeemed", f"{total_red:,}")
c3.metric("Net Movement", f"{net:,}")
c4.metric("Redemption Rate", f"{rate:.1f}%")

st.subheader("Ticket Activity Over Time")
freq = st.selectbox("Aggregation", ["15 minutes","1 hour","1 day"], index=1)
rule = {"15 minutes":"15min","1 hour":"1h","1 day":"1D"}[freq]
ts = dff.set_index("Timestamp")[["Sales Count","Redemption Count"]].resample(rule).sum().reset_index()
fig = px.line(ts, x="Timestamp", y=["Sales Count","Redemption Count"],
              labels={"value":"Tickets","variable":"Metric"}, markers=False)
st.plotly_chart(fig, use_container_width=True)

left,right = st.columns(2)
with left:
    st.subheader("Average Demand by Hour")
    h = dff.groupby("Hour", as_index=False)["Sales Count"].mean()
    st.plotly_chart(px.bar(h, x="Hour", y="Sales Count", labels={"Sales Count":"Avg. sales"}), use_container_width=True)
with right:
    st.subheader("Weekday vs Weekend")
    w = dff.groupby("Weekend", as_index=False)[["Sales Count","Redemption Count"]].mean()
    st.plotly_chart(px.bar(w, x="Weekend", y=["Sales Count","Redemption Count"], barmode="group"), use_container_width=True)

left,right = st.columns(2)
with left:
    st.subheader("Seasonal Demand")
    s = dff.groupby("Season", as_index=False)["Sales Count"].mean()
    st.plotly_chart(px.bar(s, x="Season", y="Sales Count", category_orders={"Season":["Winter","Spring","Summer","Fall"]}), use_container_width=True)
with right:
    st.subheader("Net Passenger Movement")
    net_ts = dff.set_index("Timestamp")["Net Passenger Movement"].resample(rule).sum().reset_index()
    st.plotly_chart(px.area(net_ts, x="Timestamp", y="Net Passenger Movement"), use_container_width=True)

st.subheader("Peak Activity Record")
st.dataframe(pd.DataFrame([{
    "Timestamp": peak["Timestamp"],
    "Sales Count": int(peak["Sales Count"]),
    "Redemption Count": int(peak["Redemption Count"]),
    "Net Movement": int(peak["Net Passenger Movement"])
}]), use_container_width=True)

st.subheader("Operational Notes")
st.markdown("""
- Use peak-hour demand to inform staffing and terminal queue management.
- Compare sales and redemptions to understand timing differences between purchase and travel.
- Use seasonal and weekday/weekend patterns when planning capacity.
- Treat extreme observations as candidates for investigation rather than automatically deleting them.
""")
