import streamlit as st
import plotly.express as px
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Safe Space Kenya",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling and smooth flow
st.markdown("""
<style>
    /* Main theme */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3e4ff 100%);
    }

    /* Sticky tab bar */
    .stTabs [data-baseweb="tab-list"] {
        position: sticky;
        top: 0;
        z-index: 100;
        background-color: #e6f2ff;
        padding: 10px 0;
        gap: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #4a90e2;
        color: white;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #357abd;
        transform: translateY(-2px);
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff6f61;
        color: white;
    }

    /* Content containers */
    .program-container {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        animation: fadeIn 0.5s ease-in;
    }

    .program-title {
        color: #1a3c6e;
        border-bottom: 2px solid #4a90e2;
        padding-bottom: 10px;
        margin-bottom: 20px;
        font-size: 1.8em;
    }

    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Back to Top button */
    .back-to-top {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #ff6f61;
        color: white;
        padding: 10px 20px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .back-to-top:hover {
        background-color: #e55a50;
    }

    /* Smooth scrolling */
    html {
        scroll-behavior: smooth;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab"] {
            font-size: 10px;
            padding: 8px 10px;
        }
        .program-title {
            font-size: 1.5em;
        }
        .stApp {
            padding: 10px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header section
col1, col2 = st.columns([1, 3])
with col1:
    # Placeholder image replaced with a generic logo (use your own logo URL)
    st.image("https://via.placeholder.com/100x100?text=SSK", width=100)
with col2:
    st.markdown("""
        <h1 id='top'>Safe Space Kenya</h1>
        <p style='font-size: 1.3em; color: #2b5ea8;'>
            Creating Safe Spaces for Healing, Empowerment, and Sustainable Development
        </p>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Mission and Vision
with st.expander("Our Mission & Vision"):
    st.markdown("""
    **Our Mission:** To provide holistic support, empowerment, and advocacy for vulnerable communities in Kenya, fostering mental wellness, gender equality, economic independence, and environmental sustainability.

    **Our Vision:** A Kenya where every individual thrives in safe, supportive communities free from violence, discrimination, and poverty, with equal access to opportunities for growth and development.
    """)

# Program tabs
tabs = st.tabs([
    "🧠 Counseling & Psychosocial",
    "🌟 Youth Empowerment",
    "👩🏽‍🦱 Women Empowerment",
    "🏘️ Community Outreach",
    "🛠️ Skills Training",
    "📢 Advocacy & Awareness",
    "🌱 Environment & Health",
    "🛎️ Other Services",
    "📊 Budget Allocation"
])

# Tab 1: Counseling & Psychosocial Services
with tabs[0]:
    st.markdown('<div class="program-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Counseling & Psychosocial Services</h2>', unsafe_allow_html=True)
    st.write("Our counseling and psychosocial services provide safe, confidential support for individuals and groups dealing with trauma, mental health challenges, and personal difficulties.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Services Offered")
        st.markdown("""
        - Individual counseling sessions
        - Group therapy and support circles
        - Trauma-informed care
        - Crisis intervention
        - Mental health assessments
        - Referral services to specialized care
        - Teletherapy options for remote areas
        """)
    with col2:
        st.subheader("Impact Areas")
        st.markdown("""
        - Reduced mental health stigma in communities
        - Improved coping mechanisms for trauma survivors
        - Enhanced emotional well-being for over 2,000 clients annually
        - Decreased suicide rates in served communities
        - Strengthened family relationships through counseling
        - Better academic performance for supported youth
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 2: Youth Empowerment & Education
with tabs[1]:
    st.markdown('<div class="program-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Youth Empowerment & Education</h2>', unsafe_allow_html=True)
    st.write("We empower Kenya's youth through educational support, leadership development, and skills building to create the next generation of change-makers.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Services Offered")
        st.markdown("""
        - Scholarship programs for vulnerable students
        - After-school tutoring and academic support
        - Leadership training workshops
        - Career guidance and mentorship
        - Digital literacy programs
        - Entrepreneurship training for youth
        - School supplies and resource provision
        """)
    with col2:
        st.subheader("Impact Areas")
        st.markdown("""
        - Increased secondary school completion rates
        - Enhanced digital skills among rural youth
        - Development of youth-led community projects
        - Reduced youth unemployment through skills training
        - Improved academic performance in partner schools
        - Creation of youth support networks
        - Increased civic engagement among participants
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 3: Women Empowerment & Gender Equality
with tabs[2]:
    st.markdown('<div class="program-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Women Empowerment & Gender Equality</h2>', unsafe_allow_html=True)
    st.write("We champion gender equality and women's empowerment through education, economic initiatives, and advocacy to create a more equitable society.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Services Offered")
        st.markdown("""
        - Gender equality workshops and training
        - Women's leadership development
        - Support for survivors of gender-based violence
        - Legal aid and advocacy services
        - Women's health education
        - Economic empowerment programs
        - Networking and mentorship opportunities
        """)
    with col2:
        st.subheader("Impact Areas")
        st.markdown("""
        - Increased women's participation in community leadership
        - Reduced incidence of gender-based violence in served areas
        - Improved economic independence for women
        - Enhanced knowledge of women's rights and legal protections
        - Strengthened support systems for survivors
        - Increased girls' school retention rates
        - Policy advocacy for gender-sensitive legislation
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 4: Community Outreach & Wellness
with tabs[3]:
    st.markdown('<div class="program-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Community Outreach & Wellness</h2>', unsafe_allow_html=True)
    st.write("Our community outreach programs bring essential services, education, and support directly to underserved communities across Kenya.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Services Offered")
        st.markdown("""
        - Mobile health clinics
        - Community health education
        - Wellness workshops and seminars
        - Preventive health screenings
        - Hygiene and sanitation initiatives
        - Community dialogue forums
        - Disaster response and preparedness training
        """)
    with col2:
        st.subheader("Impact Areas")
        st.markdown("""
        - Improved health outcomes in remote areas
        - Increased knowledge of preventive healthcare
        - Enhanced community cohesion and support networks
        - Reduced prevalence of preventable diseases
        - Strengthened community response mechanisms
        - Increased access to health services for marginalized groups
        - Improved sanitation practices in served communities
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 5: Skills Training & Economic Empowerment
with tabs[4]:
    st.markdown('<div class="program-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Skills Training & Economic Empowerment</h2>', unsafe_allow_html=True)
    st.write("We provide practical skills training and economic empowerment programs to help individuals achieve financial independence and sustainable livelihoods.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Services Offered")
        st.markdown("""
        - Vocational training programs
        - Entrepreneurship development
        - Business startup support
        - Financial literacy training
        - Microfinance linkages
        - Apprenticeship opportunities
        - Market access support for products
        """)
    with col2:
        st.subheader("Impact Areas")
        st.markdown("""
        - Increased household incomes for participants
        - Creation of sustainable small businesses
        - Reduced poverty levels in target communities
        - Enhanced financial management skills
        - Job creation through new enterprises
        - Economic resilience during challenging times
        - Increased women's participation in the economy
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 6: Advocacy & Awareness Campaigns
with tabs[5]:
    st.markdown('<div class="program-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Advocacy & Awareness Campaigns</h2>', unsafe_allow_html=True)
    st.write("We drive social change through strategic advocacy and awareness campaigns on critical issues affecting vulnerable communities in Kenya.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Services Offered")
        st.markdown("""
        - Public awareness campaigns on social issues
        - Policy advocacy and reform initiatives
        - Community mobilization and engagement
        - Media campaigns and social media advocacy
        - Educational workshops on rights and entitlements
        - Coalition building with like-minded organizations
        - Research and publication on key social issues
        """)
    with col2:
        st.subheader("Impact Areas")
        st.markdown("""
        - Increased public awareness on critical social issues
        - Policy changes benefiting vulnerable groups
        - Enhanced community participation in advocacy
        - Reduced stigma around mental health and gender-based violence
        - Strengthened civil society networks
        - Improved implementation of existing protective policies
        - Amplified voices of marginalized communities
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 7: Environment, Health & Climate Action
with tabs[6]:
    st.markdown('<div class="program-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Environment, Health & Climate Action</h2>', unsafe_allow_html=True)
    st.write("We address environmental challenges and promote sustainable practices that protect community health and build resilience to climate change.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Services Offered")
        st.markdown("""
        - Environmental conservation initiatives
        - Climate change adaptation training
        - Sustainable agriculture programs
        - Tree planting and
