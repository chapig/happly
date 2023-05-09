# Happly - Personal Job Assistant 🤖

Happly is a Python-based application designed to automate the job search and cover letter generation process using AI. This personal job assistant scans job openings on [remotive.com](https://remotive.com/) and crafts tailored cover letters based on your resume and the job description. Happly was developed to streamline the job search experience and alleviate stress, particularly for those facing challenges in the job market, such as Venezuelans.

In the future, we plan to expand Happly's capabilities by adding support for more websites.

## Preview

Happly will automatically generate a cover letter when it determines that you are a good fit for a job opening:
image

Happly will share its thoughts when it believes that you do not fit a particular job opening:
image

## Features 🌟

- Searches for jobs on [remotive.com](https://remotive.com/) using keywords extracted from your resume.
- Assesses the degree of alignment between a job opening and your resume.
- Creates personalized cover letters for each matching job opening.
- Saves generated cover letters as individual markdown files in the 'Cover Letters' directory.
- Customizable settings through the `settings.toml` file, allowing you to modify prompts, models, and more.

## Getting Started 🚀

### Prerequisites

- Python 3.6 or later
- An OpenAI API key

### Dependencies

- openai
- feedparser
- beautifulsoup4
- colorama
- yaspin

To install the required dependencies, run:

```
pip install -r requirements.txt
```

### Setup

1. Clone the Happly repository.

```
git clone https://github.com/chapig/happly.git
cd happly
```

2. Configure your settings in the `settings.toml` file.

```toml
# settings.toml

# OpenAI API Key
openai_key = "YOUR_API_KEY"

# Model to be used (default is gpt-3.5-turbo)
model = "gpt-3.5-turbo"

# Resume file name and path (default is resume.txt)
resume_file = "resume.txt"

# Save job openings to file (default is True)
save_job_openings = true

prompt_analyze_job_opening_and_resume = """
Please analyze the following job description and the provided resume of an applicant.
Based on your evaluation, determine if the applicant's qualifications and experience align
with the requirements of the job. If the match is strong, respond with 'positive'. If the
match is weak or non-existent, respond with 'negative'.
\n\nJob description:\n{job_opening}\n\nResume:\n{resume_text}\n\n"
"""

prompt_analyze_resume_for_keywords = """
Given the following resume, return the keywords that describe the applicant's skills,
and job experience. Examples: Software Development, Customer Service, Design Marketing,
Sales, Product, Business, Data, DevOps, Sysadmin, Finance, Legal, Human Resources, QA,
Writing. If the resume is not given, or provided please respond with 'No resume provided'
Resume: \n{resume_text}
"""

prompt_write_cover_letter = """
Please analyze the following job description and the provided resume of an applicant.
Create a cover letter to better align with the requirements of the job, highlighting relevant
qualifications and experiences.
Job description: {job_description}
Applicant's resume: {resume_text}
"""
```

3. Add your resume as a text file to the project directory, using the file name specified in `settings.toml`.

### Usage

Run the following command in the terminal to initiate the job search and cover letter generation process:

```
python happly.py
```

## How it Works 🧠

The application performs the following steps to discover matching jobs and produce cover letters:

1. Extracts keywords from your resume using OpenAI's GPT-3.
2. Searches for jobs on [remotive.com](https://remotive.com/) based on the extracted keywords.
3. Evaluates each job opening's compatibility with your resume using OpenAI's GPT-3.5-turbo.
4. Generates a tailored cover letter for each matching job using OpenAI's GPT-3.5-turbo.
5. Saves each generated cover letter as a markdown file in the 'Cover Letters' directory.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.