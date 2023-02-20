from fastapi import FastAPI
from utils.issues import get_issues


max_response_size = 10*1024*1024  # set max_response_size to 10 megabytes

app = FastAPI(max_response_size=max_response_size)


@app.get("/api/issues")
def get_accessibility_issues(url: str):
    issues = get_issues(url)
    return issues
