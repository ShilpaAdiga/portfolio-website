# import streamlit as st

# # ---- PAGE CONFIG ----
# st.set_page_config(page_title="Shilpa Adiga | Portfolio", page_icon="📊", layout="wide")

# st.markdown("""
# <style>
# .project-card:hover {
#     background-color: #f0f2f6;
#     border-radius: 10px;
#     padding: 10px;
#     transition: 0.3s ease;
# }
# </style>
# """, unsafe_allow_html=True)


# # ---- HEADER BANNER ----
# st.markdown(
#     """
#     <style>
#     .title {
#         text-align: center;
#         font-size: 40px;
#         font-weight: 700;
#         color: #4CAF50;
#     }
#     .subtitle {
#         text-align: center;
#         font-size: 20px;
#         color: #555;
#     }
#     </style>
#     <div class="title">📊 Shilpa Adiga</div>
#     <div class="subtitle">Data Analyst | Python • SQL • Excel • Power BI</div>
#     """,
#     unsafe_allow_html=True
# )


# st.markdown("## 👩‍💻 About Me")
# st.markdown("""
# Hi! I'm **Shilpa Adiga**, a data enthusiast with 3+ years of experience in data analysis, web scraping, and automation.

# I enjoy working with real-world data to uncover insights and build clean, practical solutions — from Excel dashboards to SQL reports to Python-based data tools.
# """)




# # ---- PROJECTS ----
# st.markdown("---")
# st.header("📁 Projects")

# # Project 1

# with st.container():
#     st.markdown("""
#     <div style="background-color: #f9f9f9; border-radius: 10px; padding: 15px; margin-bottom: 15px;">
#     """, unsafe_allow_html=True)

#     col1, col2 = st.columns([1, 3])
#     with col1:
#         st.image("https://img.icons8.com/color/96/000000/python.png", width=80)
#     with col2:
#         st.subheader("🛒 Flipkart Laptop Scraper")
#         st.image("assets/flipkart.png", use_container_width=True)

#         st.write(
#             "Scraped laptop listings under ₹60,000 from Flipkart using Python and BeautifulSoup. "
#             "Cleaned and exported data to Excel, handled 429 errors, and fetched full product details from product pages."
#         )
#         st.markdown("**Tools:** Python, Requests, BeautifulSoup, Pandas, Excel")
#         st.markdown("[🔗 View Project](https://github.com/ShilpaAdiga/flipkart-laptop-scraper)")
#     st.markdown('</div>', unsafe_allow_html=True)

# # Project 2

# with st.container():
#     st.markdown("""
#     <div style="background-color: #f9f9f9; border-radius: 10px; padding: 15px; margin-bottom: 15px;">
#     """, unsafe_allow_html=True)

#     col1, col2 = st.columns([1, 3])
#     with col1:
#         st.image("https://upload.wikimedia.org/wikipedia/commons/6/69/Airbnb_Logo_B%C3%A9lo.svg", width=80)
#     with col2:
#         st.subheader("🏠 Paris Airbnb EDA")
#         st.image("assets/airbnb.png", use_container_width=True)

#         st.write(
#             "Performed EDA on 86K+ Airbnb listings in Paris. Explored pricing trends, room types, host activity, and availability using Python."
#         )
#         st.markdown("**Tools:** Python, Pandas, Matplotlib, Seaborn")
#         st.markdown("[🔗 View Project](https://github.com/ShilpaAdiga/paris-airbnb-analysis)")
#     st.markdown('</div>', unsafe_allow_html=True)

# # Project 3

# with st.container():
#     st.markdown("""
#     <div style="background-color: #f9f9f9; border-radius: 10px; padding: 15px; margin-bottom: 15px;">
#     """, unsafe_allow_html=True)

#     col1, col2 = st.columns([1, 3])
#     with col1:
#         st.image("https://img.icons8.com/color/96/sql.png", width=80)
#     with col2:
#         st.subheader("🧮 Northwind SQL Data Analysis")
#         st.image("assets/northwind.png", use_container_width=True)

#         st.write(
#             "Analyzed sales, customer behavior, and employee performance using SQL queries on the Northwind database. "
#             "Visualized insights using Python libraries."
#         )
#         st.markdown("**Tools:** SQL, SQLite, Pandas, Matplotlib, Seaborn")
#         st.markdown("[🔗 View Project](https://github.com/ShilpaAdiga/northwind-sql-analysis)")
#     st.markdown('</div>', unsafe_allow_html=True)

# # Project 4

# with st.container():
#     st.markdown(
#     """
#     <div style='background-color: #f5f5f5; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
#     """, unsafe_allow_html=True
# )
#     col1, col2 = st.columns([1, 3])
#     with col1:
#         st.image("https://img.icons8.com/color/96/combo-chart.png", width=80)
#     with col2:
#         st.subheader("📊 Global Superstore Dashboard")
#         st.image("assets/superstore.png", use_container_width=True)
#         st.write(
#             "Built an interactive dashboard using Excel and Power BI on 5K+ sales records. "
#             "Analyzed sales by category, region, segment, and returns."
#         )
#         st.markdown("**Tools:** Excel, Power BI")
#         st.markdown("[🔗 View Project](https://github.com/ShilpaAdiga/global-superstore-dashboard)")
#     st.markdown("</div>", unsafe_allow_html=True)


# # ---- SKILLS ----
# st.markdown("---")
# st.header("🛠️ Skills")

