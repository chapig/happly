import openai.error
from colorama import Fore

from src.assistant import assistant_message
from src.download_remotive import get_jobs
from src.keywords import keywords
from src.process_jobs import process_jobs
from settings import save_job_openings

def test_openai_api_connection():
    """Test connection to OpenAI API."""
    assistant_message("Testing connection to OpenAI API.", color=Fore.LIGHTYELLOW_EX)
    try:
        from src.assistant import job_fits

        job_fits(job_opening="Test", resume_text="Test")
    except openai.error.AuthenticationError:
        assistant_message("Connection to OpenAI API failed. Please check your API key.", color=Fore.LIGHTRED_EX)
        exit(1)
    except openai.error.RateLimitError:
        assistant_message("Connection to OpenAI API failed due to billing settings. Please check your API key.",
                          color=Fore.LIGHTRED_EX)
        exit(1)


def search_jobs_for_keywords(resume_keywords):
    """Search for jobs matching the given keywords and process them."""
    for keyword in resume_keywords:
        assistant_message(f"Searching for jobs with keyword {keyword}.", color=Fore.LIGHTYELLOW_EX)
        job_openings = get_jobs(keyword)
        job_openings = list(job_openings)
        if save_job_openings:
            save_job_openings_to_file(job_openings, keyword)
        process_jobs(job_openings)


def save_job_openings_to_file(job_openings, keyword):
    """Save job openings to a JSON file."""
    with open(f"memory/{keyword}.json", "w", encoding="utf-8") as file:
        file.write(str(list(job_openings)))


def main():
    test_openai_api_connection()

    assistant_message("Hello, I am your personal assistant. I will help you find a job that fits you.",
                      color=Fore.LIGHTYELLOW_EX)
    resume_keywords = keywords()

    search_jobs_for_keywords(resume_keywords)


if __name__ == "__main__":
    main()
