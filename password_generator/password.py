import streamlit as st
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    # Initialize an empty character pool
    characters = ''
    
    # Add selected character types to the pool
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Check if at least one character type is selected
    if not characters:
        return "Please select at least one character type!"
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.title("Password Generator")
    
    # Password length slider
    length = st.slider("Password Length", min_value=6, max_value=30, value=12)
    
    # Character type checkboxes
    col1, col2 = st.columns(2)
    with col1:
        use_uppercase = st.checkbox("Uppercase Letters", value=True)
        use_lowercase = st.checkbox("Lowercase Letters", value=True)
    with col2:
        use_numbers = st.checkbox("Numbers", value=True)
        use_special = st.checkbox("Special Characters", value=False)
    
    # Generate password button
    if st.button("Generate Password"):
        password = generate_password(
            length,
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_special
        )
        st.success(f"Generated Password: {password}")
        
        # Copy button
        st.code(password)
        st.button("Copy to Clipboard", help="Click to copy password")

if __name__ == "__main__":
    main()



