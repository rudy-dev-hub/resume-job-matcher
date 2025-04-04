import json

def match_jobs(parsed_resume, job_file_path):
    with open(job_file_path, "r") as f:
        jobs = json.load(f)

    results = []
    for job in jobs:
        score = 0
        for skill in parsed_resume["skills"]:
            if skill in job["description"].lower():
                score += 1
        results.append((job, score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results