# st.markdown("""
# - 💻 **Languages & Tools**: Python, SQL, Excel, Power BI  
# - 📚 **Libraries**: pandas, numpy, matplotlib, seaborn, BeautifulSoup, requests  
# - 🧹 **Techniques**: Web Scraping, Data Cleaning, EDA, Dashboarding, Reporting  
# - 🔧 **Other**: Streamlit, Jupyter Notebook, Git, GitHub
# """)



# # ---- CONTACT ----
# st.markdown("---")
# st.header("📬 Let's Connect")

# st.markdown("""
# 📧 [**shilpa.yourmail@example.com**](mailto:shilpa.yourmail@example.com)  
# 🔗 [**LinkedIn: linkedin.com/in/shilpaadiga**](https://www.linkedin.com/in/shilpaadiga)
# """)


# st.markdown("---")
# st.markdown("<center>© 2025 Shilpa Adiga</center>", unsafe_allow_html=True)


import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Shilpa Adiga | Portfolio", page_icon="📊", layout="wide")

# ---- GLOBAL STYLES ----
st.markdown("""
<style>
    .project-card {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    .project-image {
        border-radius: 8px;
    }

    .footer {
        text-align: center;
        font-size: 14px;
        color: gray;
        margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("<h1 style='text-align: center;'>📊 Shilpa Adiga</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Data Analyst | Python • SQL • Excel • Power BI</h4>", unsafe_allow_html=True)

# ---- ABOUT ----
st.markdown("## 👩‍💻 About Me")
st.write("""
Hi! I'm **Shilpa Adiga**, a data enthusiast with 3+ years of experience in data analysis, web scraping, and automation.

I enjoy working with real-world data to uncover insights and build clean, practical solutions — from Excel dashboards to SQL reports to Python-based data tools.
""")

# ---- PROJECTS ----
st.markdown("---")
st.header("📁 Projects")

# Flipkart Project
st.markdown('<div class="project-card">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://img.icons8.com/color/96/000000/python.png", width=80)
with col2:
    st.subheader("🛒 Flipkart Laptop Scraper")
    st.image("assets/flipkart.png", use_container_width=True, caption="Sample Output")
    st.write("Scraped laptop listings under ₹60,000 from Flipkart using Python and BeautifulSoup. Cleaned and exported data to Excel, handled 429 errors, and fetched full product details from product pages.")
    st.markdown("**Tools:** Python, Requests, BeautifulSoup, Pandas, Excel")
    st.markdown("[🔗 View Project](https://github.com/ShilpaAdiga/flipkart-laptop-scraper)")
st.markdown('</div>', unsafe_allow_html=True)

# Airbnb EDA
st.markdown('<div class="project-card">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/69/Airbnb_Logo_B%C3%A9lo.svg", width=80)
with col2:
    st.subheader("🏠 Paris Airbnb EDA")
    st.image("assets/airbnb.png", use_container_width=True, caption="Price Distribution by Room Type")
    st.write("Performed exploratory analysis on 86K+ Airbnb listings in Paris. Explored pricing trends, host activity, availability, and room type distribution.")
    st.markdown("**Tools:** Python, Pandas, Matplotlib, Seaborn")
    st.markdown("[🔗 View Project](https://github.com/ShilpaAdiga/paris-airbnb-analysis)")
st.markdown('</div>', unsafe_allow_html=True)

# Northwind SQL Project
st.markdown('<div class="project-card">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://img.icons8.com/color/96/sql.png", width=80)
with col2:
    st.subheader("🧮 Northwind SQL Data Analysis")
    st.image("assets/northwind.png", use_container_width=True, caption="Employee Sales vs Customer Behavior")
    st.write("Analyzed sales, customer behavior, and employee performance using SQL queries on the Northwind database. Visualized insights using Python libraries.")
    st.markdown("**Tools:** SQL, SQLite, Pandas, Matplotlib, Seaborn")
    st.markdown("[🔗 View Project](https://github.com/ShilpaAdiga/northwind-sql-analysis)")
st.markdown('</div>', unsafe_allow_html=True)

# Superstore Dashboard
st.markdown('<div class="project-card">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://img.icons8.com/color/96/combo-chart.png", width=80)
with col2:
    st.subheader("📊 Global Superstore Dashboard")
    st.image("assets/superstore.png", use_container_width=True, caption="Sales by Category Dashboard")
    st.write("Built an interactive dashboard using Excel and Power BI on 5K+ sales records. Analyzed sales by category, region, segment, and returns.")
    st.markdown("**Tools:** Excel, Power BI")
    st.markdown("[🔗 View Project](https://github.com/ShilpaAdiga/global-superstore-dashboard)")
st.markdown('</div>', unsafe_allow_html=True)

# ---- SKILLS ----
st.markdown("---")
st.header("🛠️ Skills")
st.markdown("""
- 💻 **Languages & Tools**: Python, SQL, Excel, Power BI  
- 📚 **Libraries**: pandas, numpy, matplotlib, seaborn, BeautifulSoup, requests  
- 🧹 **Techniques**: Web Scraping, Data Cleaning, EDA, Dashboarding, Reporting  
- 🔧 **Other**: Streamlit, Jupyter Notebook, Git, GitHub
""")

# ---- CONTACT ----
st.markdown("---")
st.header("📬 Let's Connect")
st.markdown("""
📧 [**shilpaadiga09@gmail.com **](mailto:shilpaadiga09@gmail.com )  
🔗 [**LinkedIn: linkedin.com/in/shilpaadiga**](https://www.linkedin.com/in/shilpa-adiga-569838169/)
""")

# ---- FOOTER ----
st.markdown("---")
st.markdown("<div class='footer'>© 2025 Shilpa Adiga</div>", unsafe_allow_html=True)
