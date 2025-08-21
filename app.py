import streamlit as st

# -----------------------------
# Safe Space Kenya – Streamlit Website
# -----------------------------

# Page Config
st.set_page_config(page_title="Safe Space Kenya", page_icon="🌍", layout="wide")

# Title & Intro
st.title("🌍 Safe Space Kenya")
st.subheader("Creating Safe, Empowered & Resilient Communities")
st.write("Welcome to Safe Space Kenya, a non-profit organization dedicated to mental health, empowerment, education, counseling, and sustainability.")

# Sidebar Navigation
menu = st.sidebar.radio(
    "Navigate Programs",
    [
        "Home",
        "Mental Health & Psychosocial Support",
        "Guidance & Counseling",
        "Youth Empowerment & Leadership",
        "Education Support & Digital Literacy",
        "Women Empowerment & Gender Equality",
        "Community Outreach & Wellness",
        "Skills Training & Economic Empowerment",
        "Advocacy & Awareness Campaigns",
        "Environment & Climate Change",
        "Contact Us"
    ]
)

# Program Content
if menu == "Home":
    st.image("https://images.unsplash.com/photo-1524504388940-b1c1722653e1", use_container_width=True)
    st.markdown("""
    ## Our Mission
    To provide a safe, supportive space for mental health, empowerment, education, counseling, and climate resilience in Kenya.  
    We believe in **holistic community transformation** where wellness, education, empowerment and sustainability go hand in hand.

    ### What We Do
    Safe Space Kenya runs **nine flagship programs** designed to nurture **mental wellness, social empowerment, economic growth, and environmental sustainability** in communities.
    """)

elif menu == "Mental Health & Psychosocial Support":
    st.header("🧠 Mental Health & Psychosocial Support")
    st.write("""
    This is the heart of Safe Space Kenya. We offer a range of counseling services to ensure individuals receive **timely, affordable, and compassionate care**.  

    **Services include:**  
    - **Individual & group therapy sessions** led by professional counselors.  
    - **Trauma healing workshops** for survivors of abuse, GBV, and displacement.  
    - **Peer support circles** where community members can share and heal together.  
    - **24/7 hotline & online counseling**, making support available anytime, anywhere.  
    - **School-based mental health outreach** to nurture resilience in young learners.  
    """)

elif menu == "Guidance & Counseling":
    st.header("💬 Guidance & Counseling")
    st.write("""
    Our **Guidance & Counseling program** focuses on **life challenges, career development, and family issues**. It integrates counseling into education, work, and family life.  

    **Services include:**  
    - **Career guidance** for students, graduates, and job seekers.  
    - **Academic counseling** for learners struggling with performance or motivation.  
    - **Relationship & family therapy**, helping resolve conflicts and strengthen bonds.  
    - **Counseling for addiction recovery** (alcohol, drugs, internet).  
    - **Life skills & mentorship workshops** for personal growth and resilience.  
    """)

elif menu == "Youth Empowerment & Leadership":
    st.header("🌟 Youth Empowerment & Leadership")
    st.write("""
    We believe in **equipping youth with leadership skills, confidence, and resilience** to become tomorrow’s change-makers. Counseling support is embedded to ensure emotional wellness during the journey.  

    **Activities include:**  
    - **Youth leadership bootcamps** to build confidence, teamwork, and decision-making.  
    - **Peer mentorship programs**, linking experienced leaders with young people.  
    - **Soft skills training** (public speaking, conflict resolution, CV writing).  
    - **Counseling services** to help youth manage stress, career uncertainty, and life transitions.  
    - **Volunteer opportunities** to strengthen civic engagement and responsibility.  
    """)

