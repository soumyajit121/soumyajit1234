# import streamlit as st
# import pandas as pd
# import plotly.express as px
# # from google import genai

# # st.title('Hello, Streamlit!')


# # client = genai.Client(api_key="AIzaSyAgtK89IhyvnbkMtgAvTX3W1pj45ZtCOI0")

# # response = client.models.generate_content(
# #     model="gemini-2.5-flash",
# #     contents= st.text_input("Enter your prompt here:")
# # )
# # st.write(response.text)

# # st.title("My name is soumyajit")
# # df = pd.read_csv("C:\\Users\\WTS-LAP-81\\Downloads\\Final_Exam_Sanjoy_Dutta(Webskitters)\\Employee_Performance.csv")

# # x = df.groupby('EmpName').agg(total = ('EmpName','count')).reset_index()
# # st.metric("hello", x['total'].sum(),"orange")

# # st.metric("hello", x['total'].sum(),"orange")

# # st.metric("hello", x['total'].mean(),"red")

# # st.file_uploader("Upload a CSV file", type=["csv"])

# # st.dataframe(df)

# # st.snow()

# # st.sidebar.title("Sidebar Title")

# # st.multiselect("Select Employees", options=df['EmpName'].unique(), default=df['EmpName'].unique())

# # st.date_input("Select a date", value=pd.to_datetime("2023-01-01"))


# # fig = px.bar(x, x='EmpName', y='total', color='EmpName',animation_frame='total', animation_group='EmpName')

# # st.plotly_chart(fig)

# import streamlit as st
# import plotly.express as px
# import pandas as pd
# import time

# st.set_page_config(layout="wide")

# # ---------- CSS ----------
# st.markdown("""
# <style>

# .stApp {
#     background: linear-gradient(-45deg,
#         #0f172a,
#         #1e293b,
#         #2563eb,
#         #06b6d4);
#     background-size: 400% 400%;
#     animation: gradient 15s ease infinite;
# }

# @keyframes gradient {
#     0% {background-position:0% 50%;}
#     50% {background-position:100% 50%;}
#     100% {background-position:0% 50%;}
# }

# .kpi-card{
#     background:rgba(255,255,255,0.10);
#     backdrop-filter:blur(16px);
#     border:1px solid rgba(255,255,255,0.18);
#     border-radius:20px;
#     padding:20px;
#     text-align:center;
#     box-shadow:0 8px 32px rgba(0,0,0,0.25);
#     transition:.3s;
# }

# .kpi-card:hover{
#     transform:translateY(-6px);
#     box-shadow:0 12px 40px rgba(0,255,255,.25);
# }

# .kpi-title{
#     color:#dbeafe;
#     font-size:14px;
#     margin-bottom:10px;
# }

# .kpi-value{
#     color:#00ffd5;
#     font-size:38px;
#     font-weight:700;
# }

# .dashboard-title{
#     text-align:center;
#     color:white;
#     font-size:42px;
#     font-weight:bold;
#     margin-bottom:20px;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------- Title ----------
# st.markdown(
#     '<div class="dashboard-title">🚀 AI Analytics Dashboard</div>',
#     unsafe_allow_html=True
# )

# # ---------- Animated KPIs ----------
# k1, k2, k3, k4 = st.columns(4)

# p1 = k1.empty()
# p2 = k2.empty()
# p3 = k3.empty()
# p4 = k4.empty()

# for i in range(0, 101, 5):

#     p1.markdown(f"""
#     <div class='kpi-card'>
#         <div class='kpi-title'>Revenue</div>
#         <div class='kpi-value'>${i*2500:,}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     p2.markdown(f"""
#     <div class='kpi-card'>
#         <div class='kpi-title'>Customers</div>
#         <div class='kpi-value'>{i*12:,}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     p3.markdown(f"""
#     <div class='kpi-card'>
#         <div class='kpi-title'>Orders</div>
#         <div class='kpi-value'>{i*8:,}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     p4.markdown(f"""
#     <div class='kpi-card'>
#         <div class='kpi-title'>Growth</div>
#         <div class='kpi-value'>{i/4:.1f}%</div>
#     </div>
#     """, unsafe_allow_html=True)

#     time.sleep(0.02)

# st.markdown("<br>", unsafe_allow_html=True)

