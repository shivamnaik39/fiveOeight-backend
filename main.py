from fastapi import FastAPI, File, UploadFile, Response, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from utils.issues import get_issues
from utils.file_utils import upload_files, process_project
from utils.update_utils import update_data
from utils.screenshot import take_batch_screenshot
from typing import List
import os
import shutil
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict


max_response_size = 10*1024*1024  # set max_response_size to 10 megabytes

app = FastAPI(max_response_size=max_response_size)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/issues")
def get_accessibility_issues(url: str):
    issues = get_issues(url)
    return issues


accepted_content_types = ['application/zip', 'application/x-zip-compressed',
                          'application/octet-stream', 'application/x-compress', 'application/x-tar']


@app.post("/api/upload_zip")
def upload_zip(files: List[UploadFile] = File(...)):
    for file in files:
        if file.content_type not in accepted_content_types:
            return JSONResponse(content={"message": f"File {file.filename} is not a zip file"}, status_code=400)

    try:
        upload_files(files)
    except Exception as e:
        return JSONResponse(content={"message": f"Failed to upload zip file. Error: {e}"}, status_code=500)

    return {"message": "Files uploaded successfully !"}


@app.post("/api/fix_all")
def fix_all_issues():
    project_name = next(os.walk('uploads'))[1][0]
    input_dir = f"uploads/{project_name}"
    output_dir = f"downloads/{project_name}_modified"

    try:
        process_project(input_dir, output_dir)
    except Exception as e:
        return JSONResponse(content={"message": f"Failed to process zip file. Error: {e}"}, status_code=500)

    return {"message": "Files processed successfully!"}


@app.get("/api/download_zip")
def download_folder(response: Response):
    if os.path.exists("temp.zip"):
        os.remove("temp.zip")

    folder_name = next(os.walk('downloads'))[1][0]
    # Set the fixed path of the directory to download
    directory_path = os.path.join(os.getcwd(), "downloads", folder_name)

    # Check that the directory exists
    if not os.path.isdir(directory_path):
        response.status_code = 404
        return {"error": f"{folder_name} not found"}

    # Create a temporary file to write the ZIP archive to
    tmp_file = os.path.join(os.getcwd(), "temp.zip")

    # Write the contents of the directory to the ZIP file
    shutil.make_archive(os.path.splitext(tmp_file)[0], "zip", directory_path)

    # Set the response headers to indicate that we are sending a ZIP file
    zip_file_name = f"{os.path.splitext(folder_name)[0]}.zip"
    response.headers["Content-Type"] = "application/zip"
    response.headers[
        "Content-Disposition"] = f"attachment; filename={zip_file_name}"

    # Stream the ZIP file to the response using FileResponse
    return FileResponse(tmp_file, media_type="application/zip", status_code=200, filename=zip_file_name)


@app.get("/api/suggest_changes")
def suggest_changes():
    # fix_all_issues();
    file_path = "dump/changes.json"
    return FileResponse(file_path)


@app.post("/api/update_changes")
def update_changes(changes: Dict):
    try:
        update_data(changes)
        return {"message": "Changes updated successfully"}
    except:
        raise HTTPException(status_code=500, detail="Error processing data")

@app.get("/api/color_contrast_screenshots")
def get_screenshots(url):
    try:
        take_batch_screenshot(url)
        return {"message": "Sucess"}
    except:
        raise HTTPException(status_code=500, detail="Error processing data")


@app.get("/api/get_logs")
def suggest_changes():
    # fix_all_issues();
    file_path = "dump/changes.json"
    return FileResponse(file_path)