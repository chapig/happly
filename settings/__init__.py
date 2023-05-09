# Import TOML
import toml

# Read the TOML file ./settings.toml
settings = toml.load("./settings.toml")

key = settings["openai_key"]
resume = settings["resume_file"]
model = settings["model"]
save_job_openings = settings["save_job_openings"]
prompt_write_cover_letter = settings["prompt_write_cover_letter"]
prompt_analyze_job_opening_and_resume = settings["prompt_analyze_job_opening_and_resume"]
prompt_analyze_resume_for_keywords = settings["prompt_analyze_resume_for_keywords"]
