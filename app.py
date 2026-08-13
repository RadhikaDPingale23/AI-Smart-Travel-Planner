import os
import streamlit as st
from dotenv import load_dotenv
from google import genai


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    client = genai.Client(api_key=API_KEY)
else:
    client = None


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Smart Travel Planner",
    page_icon="✈️",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("✈️ AI Smart Travel Planner")

st.write(
    "Plan your perfect trip using AI based on your "
    "starting point, destination, budget, duration, "
    "travel mode, interests, and travel style."
)


# =========================================================
# SIDEBAR - TRIP DETAILS
# =========================================================

st.sidebar.header("🧳 Trip Details")


# Starting Point
starting_point = st.sidebar.text_input(
    "📍 Starting Point",
    placeholder="e.g. Pune"
)


# Destination
destination = st.sidebar.text_input(
    "📍 Destination",
    placeholder="e.g. Goa"
)


# Number of Days
days = st.sidebar.number_input(
    "📅 Number of Days",
    min_value=1,
    max_value=30,
    value=3
)


# Budget
budget = st.sidebar.number_input(
    "💰 Total Budget (₹)",
    min_value=1000,
    value=15000,
    step=1000
)


# Travel Type
travel_type = st.sidebar.selectbox(
    "👥 Travel Type",
    [
        "Solo",
        "Couple",
        "Family",
        "Friends"
    ]
)


# Travel Mode
travel_mode = st.sidebar.selectbox(
    "🚆 Travel Mode",
    [
        "Train",
        "Bus",
        "Car",
        "Flight",
        "Bike"
    ]
)


# Interests
interests = st.sidebar.multiselect(
    "🎯 Your Interests",
    [
        "Beaches",
        "Adventure",
        "Food",
        "Shopping",
        "History",
        "Nature",
        "Culture",
        "Photography"
    ]
)


# =========================================================
# MAIN SECTION
# =========================================================

st.subheader("🌍 Your Travel Plan")


if destination:

    st.success(
        f"Destination selected: {destination}"
    )


    # =====================================================
    # TRIP SUMMARY
    # =====================================================

    col1, col2, col3 = st.columns(3)


    with col1:
        st.metric(
            "📅 Duration",
            f"{days} Days"
        )


    with col2:
        st.metric(
            "💰 Budget",
            f"₹{budget:,}"
        )


    with col3:
        st.metric(
            "👥 Travel Type",
            travel_type
        )


    # =====================================================
    # STARTING POINT & TRAVEL MODE
    # =====================================================

    col4, col5 = st.columns(2)


    with col4:

        if starting_point:
            st.info(
                f"📍 Starting Point: {starting_point}"
            )
        else:
            st.warning(
                "Please enter your starting point."
            )


    with col5:

        st.info(
            f"🚆 Travel Mode: {travel_mode}"
        )


    # =====================================================
    # INTERESTS
    # =====================================================

    st.write("### 🎯 Your Interests")


    if interests:

        st.write(
            ", ".join(interests)
        )

    else:

        st.info(
            "Please select at least one interest."
        )


    # =====================================================
    # GENERATE TRAVEL PLAN
    # =====================================================

    if st.button(
        "✨ Generate AI Travel Plan",
        type="primary"
    ):


        # -------------------------------------------------
        # CHECK API KEY
        # -------------------------------------------------

        if not API_KEY:

            st.error(
                "❌ Google API key not found. "
                "Please add GOOGLE_API_KEY to your .env file."
            )

            st.stop()


        # -------------------------------------------------
        # CHECK STARTING POINT
        # -------------------------------------------------

        if not starting_point:

            st.warning(
                "⚠️ Please enter your starting point."
            )

            st.stop()


        # -------------------------------------------------
        # CHECK INTERESTS
        # -------------------------------------------------

        if not interests:

            st.warning(
                "⚠️ Please select at least one interest."
            )

            st.stop()


        # =================================================
        # AI PROMPT
        # =================================================

        prompt = f"""
You are an expert AI travel planner.

Create a practical, realistic and personalized travel
itinerary based on the following trip details.

STARTING POINT:
{starting_point}

DESTINATION:
{destination}

NUMBER OF DAYS:
{days}

TOTAL BUDGET:
₹{budget}

TRAVEL TYPE:
{travel_type}

TRAVEL MODE:
{travel_mode}

INTERESTS:
{", ".join(interests)}


IMPORTANT REQUIREMENTS:

1. Create a detailed day-by-day itinerary.

2. Start the journey from the given starting point.

3. Consider the selected travel mode
   ({travel_mode}) when planning transportation.

4. Suggest suitable places to visit.

5. Suggest activities according to the selected interests.

6. Suggest food options and local specialties.

7. Provide approximate transportation costs.

8. Provide approximate accommodation costs.

9. Provide approximate food costs.

10. Provide approximate activity/entry costs.

11. Keep the estimated total cost within the given
    budget of ₹{budget}, wherever reasonably possible.

12. Consider the travel type ({travel_type}).

13. Mention approximate travel time between major places
    whenever useful.

14. Use Indian Rupees (₹) for costs.

15. Do not make unrealistic promises.

16. If the budget is insufficient, clearly mention that
    and suggest practical alternatives.

17. Give useful travel tips.

18. Keep the response simple, clear and well structured.


FORMAT:

# ✈️ Trip Overview

Give a short summary of the trip.

# 🗓️ Day-by-Day Itinerary

## Day 1
Morning:
Afternoon:
Evening:
Food:
Estimated Cost:

## Day 2
Morning:
Afternoon:
Evening:
Food:
Estimated Cost:

Continue for all days.

# 💰 Budget Breakdown

Transportation:
Accommodation:
Food:
Activities:
Other Expenses:
Total Estimated Cost:

# 💡 Travel Tips

Give useful practical tips.

Make the itinerary easy to understand and suitable
for a real traveler.
"""


        # =================================================
        # GENERATE AI RESPONSE
        # =================================================

        try:

            with st.spinner(
                "🤖 AI is creating your personalized travel plan..."
            ):

                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt
                )

                travel_plan = response.text


            # =================================================
            # DISPLAY ITINERARY
            # =================================================

            st.subheader(
                "🗓️ Your Personalized Itinerary"
            )

            st.markdown(
                travel_plan
            )


            # =================================================
            # BUDGET SUMMARY
            # =================================================

            st.subheader(
                "💰 Budget Summary"
            )

            daily_budget = budget / days


            budget_col1, budget_col2 = st.columns(2)


            with budget_col1:

                st.metric(
                    "Total Budget",
                    f"₹{budget:,}"
                )


            with budget_col2:

                st.metric(
                    "Average Daily Budget",
                    f"₹{daily_budget:,.0f}"
                )


            # =================================================
            # SUCCESS MESSAGE
            # =================================================

            st.success(
                "🎉 Your AI-powered travel plan has been "
                "generated successfully!"
            )


        except Exception as e:

            st.error(
                "❌ Unable to generate the AI travel plan."
            )

            st.warning(
                "Please check your API key, internet connection, "
                "and Gemini configuration."
            )

            st.code(
                str(e)
            )


else:

    st.info(
        "👈 Enter your destination from the sidebar "
        "to get started."
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "✈️ AI Smart Travel Planner | "
    "Built with Python, Streamlit & Google Gemini"
)