import os
import textwrap

import openai
from colorama import Fore
from yaspin import yaspin

from settings import model, prompt_analyze_resume_for_keywords
from settings import resume as resume_file
from src.assistant import assistant_message

resume = open(resume_file, "r", encoding="utf-8").read()


def read_keywords_from_file():
    """Read keywords from the 'memory/keywords.txt' file."""
    with open("memory/keywords.txt", "r", encoding="utf-8") as file:
        return file.read()


def save_keywords_to_file(keywords):
    """Save keywords to the 'memory/keywords.txt' file."""
    with open("memory/keywords.txt", "w", encoding="utf-8") as file:
        file.write(", ".join(keywords))


def prompt_user_to_use_previous_keywords(file_content):
    """Ask the user if they want to use the previously stored keywords."""
    assistant_message(
        "I noticed that you have already run my software before. "
        "The keywords I found last time were:",
        color=Fore.LIGHTYELLOW_EX)
    assistant_message(Fore.LIGHTBLUE_EX + textwrap.fill(file_content.strip(), 80), color=Fore.LIGHTYELLOW_EX)

    return input(Fore.LIGHTGREEN_EX + "Assistant: " + Fore.LIGHTYELLOW_EX +
                 "Do you wish me to use the same keywords, "
                 "if not, I will read the resume again" + Fore.LIGHTMAGENTA_EX +
                 " (y/n): " + Fore.LIGHTYELLOW_EX).lower() == "y"


def get_keywords_from_resume(_resume):
    """Retrieve keywords from the resume using the OpenAI API."""
    spinner = yaspin()
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts keywords from a resume."},
            {"role": "user",
             "content": prompt_analyze_resume_for_keywords.format(resume_text=_resume)}
        ],
        max_tokens=100,
    )
    if "No resume provided" in response.choices[0].message.content:
        assistant_message("No resume provided. Please provide a proper resume.", color=Fore.LIGHTRED_EX)
        exit(1)
    spinner.ok("✔")
    spinner.stop()
    return response.choices[0].message.content.strip().split(",")


def keywords(_resume=resume):
    if not os.path.exists("memory/keywords.txt"):
        open("memory/keywords.txt", "w", encoding="utf-8").close()

    file_content = read_keywords_from_file()

    if file_content != "":
        if prompt_user_to_use_previous_keywords(file_content):
            assistant_message("I will use the same keywords as last time.", color=Fore.LIGHTYELLOW_EX)
            return file_content.split(", ")

    assistant_message("I will read your resume and find the best matching keywords.", color=Fore.LIGHTYELLOW_EX)

    extracted_keywords = get_keywords_from_resume(_resume)

    stripped_keywords = list(map(lambda x: x.strip(), extracted_keywords))

    assistant_message("I have found the following keywords: " + ", ".join(stripped_keywords), color=Fore.LIGHTBLUE_EX)

    save_keywords_to_file(stripped_keywords)

    return stripped_keywords
