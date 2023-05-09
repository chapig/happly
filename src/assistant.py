import openai
from colorama import Fore

from settings import key, model, prompt_analyze_job_opening_and_resume, prompt_write_cover_letter

openai.api_key = key


def assistant_message(message: str, color):
    print(Fore.LIGHTGREEN_EX + "Assistant: " + color + message)


# Evaluate if a job opening fits the applicant's resume
def job_fits(job_opening, resume_text):
    prompt = prompt_analyze_job_opening_and_resume.format(
        job_opening=job_opening, resume_text=resume_text)

    messages = [
        {"role": "user",
         "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    assistant = response.choices[0].message['content'].strip()
    return assistant.strip()


# Create a cover letter based on the job description and applicant's resume
def write_cover_letter(job_description, resume_text):
    prompt = prompt_write_cover_letter.format(job_description=job_description, resume_text=resume_text)
    messages = [
        {"role": "user",
         "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    return response.choices[0].message['content'].strip()