elif menu == "Education Support & Digital Literacy":
    st.header("📚 Education Support & Digital Literacy")
    st.write("""
    Education is a right, and at Safe Space Kenya, we empower learners to succeed academically and mentally. Counseling is provided to struggling learners to address **academic stress, peer pressure, and mental blocks**.  

    **Programs include:**  
    - **School-based counseling & wellness talks** for students and teachers.  
    - **Tutoring & mentorship for vulnerable learners** who lack academic support.  
    - **Digital literacy training** (basic computer skills, safe internet use, coding).  
    - **Scholarship support & guidance** for learners from low-income families.  
    - **Parent counseling sessions** to improve support systems at home.  
    """)

elif menu == "Women Empowerment & Gender Equality":
    st.header("👩 Women Empowerment & Gender Equality")
    st.write("""
    This program provides a platform for **women and girls to thrive emotionally, socially, and economically**. Counseling plays a key role in trauma recovery and confidence-building.  

    **Key components:**  
    - **Entrepreneurship & financial literacy training** for self-reliance.  
    - **GBV awareness campaigns** and survivor counseling support groups.  
    - **Women’s leadership mentorship**, encouraging women to take up leadership roles.  
    - **Reproductive health & rights education**.  
    - **One-on-one counseling sessions** for women facing domestic violence or workplace discrimination.  
    """)

elif menu == "Community Outreach & Wellness":
    st.header("🤝 Community Outreach & Wellness")
    st.write("""
    We extend services to **communities, villages, and informal settlements** to ensure no one is left behind. Counseling services are integrated into all outreach activities.  

    **Outreach activities include:**  
    - **Community wellness forums** on mental health, parenting, and social cohesion.  
    - **Mobile counseling clinics** reaching underserved and rural communities.  
    - **Art, drama, and music therapy** for healing and self-expression.  
    - **Faith-based healing circles**, blending spirituality with psychological support.  
    """)

elif menu == "Skills Training & Economic Empowerment":
    st.header("💼 Skills Training & Economic Empowerment")
    st.write("""
    We empower communities with **income-generating skills** while addressing mental health challenges linked to poverty and unemployment.  

    **Services include:**  
    - **Vocational training** (crafts, tailoring, agribusiness, carpentry).  
    - **Eco-friendly income projects** (urban farming, recycling).  
    - **Entrepreneurship & startup incubation programs** with mentorship.  
    - **Group counseling sessions** to address financial stress and self-esteem.  
    - **Savings & investment clubs** for financial security.  
    """)

elif menu == "Advocacy & Awareness Campaigns":
    st.header("📢 Advocacy & Awareness Campaigns")
    st.write("""
    Advocacy is key in driving systemic change. We create awareness and influence policies while providing counseling to affected groups.  

    **Focus areas:**  
    - **Mental health awareness campaigns** to fight stigma and encourage care-seeking.  
    - **Anti-GBV advocacy**, supporting survivors through therapy and legal support.  
    - **Policy dialogue & civic engagement** to amplify youth voices.  
    - **Social media advocacy** on mental wellness, gender equality, and climate action.  
    - **Counseling sessions** for advocacy volunteers, ensuring they are emotionally supported.  
    """)

elif menu == "Environment & Climate Change":
    st.header("🌱 Environment & Climate Change")
    st.write("""
    Climate change affects not only our physical world but also our **mental health**. Safe Space Kenya integrates **eco-counseling** to help people cope with eco-anxiety and displacement trauma.  

    **Initiatives include:**  
    - **Climate awareness forums** in schools and communities.  
    - **Youth-led eco-projects** (tree planting, clean-up drives, recycling).  
    - **Green entrepreneurship projects** (urban farming, clean energy solutions).  
    - **Eco-mental health counseling** to manage climate-related stress.  
    - **Resilience-building workshops** for communities affected by droughts, floods, or displacement.  
    """)

elif menu == "Contact Us":
    st.header("📩 Contact Safe Space Kenya")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success(f"Thank you {name}, we have received your message and will respond soon!")

    st.markdown("""
    **Phone:** +254 758 943 430  
    **Email:** owinojerim269@gmail.com  
    """)

# Footer
st.markdown("---")
st.caption("© 2025 Safe Space Kenya | All Rights Reserved")
