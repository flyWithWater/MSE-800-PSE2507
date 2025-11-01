from urllib import response
from google import genai

from google.genai import types
import os

API_KEY = "AIzaSyBpzcpd8LpW36Dq_VioA0Z-hkYdcNFQjwc"

"""
Develop a project using an LLM API to analyze your CV and provide personalized recommendations for updating it 
to better align with current trends and opportunities in the tech industry. 
Share the GitHub and result when you have done.
"""

def instructor_chatbot():
    client = genai.Client(api_key=API_KEY)

    
    print("Welcome to AI CV analyzer service!\n")
    
    cv_paths = input("input your CV's location:")
    

    # Construct prompt
    prompt = f"""
    You are a professional CV analyzer. Provide an itinerary recommendation based on user data.
    
    User Details:
    - days: {days} days
    - destination: {location} city
    - Age: {age} years
    
    Based on your personal information, 
    Then, give a structured itinerary with a name of the place, address and short description for each day seperatly in order with maximom three activities in a day.
    """
    
    try:
        # response = openai.ChatCompletion.create(
        #     model="gpt-4",
        #     messages=[{"role": "system", "content": "You are a professional itinerary recommender."},
        #               {"role": "user", "content": prompt}],
        #     max_tokens=200,
        #     temperature=0.7
        # )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(system_instruction="You are a professional itinerary recommender.",temperature=0.1),
            contents=[prompt]
        )
        
        
        print("\n My Name is Hadi as AI Itinerary expert:")
        print(response.text)
        
    except Exception as e:
        print("Error communicating with OpenAI API:", e)

if __name__ == "__main__":
    instructor_chatbot()