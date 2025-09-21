from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash", 
    )

st.title("AI Travel Planner")

# Input fields for travel planning
destination = st.text_input("Enter your destination:")
trip_duration = st.text_input("Enter trip duration (e.g., 3 days, 1 week):")
interests = st.multiselect("Select your interests:", ["Food", "History", "Nature", "Shopping", "Art & Culture", "Nightlife", "Relaxation"])
accommodation = st.selectbox("Preferred accommodation:", ["Hotel", "Hostel", "Airbnb", "Resort", "Vacation Rental"])
season = st.selectbox("Travel season:", ["Spring", "Summer", "Fall", "Winter"])
dietary_restrictions = st.selectbox("Any dietary restrictions?", ["None", "Vegetarian", "Vegan", "Gluten-free", "Dairy-free", "Other"])

budget = st.number_input("Enter your Budget (in pkr)", min_value=0)
travel_companions = st.selectbox("Traveling with:", ["Solo", "Partner", "Family", "Friends"])


prompt = f"""
You are an expert travel planner with extensive knowledge about destinations worldwide.
You must follow the instructions carefully and stay within your expertise.
If any information is missing or unclear, politely state the limitations instead of making up facts.

The user's travel details are as follows:
Destination: {destination}
Trip Duration: {trip_duration}
Interests: {interests}
Accommodation Preference: {accommodation}
Season: {season}
Dietary Restrictions: {dietary_restrictions}
Budget Level in pkr: {budget}
Travel Companions: {travel_companions}

Based on this information, provide:
1. Destination Overview: Brief introduction to the destination and what makes it special
2. Itinerary: A day-by-day plan that matches the trip duration
3. Activity Recommendations: Suggestions based on the user's interests
4. Dining Suggestions: Restaurant and food recommendations considering dietary restrictions
5. Accommodation Tips: Advice on where to stay based on preferences
6. Packing Tips: What to bring considering the season and activities
7. Budgeting Advice: How to manage expenses based on the travel style and budget level
8. Local Tips: Cultural norms, transportation options, and safety considerations

Important Rules:
- Do not provide any medical or safety advice that could be considered professional
- If the destination is not clear or too vague, ask for clarification
- Keep the response well-organized and easy to read
- Do not hallucinate any information or make up facts about the destination
- If you're not familiar with the destination, politely state that
"""

if st.button("Generate Plan"):
    with st.spinner("Generating your personalized fitness and diet plan..."):
        result = model.invoke(prompt)
        st.subheader("Full Response")
        st.write(result.content)
    