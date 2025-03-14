import streamlit as st
import re
from generatePass import password_generator

# Custom CSS for dark theme
st.markdown(
    """
    <style>
        .stApp {
            background-color: #142030;  /* Dark gray background */
            color: white;  /* White text */
        }
        h1, h2, h3, h4, h5, h6 {
            color: #e74c3c;  /* Red color for headings */
        }
        .stTextInput>label, .stButton>button {
            color: #27ae60;  /* Green color for text input labels and buttons */
        }
        .stAlert div {
            color: white;  /* Black text for alert content */
        }
        .stButton>button:hover {
            background-color: #2ecc71;  /* Light green background on hover */
            color: #ffffff;  /* White text on hover */
        }
        /* Custom CSS for number input label */
        .stNumberInput>label {
            color: #27ae60;  /* Green color for number input label */
        }
    </style>
    """,
    unsafe_allow_html=True
)

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("⚠️ Password should contain at least one uppercase letter.")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("⚠️ Password should contain at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("⚠️ Password should contain at least one digit.")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("⚠️ Password should contain at least one special character (!@#$%^&*).")
    
    if score >= 5:
        feedback.append("✅ Your Password is Strong")
    elif 3 <= score < 5:
        feedback.append('🟡 Your password is moderate. Consider improving it."')
    else:
        feedback.append('🔴 Your password is weak. Please follow the suggestions above.')
    
    return feedback

def main():
    st.title("🔐 Password Strength and Security Checker")
    
    st.write("Enter your password below to check its strength and security.")

    # Input for password
    password = st.text_input("Enter Your Password: ", type="password")

    # Button to check password strength
    if st.button('Check password strength'):
        if password:
            feedback = check_password_strength(password)
            for msg in feedback:
                st.write(msg)
        else:
            st.error("Please Enter Your Password")

    # Initialize session state
    if "generate_clicked" not in st.session_state:
        st.session_state.generate_clicked = False
    st.markdown("<hr style='border: none; height: 1px; background-color: white; margin-top: 20px; margin-bottom: 20px;'>", unsafe_allow_html=True)
    # Button to generate password
    if st.button('Generate password'):
        st.session_state.generate_clicked = True

    # Conditional rendering for password generation
    if st.session_state.generate_clicked:
        user_input = st.number_input("Please Enter Password Length (minimum 4): ", min_value=4, value=8)

        if st.button('Generate and Check Strong Password'):
            generated_password = password_generator(int(user_input)) 
            st.success(f"Generated Password: {generated_password}")
            feedback = check_password_strength(generated_password)
            for msg in feedback:
                st.write(msg)

if __name__ == '__main__':
    main()