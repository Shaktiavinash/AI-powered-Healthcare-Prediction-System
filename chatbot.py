def ai_doctor_chatbot(user_input):

    responses = {
        "fever": "You may have an infection. Drink fluids and rest.",
        "diabetes": "Maintain healthy diet and monitor blood sugar.",
        "heart": "Regular exercise and low cholesterol diet help heart health.",
        "headache": "It may be due to stress or dehydration."
    }

    for key in responses:
        if key in user_input.lower():
            return responses[key]

    return "Please consult a healthcare professional for proper diagnosis."
   
 # ==========================================================
# ADVANCED AI DOCTOR CHATBOT
# ==========================================================

if page == "AI Doctor Chatbot":

    st.header("🤖 AI Doctor Chatbot")
    st.write("Ask medical questions and get general health advice.")

    # Chat history storage
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # User input
    user_prompt = st.chat_input("Ask a health question")

    if user_prompt:

        # Show user message
        st.session_state.messages.append({"role":"user","content":user_prompt})

        with st.chat_message("user"):
            st.write(user_prompt)

        text = user_prompt.lower()

        # Knowledge responses
        if "fever" in text or "temperature" in text:
            response = "Fever can indicate infection. Drink fluids, rest well, and consult a doctor if it continues."

        elif "diabetes" in text or "sugar" in text:
            response = "To manage diabetes maintain healthy diet, avoid excess sugar, exercise regularly, and monitor blood glucose."

        elif "heart" in text or "chest pain" in text:
            response = "Chest pain may indicate heart problems. Please consult a doctor immediately if symptoms persist."

        elif "liver" in text:
            response = "To keep your liver healthy avoid alcohol, eat balanced diet, and maintain healthy weight."

        elif "headache" in text:
            response = "Headaches may be caused by stress, dehydration or lack of sleep. Drink water and rest."

        elif "cold" in text or "cough" in text:
            response = "Common cold usually improves with rest, hydration and warm fluids."

        elif "diet" in text:
            response = "A balanced diet includes vegetables, fruits, whole grains, protein, and healthy fats."

        elif "exercise" in text:
            response = "Regular exercise improves heart health, metabolism, and overall well-being."

        else:
            response = "I recommend consulting a healthcare professional for accurate diagnosis."

        # Save response
        st.session_state.messages.append({"role":"assistant","content":response})

        # Display bot response
        with st.chat_message("assistant"):
            st.write(response)