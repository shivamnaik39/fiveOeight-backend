import os
import zipfile
import shutil
import tempfile
from utils.html_utils import get_soup, extract_image_names, add_name_and_label, add_alt_to_anchor_tags, add_lang_attr, convert_deprecated_tags

# List of deprecated HTML tags to search for
deprecated_tags = ['strike', 'font', 'center']


def process_html_file(input_file_path, output_file_path):
    """
    Processes a single HTML file, searching for deprecated tags and replacing them with span tags.

    :param input_file_path: path to the input HTML file
    :param output_file_path: path to the output HTML file
    """

    soup = get_soup(input_file_path)

    # extract alt tags for image
    soup = extract_image_names(soup)

    # Add name and label to input
    soup = add_name_and_label(soup)

    # Add alt tags to anchor tags
    soup = add_alt_to_anchor_tags(soup)

    # Add lang attribute to any html tags
    soup = add_lang_attr(soup)

    # Add lang attribute to any html tags
    soup = convert_deprecated_tags(soup, ['i', 'b', 'center'])

    # Write modified HTML to new file in output directory
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, 'w') as f:
        f.write(str(soup))


def process_files(input_dir, output_dir):
    """
    Traverses a directory and its subdirectories, and processes all HTML files found in them.

    :param input_dir: path to the input directory to traverse
    :param output_dir: path to the output directory to write the modified HTML files
    """
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
            process_files(input_subdir, output_subdir)

        for filename in filenames:
            if filename.endswith('.html'):
                input_file_path = os.path.join(dirpath, filename)
                output_file_path = os.path.join(
                    output_dir, os.path.relpath(input_file_path, start=input_dir))

                process_html_file(input_file_path, output_file_path)

            # elif filename.endswith('.css'):
            #     input_file_path = os.path.join(dirpath, filename)
            #     output_file_path = os.path.join(
            #         output_dir, os.path.relpath(input_file_path, start=input_dir))

            #     process_css_file(input_file_path, output_file_path)

            else:
                # Copy non-HTML files to output directory
                input_filepath = os.path.join(dirpath, filename)
                output_filepath = os.path.join(
                    output_dir, os.path.relpath(input_filepath, start=input_dir))
                os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
                shutil.copy2(input_filepath, output_filepath)


def process_css_file(input_file_path, output_file_path):
    """
    Traverses a directory and its subdirectories, and processes all CSS files found in them.
    Currently does nothing.

    :param input_dir: path to the input directory to traverse
    :param output_dir: path to the output directory to write the modified CSS files
    """
    # This function is a placeholder and currently does nothing
    pass


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

    for file in files:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            # Write the contents of the uploaded file to the temporary file
            shutil.copyfileobj(file.file, tmp)
            # Extract the uploaded zip file to the input_files directory
            with zipfile.ZipFile(tmp.name, 'r') as zip_ref:
                zip_ref.extractall(input_location)
        os.unlink(tmp.name)


def process_project(input_dir, output_dir):
    if input_dir == output_dir:
        raise ValueError(
            "Input directory and output directory cannot be the same.")
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    process_files(input_dir, output_dir)
