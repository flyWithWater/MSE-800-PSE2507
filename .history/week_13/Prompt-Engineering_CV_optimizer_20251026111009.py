from urllib import response
from google import genai

from google.genai import types
import os

from isort import file

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
    
    cv_content = file()

    # Construct prompt
    prompt = f"""
    You are a professional CV analyzer. Provide an anylyze result based on current trends and opportunities in the tech industry.
    
    CV content:
    {cv_content}

    
    Based on your personal information of an expert and the trends online currentlly.
    Then, give the final result of the CV, which contains multiple items/points of suggestion. All the suggestions are about how to modify and optimise the CV to saticefy the needs of the industry, to help the person can get more chances to get an interview and jobs.
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