# # ---------- Chart ----------
# df = pd.DataFrame({
#     "Month":["Jan","Feb","Mar","Apr","May","Jun"],
#     "Revenue":[120,180,220,260,330,420]
# })

# fig = px.area(
#     df,
#     x="Month",
#     y="Revenue",
#     line_shape="spline"
# )

# fig.update_traces(
#     line=dict(width=4,color="#00ffd5")
# )

# fig.update_layout(
#     height=450,
#     paper_bgcolor="rgba(0,0,0,0)",
#     plot_bgcolor="rgba(0,0,0,0)",
#     font_color="white",
#     title="Revenue Trend",
#     title_x=0.5
# )

# st.plotly_chart(fig, use_container_width=True)

# # ---------- Progress KPIs ----------
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric("Model Accuracy", "94.8%", "+2.3%")
#     st.progress(95)

# with col2:
#     st.metric("Customer Retention", "88%", "+5%")
#     st.progress(88)

# with col3:
#     st.metric("System Health", "99.9%", "+0.2%")
#     st.progress(99)



import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")

# ---------------- DATA ---------------- #

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 45],
    "Department": ["Sales", "IT", "Finance", "HR", "Marketing"]
})

# ---------------- CSS ---------------- #

st.markdown("""
<style>

/* =========================
   ANIMATED GRADIENT BACKGROUND
========================= */

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

/* =========================
   TITLE
========================= */

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

/* =========================
   GLASS KPI CARD
========================= */

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

/* glowing border */
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

/* =========================
   TABLE STYLE
========================= */

[data-testid="stDataFrame"] {
    border-radius: 15px;
    border: 1px solid #00ff66;
    box-shadow: 0 0 15px rgba(0,255,102,0.3);
}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"] {
    background: #0a0a0a;
    border-right: 1px solid #00ff66;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.markdown('<div class="title">⚡ NEON DASHBOARD ⚡</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- SIDEBAR FILTER ---------------- #

selected = st.sidebar.multiselect(
    "Select Employees",
    options=df["Name"].unique(),
    default=df["Name"].unique()
)

filtered_df = df[df["Name"].isin(selected)]

# ---------------- KPI VALUES ---------------- #

total_people = len(filtered_df)
avg_age = round(filtered_df["Age"].mean(), 1)
max_age = filtered_df["Age"].max()
min_age = filtered_df["Age"].min()

# ---------------- KPI CARDS ---------------- #

c1, c2, c3, c4 = st.columns(4)

kpis = [
    ("TOTAL PEOPLE", total_people),
    ("AVERAGE AGE", avg_age),
    ("MAX AGE", max_age),
    ("MIN AGE", min_age)
]

for col, (title, value) in zip([c1, c2, c3, c4], kpis):
    with col:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">{title}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

# ---------------- CHART ---------------- #

fig = px.scatter(
    filtered_df,
    x="Name",
    y="Age",
    color="Department",
    text="Age", animation_frame="Department",size = "Age"
)



fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white",
    title="Employee Age Analysis",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)



df = pd.DataFrame({
    "Step": list(range(10)),
    "Value": [i**2 for i in range(10)]
})

fig = px.line(df, x="Step", y="Value")

fig.update_traces(mode="lines+markers")
fig.show()

# # ---------------- TABLE ---------------- #

# st.subheader("Employee Data")
# st.dataframe(filtered_df, use_container_width=True)

# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px

# np.random.seed(42)

# df = pd.DataFrame({
#     "frame": np.tile(np.arange(1, 51), 3),
#     "value": np.concatenate([
#         np.random.randn(50).cumsum(),
#         np.random.randn(50).cumsum(),
#         np.random.randn(50).cumsum()
#     ]),
#     "series": ["A"]*50 + ["B"]*50 + ["C"]*50
# })

# fig = px.line(
#     df,
#     x="frame",
#     y="value",
#     color="series",
#     animation_frame="frame"
# )

# # ✅ IMPORTANT: lock y-axis so movement is visible
# fig.update_layout(
#     yaxis=dict(range=[df["value"].min() - 5, df["value"].max() + 5]),
#     xaxis=dict(range=[1, 50])
# )

# st.plotly_chart(fig, use_container_width=True)

# df = pd.read_csv("C:\\Users\\WTS-LAP-81\\Downloads\\ipl_dataset_800_rows.csv")

# mitosheet.sheet(df)

