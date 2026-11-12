
import streamlit as st
import pandas as pd
import plotly.express as px


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Neon Dashboard",
    page_icon="⚡",
    layout="wide"
)


# ==================================================
# EMPLOYEE DATA
# ==================================================

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 45],
    "Department": [
        "Sales",
        "IT",
        "Finance",
        "HR",
        "Marketing"
    ]
})


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

/* BACKGROUND */

.stApp {
    background: linear-gradient(
        -45deg,
        #000000,
        #112E81,
        #000000,
        #4647AE
    );

    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
    color: white;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}


/* TITLE */

.title {
    text-align: center;
    font-size: 50px;
    font-weight: 900;
    color: #00ff66;

    text-shadow:
        0 0 10px #00ff66,
        0 0 25px #00ff66,
        0 0 40px #00ff66;
}


/* KPI CARDS */

.kpi-card {
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(15px);

    border-radius: 20px;
    padding: 25px;
    text-align: center;

    border: 1px solid rgba(255,255,255,0.15);

    transition: 0.3s;
    position: relative;
    overflow: hidden;
}

.kpi-card::before {
    content: "";
    position: absolute;
    inset: 0;
    padding: 2px;

    background: linear-gradient(
        90deg,
        #112E81,
        #4647AE,
        #112E81
    );

    background-size: 300% 300%;
    animation: borderMove 4s linear infinite;

    -webkit-mask:
        linear-gradient(#fff 0 0) content-box,
        linear-gradient(#fff 0 0);

    -webkit-mask-composite: xor;
}

@keyframes borderMove {
    0% { background-position: 0% 50%; }
    100% { background-position: 300% 50%; }
}

.kpi-card:hover {
    transform: translateY(-6px);

    box-shadow:
        0 0 20px #00ff66,
        0 0 40px #ffee00;
}

.kpi-title {
    color: #ffee00;
    font-size: 14px;
    letter-spacing: 1px;
}

.kpi-value {
    color: #00ff66;
    font-size: 40px;
    font-weight: bold;

    text-shadow:
        0 0 10px #00ff66;
}


/* TABLE */

[data-testid="stDataFrame"] {
    border-radius: 15px;
    border: 1px solid #00ff66;

    box-shadow:
        0 0 15px rgba(0,255,102,0.3);
}


/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #0a0a0a;
    border-right: 1px solid #00ff66;
}


/* HEADINGS */

h2, h3 {
    color: #00ff66 !important;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# DASHBOARD TITLE
# ==================================================

st.markdown(
    '<div class="title">⚡ NEON DASHBOARD ⚡</div>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)


# ==================================================
# SIDEBAR FILTERS
# ==================================================

st.sidebar.title("⚙️ Dashboard Filters")

selected = st.sidebar.multiselect(
    "Select Employees",
    options=df["Name"].unique(),
    default=df["Name"].unique()
)

filtered_df = df[
    df["Name"].isin(selected)
]


# ==================================================
# KPI CALCULATIONS
# ==================================================

total_people = len(filtered_df)

if not filtered_df.empty:

    avg_age = round(filtered_df["Age"].mean(), 1)
    max_age = filtered_df["Age"].max()
    min_age = filtered_df["Age"].min()

else:

    avg_age = 0
    max_age = 0
    min_age = 0


# ==================================================
# KPI CARDS
# ==================================================

st.subheader("📊 Employee Overview")

c1, c2, c3, c4 = st.columns(4)

kpis = [
    ("TOTAL PEOPLE", total_people),
    ("AVERAGE AGE", avg_age),
    ("MAX AGE", max_age),
    ("MIN AGE", min_age)
]

for col, (title, value) in zip(
    [c1, c2, c3, c4],
    kpis
):

    with col:

        st.markdown(f"""
        <div class="kpi-card">

            <div class="kpi-title">
                {title}
            </div>

            <div class="kpi-value">
                {value}
            </div>

        </div>
        """, unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# ==================================================
# EMPLOYEE SCATTER CHART
# ==================================================

st.subheader("👥 Employee Age Analysis")

if not filtered_df.empty:

    fig = px.scatter(
        filtered_df,
        x="Name",
        y="Age",
        color="Department",
        text="Age",
        size="Age",
        animation_frame="Department",
        title="Employee Age Analysis"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        title_x=0.5,
        xaxis_title="Employee Name",
        yaxis_title="Age"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info("Please select at least one employee.")


# ==================================================
# LINE CHART DATA
# ==================================================

st.subheader("📈 Step vs Value Analysis")

line_df = pd.DataFrame({

    "Step": list(range(10)),

    "Value": [
        i**2 for i in range(10)
    ]

})


# ==================================================
# LINE CHART
# ==================================================

line_fig = px.line(
    line_df,
    x="Step",
    y="Value",
    title="Step vs Value Analysis",
    markers=True
)

line_fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white",
    title_x=0.5,
    xaxis_title="Step",
    yaxis_title="Value"
)

line_fig.update_traces(
    mode="lines+markers",
    line=dict(width=3)
)

st.plotly_chart(
    line_fig,
    use_container_width=True
)


# ==================================================
# EMPLOYEE DATA TABLE
# ==================================================

st.markdown("---")

st.subheader("📋 Employee Details")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)


# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<div style="
    text-align:center;
    color:#00ff66;
    padding:20px;
    font-size:14px;
">
    ⚡ NEON DASHBOARD | Built with Python & Streamlit ⚡
</div>
""", unsafe_allow_html=True)
