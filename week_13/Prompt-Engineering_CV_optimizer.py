try:
    from docx import Document
except ImportError as exc:
    raise ImportError(
        "python-docx package is required. Install it with 'pip install python-docx'."
    ) from exc

try:
    import google.generativeai as genai
    from google.generativeai import types
except ImportError as exc:
    raise ImportError(
        "google-generativeai package is required. Install it with 'pip install google-generativeai'."
    ) from exc

import os
from typing import Optional


API_KEY = "AIzaSyCIlCY3kayy1Dr8IO2t5pUg0_4RKyyJCRM"
DEFAULT_MODEL = "gemini-1.0-pro"

"""
Develop a project using an LLM API to analyze your CV and provide personalized recommendations for updating it 
to better align with current trends and opportunities in the tech industry. 
Share the GitHub and result when you have done.
"""



def read_docx_text(path: str) -> str:
    doc = Document(path)
    lines = [p.text for p in doc.paragraphs if p.text.strip() != ""]
    return "\n".join(lines)


def resolve_model_name() -> str:
    env_model = os.environ.get("GEMINI_MODEL")
    if env_model:
        return env_model

    try:
        models = list(genai.list_models())
    except Exception:
        return DEFAULT_MODEL

    def supported_name(candidate: str) -> Optional[str]:
        for model in models:
            full_name = getattr(model, "name", "")
            name = full_name.split("/")[-1]
            methods = getattr(model, "supported_generation_methods", [])
            if name.endswith(candidate) and "generateContent" in methods:
                return name
        return None

    for candidate in ("gemini-1.5-flash", "gemini-1.0-pro", DEFAULT_MODEL):
        resolved = supported_name(candidate)
        if resolved:
            return resolved

    for model in models:
        methods = getattr(model, "supported_generation_methods", [])
        if "generateContent" in methods:
            full_name = getattr(model, "name", DEFAULT_MODEL)
            return full_name.split("/")[-1]

    return DEFAULT_MODEL


def instructor_chatbot():
    genai.configure(api_key=API_KEY)
    model_name = resolve_model_name()
    model = genai.GenerativeModel(model_name=model_name)
    generation_config = types.GenerationConfig(temperature=0.1)

    print("Welcome to AI CV analyzer service!\n")
    print(f"Using Gemini model: {model_name}\n")
    
    cv_paths = input("input your CV's location:")
    
    cv_content = read_docx_text(cv_paths)

    # Construct prompt
    prompt = f"""
    You are a professional CV analyzer. Provide an anylyze result based on current trends and opportunities in the tech industry.
    
    CV content:{cv_content}

    
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

        response = model.generate_content(
            prompt,
            generation_config=generation_config,
        )

        print(response.text)
        
    except Exception as e:
        message = (
            "Error communicating with Google Generative AI API:"
            f" {e}.\nHint: set GEMINI_MODEL environment variable (e.g. export GEMINI_MODEL=gemini-pro) "
            "or update google-generativeai to the latest version."
        )
        print(message)

if __name__ == "__main__":
    instructor_chatbot()
