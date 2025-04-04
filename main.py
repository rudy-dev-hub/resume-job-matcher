from app.resume_parser import parse_resume
from app.job_matcher import match_jobs

if __name__ == "__main__":
    resume_path = "data/rudresh_resume.pdf"
    parsed_resume = parse_resume(resume_path)

    print("\nExtracted Resume Info:")
    print(parsed_resume)

    match_results = match_jobs(parsed_resume, "data/job_descriptions.json")

    print("\nJob Matches:")
    for job, score in match_results:
        print(f"{job['title']} - Match Score: {score:.2f}")
