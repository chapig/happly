# Import TOML
import toml

# Read the TOML file ./settings.toml
settings = toml.load("./settings.toml")

key = settings["openai_key"]
resume = settings["resume_file"]
model = settings["model"]
save_job_openings = settings["save_job_openings"]
