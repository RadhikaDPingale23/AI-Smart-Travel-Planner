# ✈️ AI Smart Travel Planner

## 📌 Introduction

AI Smart Travel Planner is an AI-powered web application that helps users create personalized travel plans based on their travel preferences.

The application allows users to enter details such as their starting point, destination, number of days, budget, travel type, travel mode, and interests. Based on these inputs, the application uses the Google Gemini API to generate a personalized day-by-day travel itinerary.

The generated travel plan includes suggested activities, food recommendations, estimated expenses, and useful travel tips, helping users plan their trips in a simple and convenient way.

This project was developed as a personal project using **Python, Streamlit, and Google Gemini API**.

## ✨ Key Features

- 🌍 Enter any destination and starting point
- 📅 Choose the number of travel days
- 💰 Set a total trip budget
- 👥 Select travel type such as Solo, Friends, Family, or Couple
- ✈️ Choose a preferred travel mode such as Flight, Train, Bus, Car, or Bike
- 🎯 Select interests such as Beaches, Food, Shopping, Adventure, History, and Photography
- 🤖 Generate personalized travel itineraries using Google Gemini AI
- 🗓️ Get a day-by-day travel plan
- 🍴 Receive food and activity recommendations
- 💵 Get estimated trip expenses based on the selected budget
- 🎒 Get useful travel tips and suggestions
- 🌐 Plan trips for destinations around the world

## 🛠️ Technologies Used

- **Python** – Main programming language used to develop the application
- **Streamlit** – Used to build the interactive web interface
- **Google Gemini API** – Used for AI-powered travel plan generation
- **Google GenAI SDK** – Used to connect the application with Gemini
- **python-dotenv** – Used to securely manage the API key through environment variables
- **Git & GitHub** – Used for version control and project hosting


## ⚙️ How the Project Works

1. The user enters the **starting point** and **destination**.
2. The user selects the **number of days** and enters the **total budget**.
3. The user selects the **travel type** and **preferred travel mode**.
4. The user selects their **travel interests**.
5. The application collects all the selected travel preferences.
6. These preferences are sent to the **Google Gemini API** through a structured AI prompt.
7. Gemini generates a personalized **day-by-day travel itinerary**.
8. The application displays the itinerary along with **activities, food suggestions, estimated expenses, and travel tips**.
