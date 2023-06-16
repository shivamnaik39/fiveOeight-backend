import os
import json
import zipfile
import shutil
import tempfile
from utils.html_utils import get_soup, extract_image_names, add_name_and_label, add_alt_to_anchor_tags, add_lang_attr, convert_deprecated_tags, process_video
from utils.css_utils import replace_css_colors, update_css_colors

# List of deprecated HTML tags to search for
deprecated_tags = ['strike', 'font', 'center']


def process_html_file(input_file_path, output_file_path, changes):
    """
    Processes a single HTML file, searching for deprecated tags and replacing them with span tags.

    :param input_file_path: path to the input HTML file
    :param output_file_path: path to the output HTML file
    """ 
    print(input_file_path)

    soup = get_soup(input_file_path)

    # extract alt tags for image
    soup, alt_changes = extract_image_names(soup)

    rel_path = os.path.relpath(input_file_path, "uploads")

    if rel_path not in changes['img_alt']:
        changes['img_alt'][rel_path] = alt_changes

    # Add name and label to input
    soup = add_name_and_label(soup)

    # Add alt tags to anchor tags
    soup = add_alt_to_anchor_tags(soup)

    # Add lang attribute to any html tags
    soup = add_lang_attr(soup)

    # Add captions to video
    # soup = process_video(soup, input_file_path, output_file_path)

    # Add lang attribute to any html tags
    soup = convert_deprecated_tags(soup, ['i', 'b', 'center'])

    # Write modified HTML to new file in output directory
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, 'w') as f:
        f.write(str(soup))

    # print(changes)

    if not os.path.exists("dump"):
        os.makedirs("dump")

    # Write changes to log file
    with open("dump/changes.json", 'w') as f:
        f.write(json.dumps(changes))


def process_files(input_dir, output_dir, changes, processed_files=None):
    """
    Traverses a directory and its subdirectories, and processes all HTML files found in them.

    :param input_dir: path to the input directory to traverse
    :param output_dir: path to the output directory to write the modified HTML files
    """

    if processed_files is None:
        processed_files = set()

    for dirpath, dirnames, filenames in os.walk(input_dir):
        if 'node_modules' in dirnames:
            # Skip the 'node_modules' directory and all its contents
            dirnames.remove('node_modules')
        if '.git' in dirnames:
            # Skip the 'node_modules' directory and all its contents
            dirnames.remove('.git')

        if '.angular' in dirnames:
            # Skip the 'node_modules' directory and all its contents
            dirnames.remove('.angular')

        for dirname in dirnames:
            # Recurse into subdirectories
            input_subdir = os.path.join(dirpath, dirname)
            output_subdir = os.path.join(
                output_dir, os.path.relpath(input_subdir, start=input_dir))
            os.makedirs(output_subdir, exist_ok=True)
            process_files(input_subdir, output_subdir,
                          changes, processed_files)

        for filename in filenames:
            skip_files1 = ["cart-page", "footer", "header",
                           "home", "not-found", "product-page", "search", "tags"]

            skip_files2 = ["cart-page",
                           "home", "not-found", "product-page", "search", "tags"]

            skip_files_html = [f"{x}.component.html" for x in skip_files1]
            skip_files_css = [f"{x}.component.css" for x in skip_files2]

            condition_html = filename not in skip_files_html
            condition_css = filename not in skip_files_css

            if filename.endswith('.html') and condition_html and filename not in processed_files:
                processed_files.add(filename)
                print(filename)
                input_file_path = os.path.join(dirpath, filename)
                output_file_path = os.path.join(
                    output_dir, os.path.relpath(input_file_path, start=input_dir))

                process_html_file(input_file_path, output_file_path, changes)

            elif filename.endswith('.css') and condition_css and filename not in processed_files:
                processed_files.add(filename)
                print(filename)
                input_file_path = os.path.join(dirpath, filename)
                output_file_path = os.path.join(
                    output_dir, os.path.relpath(input_file_path, start=input_dir))

                process_css_file(input_file_path, output_file_path, changes)

            elif filename not in processed_files:
                # Copy non-HTML files to output directory
                processed_files.add(filename)
                input_filepath = os.path.join(dirpath, filename)
                output_filepath = os.path.join(
                    output_dir, os.path.relpath(input_filepath, start=input_dir))
                os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
                shutil.copy2(input_filepath, output_filepath)


def process_css_file(input_file_path, output_file_path, changes):
    """
    Traverses a directory and its subdirectories, and processes all CSS files found in them.
    Currently does nothing.

    :param input_dir: path to the input directory to traverse
    :param output_dir: path to the output directory to write the modified CSS files
    """
    # This function is a placeholder and currently does nothing
    color_changes = replace_css_colors(input_file_path, output_file_path)
    rel_path = os.path.relpath(input_file_path, "uploads")

    if rel_path not in changes['color_contrast']:
        changes['color_contrast'][rel_path] = color_changes

    if not os.path.exists("dump"):
        os.makedirs("dump")

    # Write changes to log file
    with open("dump/changes.json", 'w') as f:
        f.write(json.dumps(changes))


def upload_files(files):
    input_location = "uploads"
    output_location = "downloads"
    # Remove existing files from the input_files directory
    if os.path.exists(input_location):
        shutil.rmtree(input_location)
    os.makedirs(input_location)

    if os.path.exists(output_location):
        shutil.rmtree(output_location)
    os.makedirs(output_location)

    if os.path.exists("temp.zip"):
        os.remove("temp.zip")

    for file in files:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            # Write the contents of the uploaded file to the temporary file
            shutil.copyfileobj(file.file, tmp)
            # Extract the uploaded zip file to the input_files directory
            with zipfile.ZipFile(tmp.name, 'r') as zip_ref:
                zip_ref.extractall(input_location)
        os.unlink(tmp.name)


def process_project(input_dir, output_dir):
    changes = {"img_alt": {}, "color_contrast": {}}
    if input_dir == output_dir:
        raise ValueError(
            "Input directory and output directory cannot be the same.")
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    process_files(input_dir, output_dir, changes)


def create_zip_file(directory_path, zip_file_path):
    """Create a ZIP archive of the contents of a directory."""
    shutil.make_archive(os.path.splitext(zip_file_path)
                        [0], "zip", directory_path)


def delete_file(file_path):
    """Delete a file from disk."""
    os.remove(file_path)
