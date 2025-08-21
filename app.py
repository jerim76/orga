import streamlit as st
import plotly.express as px
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Safe Space Kenya",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Main theme color */
    .stApp {
        background-color: #e6f2ff;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #e6f2ff;
        border-radius: 10px 10px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: bold;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #b3d9ff;
    }
    
    /* Content containers */
    .program-container {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    .program-title {
        color: #0066cc;
        border-bottom: 2px solid #0066cc;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    
    /* Animation */
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    
    .fade-in {
        animation: fadeIn 1s;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab"] {
            font-size: 12px;
            padding: 8px 12px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header section
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://placeholder.com/100x100", width=100)  # Replace with actual logo
with col2:
    st.title("Safe Space Kenya")
    st.subheader("Creating Safe Spaces for Healing, Empowerment and Sustainable Development")

st.markdown("---")

# Mission and Vision
mission_expander = st.expander("Our Mission & Vision")
with mission_expander:
    st.write("""
    **Our Mission:** To provide holistic support, empowerment, and advocacy for vulnerable communities in Kenya, 
    fostering mental wellness, gender equality, economic independence, and environmental sustainability.
    
    **Our Vision:** A Kenya where every individual thrives in safe, supportive communities free from violence, 
    discrimination, and poverty, with equal access to opportunities for growth and development.
    """)

# Program tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "Counseling & Psychosocial", 
    "Youth Empowerment", 
    "Women Empowerment", 
    "Community Outreach", 
    "Skills Training", 
    "Advocacy & Awareness", 
    "Environment & Health", 
    "Other Services", 
    "Budget Allocation"
])

# Tab 1: Counseling & Psychosocial Services
with tab1:
    st.markdown('<div class="program-container fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Counseling & Psychosocial Services</h2>', unsafe_allow_html=True)
    
    st.write("""
    Our counseling and psychosocial services provide safe, confidential support for individuals and groups 
    dealing with trauma, mental health challenges, and personal difficulties.
    """)
    
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
with tab2:
    st.markdown('<div class="program-container fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Youth Empowerment & Education</h2>', unsafe_allow_html=True)
    
    st.write("""
    We empower Kenya's youth through educational support, leadership development, and skills building 
    to create the next generation of change-makers.
    """)
    
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
with tab3:
    st.markdown('<div class="program-container fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Women Empowerment & Gender Equality</h2>', unsafe_allow_html=True)
    
    st.write("""
    We champion gender equality and women's empowerment through education, economic initiatives, 
    and advocacy to create a more equitable society.
    """)
    
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
with tab4:
    st.markdown('<div class="program-container fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Community Outreach & Wellness</h2>', unsafe_allow_html=True)
    
    st.write("""
    Our community outreach programs bring essential services, education, and support directly to 
    underserved communities across Kenya.
    """)
    
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
with tab5:
    st.markdown('<div class="program-container fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Skills Training & Economic Empowerment</h2>', unsafe_allow_html=True)
    
    st.write("""
    We provide practical skills training and economic empowerment programs to help individuals 
    achieve financial independence and sustainable livelihoods.
    """)
    
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
with tab6:
    st.markdown('<div class="program-container fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Advocacy & Awareness Campaigns</h2>', unsafe_allow_html=True)
    
    st.write("""
    We drive social change through strategic advocacy and awareness campaigns on critical issues 
    affecting vulnerable communities in Kenya.
    """)
    
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
with tab7:
    st.markdown('<div class="program-container fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Environment, Health & Climate Action</h2>', unsafe_allow_html=True)
    
    st.write("""
    We address environmental challenges and promote sustainable practices that protect community health 
    and build resilience to climate change.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Services Offered")
        st.markdown("""
        - Environmental conservation initiatives
        - Climate change adaptation training
        - Sustainable agriculture programs
        - Tree planting and reforestation projects
        - Clean energy adoption support
        - Waste management and recycling programs
        - Water conservation and sanitation projects
        """)
    
    with col2:
        st.subheader("Impact Areas")
        st.markdown("""
        - Improved environmental conservation in target areas
        - Enhanced community resilience to climate shocks
        - Adoption of sustainable farming practices
        - Increased access to clean energy solutions
        - Improved waste management practices
        - Better water security in drought-prone areas
        - Reduced environmental degradation
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 8: Other Services
with tab8:
    st.markdown('<div class="program-container fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Other Services</h2>', unsafe_allow_html=True)
    
    st.write("""
    Additional services that support our mission and enhance our impact through partnerships, 
    donor relations, and innovative support mechanisms.
    """)
    
    services = st.selectbox("Select a service to learn more:", 
                          ["Donor Relations", "Live Chat Support", "Booking System", "Partnerships"])
    
    if services == "Donor Relations":
        st.subheader("Donor Relations")
        st.write("""
        We maintain transparent, accountable relationships with our donors through:
        - Regular impact reports and updates
        - Donor recognition programs
        - Customized engagement opportunities
        - Financial transparency initiatives
        - Donor feedback mechanisms
        """)
        
    elif services == "Live Chat Support":
        st.subheader("Live Chat Support")
        st.write("""
        Our confidential live chat service provides:
        - Immediate psychosocial support
        - Resource navigation assistance
        - Crisis intervention
        - Referral services
        - Anonymous support options
        """)
        # This would connect to an actual chat service in implementation
        if st.button("Start Live Chat"):
            st.info("Chat service would be activated here in the full implementation")
            
    elif services == "Booking System":
        st.subheader("Booking System")
        st.write("""
        Easily schedule appointments for our services:
        - Counseling sessions
        - Training workshops
        - Medical consultations
        - Legal aid appointments
        - Community outreach events
        """)
        # Example booking form
        service_type = st.selectbox("Select Service", ["Counseling", "Legal Aid", "Medical Consultation", "Training"])
        date = st.date_input("Preferred Date")
        time = st.time_input("Preferred Time")
        if st.button("Submit Booking Request"):
            st.success("Your booking request has been received. We'll contact you to confirm.")
            
    elif services == "Partnerships":
        st.subheader("Partnerships")
        st.write("""
        We collaborate with various organizations to maximize our impact:
        - Corporate partnerships for CSR initiatives
        - NGO collaborations for program implementation
        - Government partnerships for policy advocacy
        - Community-based organization networks
        - International development agencies
        """)
        if st.button("Learn About Partnership Opportunities"):
            st.info("Partnership information would be displayed here")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 9: Budget & Resource Allocation
with tab9:
    st.markdown('<div class="program-container fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="program-title">Budget & Resource Allocation</h2>', unsafe_allow_html=True)
    
    st.write("""
    We maintain transparency in our financial management to ensure resources are allocated effectively 
    to maximize impact in the communities we serve.
    """)
    
    # Budget allocation data
    budget_data = pd.DataFrame({
        'Category': ['Program Services', 'Administrative Costs', 'Fundraising & Marketing'],
        'Percentage': [70, 20, 10],
        'Color': ['#1f77b4', '#ff7f0e', '#2ca02c']
    })
    
    # Create pie chart
    fig = px.pie(budget_data, values='Percentage', names='Category', 
                 color='Category', color_discrete_map={
                     'Program Services': '#1f77b4',
                     'Administrative Costs': '#ff7f0e',
                     'Fundraising & Marketing': '#2ca02c'
                 })
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(showlegend=False, height=400)
    
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Program Services", "70%", 
                 "Direct community impact programs")
    
    with col2:
        st.metric("Administrative Costs", "20%", 
                 "Operational and management expenses")
    
    with col3:
        st.metric("Fundraising & Marketing", "10%", 
                 "Resource mobilization and awareness")
    
    st.subheader("Program-Specific Allocation")
    program_allocation = pd.DataFrame({
        'Program': ['Counseling Services', 'Youth Empowerment', 'Women Empowerment', 
                   'Community Outreach', 'Skills Training', 'Advocacy', 'Environment'],
        'Percentage': [20, 15, 15, 12, 13, 10, 15]
    })
    
    st.bar_chart(program_allocation, x='Program', y='Percentage')
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.subheader("Contact Us")
    st.write("""
    Email: info@safespacekenya.org  
    Phone: +254 700 123 456  
    Address: Nairobi, Kenya
    """)

with footer_col2:
    st.subheader("Quick Links")
    st.write("""
    [Annual Reports]() | [Get Involved]()  
    [News & Updates]() | [Privacy Policy]()
    """)

with footer_col3:
    st.subheader("Follow Us")
    st.write("""
    [Facebook]() | [Twitter]()  
    [Instagram]() | [LinkedIn]()
    """)

st.markdown('<div style="text-align: center; padding: 20px;">© 2023 Safe Space Kenya. All rights reserved.</div>', 
            unsafe_allow_html=True)
