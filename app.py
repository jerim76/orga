import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Safe Space Kenya Programs",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
        /* Global styles */
        .main {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3e4ff 100%);
            padding: 20px;
            border-radius: 15px;
        }
        h1, h2, h3 {
            font-family: 'Arial', sans-serif;
            color: #1a3c6e;
        }
        h1 {
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        h2 {
            font-size: 1.8em;
            color: #2b5ea8;
        }
        p, li {
            font-size: 1.1em;
            color: #333;
            line-height: 1.6;
        }

        /* Tab styling */
        .stTabs [data-baseweb="tab"] {
            background-color: #4a90e2;
            color: white;
            border-radius: 10px 10px 0 0;
            padding: 10px 20px;
            margin-right: 5px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background-color: #357abd;
        }
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background-color: #ff6f61;
            color: white;
        }

        /* Tab content container */
        .stTabs [data-baseweb="tab-panel"] {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 10px;
        }

        /* Divider */
        hr {
            border: 0;
            height: 2px;
            background: linear-gradient(to right, #4a90e2, #ff6f61);
            margin: 20px 0;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            h1 {
                font-size: 2em;
            }
            h2 {
                font-size: 1.5em;
            }
            .stTabs [data-baseweb="tab"] {
                padding: 8px 12px;
                font-size: 0.9em;
            }
        }
    </style>
""", unsafe_allow_html=True)

# App Title and Header
st.markdown("""
    <h1>🌍 Safe Space Kenya – Program Portfolio</h1>
    <p style='text-align: center; font-size: 1.3em; color: #2b5ea8;'>
        Creating Safe, Empowered & Resilient Communities
    </p>
    <hr>
""", unsafe_allow_html=True)

# Tabs for navigation
tabs = st.tabs([
    "🧠 Mental Health",
    "💬 Counseling",
    "🌟 Youth Leadership",
    "📘 Education & Digital",
    "👩🏽‍🦱 Women Empowerment",
    "🏘️ Community Wellness",
    "🛠️ Skills Training",
    "📢 Advocacy",
    "🌱 Environment"
])

# Program details with enhanced formatting
with tabs[0]:
    st.markdown("""
    ### 🧠 Mental Health & Psychosocial Support
    Providing safe, confidential spaces for healing and growth.
    - **Individual & Group Therapy**: Sessions with licensed counselors.
    - **Peer Support Circles**: Trauma healing and stress management workshops.
    - **24/7 Hotline & Online Counseling**: Immediate support for those in need.
    - **Specialized Counseling**: Addressing anxiety, depression, grief, and addiction recovery.
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

with tabs[1]:
    st.markdown("""
    ### 💬 Guidance & Counseling
    Empowering youth and women to make informed choices.
    - **Career Counseling**: Academic mentorship and career guidance.
    - **Relationship & Family Guidance**: Support for personal relationships.
    - **Life Skills Training**: Resilience-building and decision-making sessions.
    - **School-Based Programs**: Counseling and mentorship for students.
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

with tabs[2]:
    st.markdown("""
    ### 🌟 Youth Empowerment & Leadership
    Building confident, purpose-driven young leaders.
    - **Leadership Bootcamps**: Intensive training and ambassador programs.
    - **Soft Skills Training**: Public speaking, CV writing, and decision-making.
    - **Volunteer & Internship Opportunities**: Hands-on experience for growth.
    - **Youth Advocacy**: Platforms for youth voices in policy-making.
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

with tabs[3]:
    st.markdown("""
    ### 📘 Education Support & Digital Literacy
    Preparing youth for a digital future with accessible education.
    - **School Outreach**: Mental wellness talks and tutoring programs.
    - **Digital Skills**: Computer skills, coding, and safe internet use.
    - **Scholarship Support**: Financial aid and academic motivation programs.
    - **Mentorship**: Support for vulnerable learners.
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

with tabs[4]:
    st.markdown("""
    ### 👩🏽‍🦱 Women Empowerment & Gender Equality
    Uplifting women through knowledge and opportunities.
    - **Entrepreneurship Training**: Financial literacy and business skills.
    - **GBV Support**: Awareness and counseling for survivors.
    - **Leadership Mentorship**: Empowering women to lead.
    - **Reproductive Health**: Education on rights and health.
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

with tabs[5]:
    st.markdown("""
    ### 🏘️ Community Outreach & Wellness
    Strengthening community resilience and unity.
    - **Wellness Forums**: Motivational talks and community engagement.
    - **Mobile Clinics**: Counseling services in rural areas.
    - **Creative Therapy**: Art, drama, and music for healing.
    - **Faith-Based Support**: Counseling and fellowship sessions.
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

with tabs[6]:
    st.markdown("""
    ### 🛠️ Skills Training & Economic Empowerment
    Equipping individuals with tools for self-reliance.
    - **Vocational Training**: Crafts, tailoring, and agribusiness.
    - **Eco-Friendly Projects**: Sustainable income opportunities.
    - **Startup Incubation**: Support for entrepreneurship.
    - **Financial Support**: Savings groups and microloans.
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

with tabs[7]:
    st.markdown("""
    ### 📢 Advocacy & Awareness Campaigns
    Raising voices and driving change.
    - **Mental Health Campaigns**: Breaking stigma around mental health.
    - **Anti-GBV Advocacy**: Promoting rights and safety.
    - **Policy Dialogue**: Amplifying youth voices.
    - **Digital Advocacy**: Engaging communities via social media.
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

with tabs[8]:
    st.markdown("""
    ### 🌱 Environment & Climate Change
    Linking sustainability with community resilience.
    - **Climate Awareness**: Campaigns in schools and communities.
    - **Youth-Led Eco-Projects**: Tree planting and recycling initiatives.
    - **Green Entrepreneurship**: Urban farming and clean energy ventures.
    - **Eco-Mental Health**: Support for eco-anxiety and displacement.
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; padding: 20px; color: #1a3c6e;'>
        <p>© 2025 Safe Space Kenya | Empowering Communities for a Brighter Future</p>
    </div>
""", unsafe_allow_html=True)
