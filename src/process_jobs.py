import os
import textwrap

from colorama import Fore
from yaspin import yaspin

from src.assistant import job_fits, write_cover_letter, assistant_message


class Resume:
    @property
    def resume(self):
        with open('./resume.txt', 'r', encoding="utf-8") as file:
            return file.read()


resume = Resume().resume


def generate_cover_letter_filename(title):
    output_dir = "./Cover Letters"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return os.path.join(output_dir, f"{title}.md")


def display_job_info(job):
    print(Fore.WHITE + "Job title: " + job['title'] + " at " + job['company'] + ".")
    print(Fore.WHITE + "Job link: " + job['link'])


def process_jobs(job_openings):
    for job in job_openings:

        display_job_info(job)
        analysis_job = yaspin()
        analysis_job.start()

        can_continue = job_fits(job_opening=job['description'], resume_text=resume)
        if "POSITIVE" in can_continue.upper():

            assistant_message("I think the job at " + job['title'] + " fits you.", color=Fore.LIGHTYELLOW_EX)
            assistant_message(textwrap.fill(can_continue.strip(), 80), color=Fore.LIGHTYELLOW_EX)
            assistant_message("I will write a cover letter for you.", color=Fore.LIGHTYELLOW_EX)

            spinner = yaspin()
            spinner.start()

            markdown_text = "# " + job['title'] + "\n" + "# " + job['company'] + "\n\n" + job[
                "link"] + "\n\n" + "# Cover Letter"

            cover_letter_text = write_cover_letter(job_description=job['description'], resume_text=resume)

            invalid_chars = "/\\:*?\"<>|"
            cover_letter_name = job['title'] + " at " + job['company']
            for char in invalid_chars:
                cover_letter_name = cover_letter_name.replace(char, "-")

            with open(generate_cover_letter_filename(cover_letter_name), "w", encoding="utf-8") as f:
                f.write(markdown_text + "\n\n# Cover Letter:\n" + cover_letter_text)

            assistant_message("Cover letter saved to " + generate_cover_letter_filename(cover_letter_name),
                              color=Fore.WHITE)
            spinner.ok("✔")
            spinner.stop()

        else:
            assistant_message("I don't think the job at " + job['title'] + " fits you.", color=Fore.LIGHTRED_EX)
            assistant_message(textwrap.fill(can_continue.strip(), 80), color=Fore.LIGHTRED_EX)

        analysis_job.stop()
        job_openings.remove(job)
