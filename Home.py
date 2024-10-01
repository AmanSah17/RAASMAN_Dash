import streamlit as st

# Set page configuration
st.set_page_config(page_title="AIRSHED-RAASMAN - Home", layout="wide")

# Add a company logo
logo_path = "F:\\RAASMAN_DATA\\icon\\airshed.png"  # Replace with your logo path
st.image(logo_path, width=200)  # Adjust width as necessary

# Add some styling
st.markdown("""
<style>
    body {
        background-color: #f5f5dc;  /* A mix of white and cream */
    }
    .header {
        font-size: 2em;
        text-align: center;
        margin: 20px 0;
        color: #4B0082;  /* Dark Violet */
    }
    .subheader {
        font-size: 1.5em;
        text-align: left;
        color: #333;  /* Dark Grey */
    }
    .content {
        font-size: 1em;
        text-align: justify;
        color: #444;  /* Medium Grey */
    }
    .section {
        border: 2px solid #4B0082;  /* Dark Violet */
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        background-color: #ffffff;  /* White background for sections */
    }
</style>
""", unsafe_allow_html=True)

# Homepage content
st.markdown("<h1 class='header'>Welcome to AIRSHED</h1>", unsafe_allow_html=True)

# About AIRSHED section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<h2 class='subheader'>About AIRSHED</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
    The objective of team <strong>AIRSHED</strong> is to provide expert advice on air pollution, impact assessment, and air quality management to industry, scientific institutions, local authorities, regulatory authorities, and policymakers. 
    We, at AIRSHED, are drawn with a proven track record in the fields of air pollution, research, and practice. 
    Experienced in air quality, our solutions are appropriate, reliable, and cost-effective. 
    The company plays an important role in developing the air quality management plan.
</div>
""", unsafe_allow_html=True)

# List of services
st.markdown("""
<div class='content'>
    <strong>Our Services:</strong>
    <ul>
        <li>Source Apportionment</li>
        <li>Air Pollutant Emission Inventory</li>
        <li>GHG Emissions Inventory</li>
        <li>Ambient Air Quality Monitoring</li>
        <li>Consulting/Permitting</li>
        <li>Air Pollution Dispersion Modelling</li>
        <li>Receptor Modelling</li>
        <li>Air Toxics Risk Assessment</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# About RAASMAN section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<h2 class='subheader'>About RAASMAN</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
    The website provides real-time data on the sources of air pollution in the city and is expected to help the Delhi government frame effective policies to curb it. 
    The website reflects data collected and processed by two laboratories — a ‘super site’ and a mobile laboratory. 
    The laboratories were used for the “real-time source apportionment study”, under which data on Delhi’s air were collected over many months, and a model (software) created, which shows the sources of air pollution by using air from the surroundings as input.
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer with contact information
st.markdown("""
<div class='content' style='text-align: center;'>
    <hr>
    <p>&copy; 2024 AIRSHED | Contact us: info@airshed.com | Phone: +91 12345 67890</p>
</div>
""", unsafe_allow_html=True)
