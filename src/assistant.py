import openai
from colorama import Fore

from settings import key, model

openai.api_key = key


def assistant_message(message: str, color):
    print(Fore.LIGHTGREEN_EX + "Assistant: " + color + message)


# Evaluate if a job opening fits the applicant's resume
def job_fits(job_opening, resume_text):
    messages = [
        {"role": "user",
         "content": (f"Please analyze the following job description and the provided resume of an applicant. "
                     f"Based on your evaluation, determine if the applicant's qualifications and experience align "
                     f"with the requirements of the job. If the match is strong, respond with 'positive'. If the "
                     f"match is weak or non-existent, respond with 'negative'."
                     f"\n\nJob description:\n{job_opening}\n\nResume:\n{resume_text}\n\n")}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    assistant = response.choices[0].message['content'].strip()
    return assistant.strip()


# Create a cover letter based on the job description and applicant's resume
def write_cover_letter(job_description, resume_text):
    messages = [
        {"role": "user",
         "content": (f"Please analyze the following job description and the provided resume of an applicant. "
                     f"Create a cover letter to better align with the requirements of the job, highlighting relevant "
                     f"qualifications and experiences."
                     f"Job description: {job_description}  Applicant's resume: {resume_text}.")}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    return response.choices[0].message['content'].strip()
