# Happly - Personal Job Assistant 🤖

Happly is a Python-based application that automates job search and cover letter generation using AI. This personal job assistant scans job openings on [remotive.com](https://remotive.com/) and creates tailored cover letters based on your resume and the job description. It was created to make the job search process easier and less stressful, especially for people facing challenges in the job market, like Venezuelans.

## Features 🌟

- Searches for jobs on [remotive.com](https://remotive.com/) based on the keywords extracted from your resume.
- Evaluates how well a job opening aligns with your resume.
- Generates a custom cover letter for each matching job opening.
- Stores generated cover letters as separate markdown files in the 'Cover Letters' directory.
- Customizable settings using the `settings.toml` file.

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
# OpenAI API Key
openai_key = "your_key"

# Model to be used (default is gpt-3.5-turbo)
model = "gpt-3.5-turbo"

# Resume file name and path (default is resume.txt)
resume_file = "resume.txt"

# Save job openings to file (default is True)
save_job_openings = true
```

3. Add your resume as a text file to the project directory, using the file name specified in `settings.toml`.

### Usage

Run the following command in the terminal to start the job search and cover letter generation process:

```
python happly.py
```

## How it Works 🧠

The application uses the following steps to find matching jobs and generate cover letters:

1. Extracts keywords from your resume using OpenAI's GPT-3.
2. Searches for jobs on [remotive.com](https://remotive.com/) based on the extracted keywords.
3. Evaluates each job opening's alignment with your resume using OpenAI's GPT-3.5-turbo.
4. Generates a custom cover letter for each matching job using OpenAI's GPT-3.5-turbo.
5. Saves each generated cover letter as a markdown file in the 'Cover Letters' directory.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
