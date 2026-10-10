
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Conveyor Monitor",
    page_icon="⚙️",
    layout="wide"
)

# Custom design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eef5ff, #f8fbff);
}
.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #153e75;
}
.subtitle {
    color: #536780;
    font-size: 16px;
}
div[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #d9e6f5;
    box-shadow: 0 4px 12px #163e7510;
}
div[data-testid="stMetricLabel"] {
    color: #52657e;
}
div[data-testid="stMetricValue"] {
    color: #174a85;
}
section[data-testid="stSidebar"] {
    background: #e5efff;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="main-title">⚙️ Smart Conveyor Monitor</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Predictive Maintenance Dashboard | '
    'Monitor controller health and sensor readings</div>',
    unsafe_allow_html=True
)

st.divider()

# Sidebar controls
st.sidebar.title("🎛️ Sensor Controls")
st.sidebar.caption("Change values to test the dashboard.")

temperature = st.sidebar.slider(
    "🌡️ Temperature (°C)", 20, 100, 40
)
current = st.sidebar.slider(
    "⚡ Current (A)", 0.0, 10.0, 2.0, 0.1
)
voltage_ripple = st.sidebar.slider(
    "🔌 Voltage Ripple (V)", 0.0, 5.0, 0.5, 0.1
)

# Status logic
if temperature >= 75 or current >= 7 or voltage_ripple >= 2.5:
    status = "WARNING"
    message = "Abnormal readings detected. Inspect the controller."
    st.error("🔴 WARNING — " + message)

elif temperature >= 60 or current >= 5 or voltage_ripple >= 1.5:
    status = "CAUTION"
    message = "Readings are elevated. A maintenance inspection is recommended."
    st.warning("🟡 CAUTION — " + message)

else:
    status = "NORMAL"
    message = "All readings are within the demo limits."
    st.success("🟢 NORMAL — " + message)

# Metric cards
st.subheader("📊 Live Monitoring")

c1, c2, c3 = st.columns(3)

c1.metric(
    "🌡️ Temperature",
    f"{temperature} °C",
    help="Simulated controller temperature"
)
c2.metric(
    "⚡ Current",
    f"{current:.1f} A",
    help="Simulated electrical current"
)
c3.metric(
    "🔌 Voltage Ripple",
    f"{voltage_ripple:.1f} V",
    help="Simulated voltage ripple"
)

# Status panel
st.subheader("🩺 Controller Health")

if status == "WARNING":
    st.error(f"Status: {status}")
elif status == "CAUTION":
    st.warning(f"Status: {status}")
else:
    st.success(f"Status: {status}")

st.info(f"💡 Recommendation: {message}")

# Chart section
st.subheader("📈 Sensor Readings Analysis")

chart_data = pd.DataFrame({
    "Parameter": [
        "Temperature (°C)",
        "Current (A)",
        "Voltage Ripple (V)"
    ],
    "Reading": [
        temperature,
        current,
        voltage_ripple
    ]
})

left, right = st.columns([3, 2])

with left:
    st.markdown("#### Current Readings")
    st.bar_chart(
        chart_data.set_index("Parameter"),
        color="#2878d0"
    )

with right:
    st.markdown("#### Reading Summary")
    st.dataframe(
        chart_data,
        hide_index=True,
        use_container_width=True
    )

# Footer
st.divider()
st.caption(
    "⚙️ Smart Conveyor Predictive Maintenance | "
    "Demo prototype — simulated sensor readings only. "
    "Thresholds are illustrative and require validation "
    "before real equipment use."
)
