import streamlit as st

# Page configuration
st.set_page_config(page_title="Safe Space Kenya Programs", layout="wide")

# App Title
st.markdown("""
# 🌍 Safe Space Kenya – Program Portfolio
Creating Safe, Empowered & Resilient Communities
""")

# Tabs for navigation
tabs = st.tabs([
    "Mental Health & Psychosocial Support",
    "Guidance & Counseling",
    "Youth Empowerment & Leadership",
    "Education Support & Digital Literacy",
    "Women Empowerment & Gender Equality",
    "Community Outreach & Wellness",
    "Skills Training & Economic Empowerment",
    "Advocacy & Awareness Campaigns",
    "Environment & Climate Change"
])

# Program details
with tabs[0]:
    st.markdown("""
    ## 🧠 Mental Health & Psychosocial Support
    We provide safe, confidential spaces where individuals can heal and grow. Services include:
    - Individual & group therapy sessions with licensed counselors.
    - Peer support circles, trauma healing, and stress management workshops.
    - 24/7 hotline & online counseling for immediate help.
    - Counseling for anxiety, depression, grief, and addiction recovery.
    """)

with tabs[1]:
    st.markdown("""
    ## 💬 Guidance & Counseling
    Empowering youth and women to make informed life choices:
    - Career counseling and academic mentorship.
    - Relationship & family guidance.
    - Life skills and resilience-building sessions.
    - School-based counseling and mentorship programs.
    """)

with tabs[2]:
    st.markdown("""
    ## 🌟 Youth Empowerment & Leadership
    Building confident, skilled, and purpose-driven young leaders:
    - Leadership bootcamps & ambassador programs.
    - Soft skills training (public speaking, CV writing, decision-making).
    - Volunteer, mentorship & internship opportunities.
    - Safe platforms for youth voices in policy-making.
    """)

with tabs[3]:
    st.markdown("""
    ## 📘 Education Support & Digital Literacy
    Promoting access to learning and preparing youth for the digital future:
    - School outreach & mental wellness talks.
    - Tutoring & mentorship for vulnerable learners.
    - Computer skills, coding, and safe internet use.
    - Scholarship support & academic motivation programs.
    """)

with tabs[4]:
    st.markdown("""
    ## 👩🏽‍🦱 Women Empowerment & Gender Equality
    Uplifting women through knowledge, resources, and opportunities:
    - Entrepreneurship & financial literacy training.
    - GBV awareness & survivor counseling support.
    - Women’s leadership mentorship.
    - Reproductive health & rights education.
    """)

with tabs[5]:
    st.markdown("""
    ## 🏘️ Community Outreach & Wellness
    Strengthening resilience and unity within communities:
    - Community wellness forums & motivational talks.
    - Mobile counseling clinics in rural areas.
    - Art, drama & music therapy for healing.
    - Faith-based counseling and fellowship sessions.
    """)

with tabs[6]:
    st.markdown("""
    ## 🛠️ Skills Training & Economic Empowerment
    Equipping youth and women with tools for self-reliance:
    - Vocational training (crafts, tailoring, agribusiness).
    - Eco-friendly income projects.
    - Startup incubation & entrepreneurship support.
    - Savings, microloans & investment groups.
    """)

with tabs[7]:
    st.markdown("""
    ## 📢 Advocacy & Awareness Campaigns
    Raising voices, breaking stigma, and driving change:
    - Mental health awareness campaigns.
    - Anti-GBV & rights advocacy.
    - Policy dialogue for youth voices.
    - Digital advocacy through social media platforms.
    """)

with tabs[8]:
    st.markdown("""
    ## 🌱 Environment & Climate Change
    Linking sustainability with wellness and community resilience:
    - Climate awareness campaigns in schools & communities.
    - Youth-led eco-projects (tree planting, recycling).
    - Green entrepreneurship (urban farming, clean energy).
    - Eco-mental health support to address eco-anxiety & displacement.
    """)

# Light blue background styling
st.markdown(
    """
    <style>
        body {
            background-color: #e6f2ff;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: #cce6ff;
            color: black;
            border-radius: 10px;
            margin-right: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
