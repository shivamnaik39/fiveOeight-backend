from bs4 import BeautifulSoup
import cssutils
from utils.css_utils import write_css_rules_to_file, get_css_rules


def update_data(data):
    # Process img_alt data for HTML files
    for filepath, value in data["img_alt"].items():
        # Call the process_html function for each filepath
        modified_path = get_modified_path(filepath)
        update_html(modified_path, value["img-alt"])

    # Process color_contrast data for CSS files
    for filepath, value in data["color_contrast"].items():
        # Call the process_css function for each filepath
        modified_path = get_modified_path(filepath)
        update_css(modified_path, value)


def update_html(filepath, img_alt_list):
    # Function to process img-alt data for HTML files
    # Here, we'll use Beautiful Soup to update the HTML file
    # Open the HTML file using the given filepath
    with open(filepath, 'r') as f:
        html = f.read()

    # Create a BeautifulSoup object from the HTML file
    soup = BeautifulSoup(html, 'html.parser')

    # Iterate over each img-alt object in the img_alt_list
    for img_alt_obj in img_alt_list:
        # Get the src url from the selector of the img-alt object
        src_url = img_alt_obj['selector'].split('"')[1]
        # Find all img tags with the src attribute equal to the src_url
        img_tags = soup.find_all('img', {'src': src_url})

        # If img tags are found, update their alt attributes
        if img_tags:
            for img_tag in img_tags:
                img_tag['alt'] = img_alt_obj['new_value']

    # Write the updated HTML back to the file
    with open(filepath, 'w') as f:
        f.write(str(soup))


def update_css(filepath, color_contrast_list):
    # Function to process color-contrast data for CSS files
    # Here, you can write your code to process the color-contrast data for the given filepath
    # Get the CSS rules from the file
    css_rules = get_css_rules(filepath)

    # Iterate over the objects and update the CSS rules
    for obj in color_contrast_list:
        # Find the CSS rule with the matching class name
        for rule in css_rules:
            if rule.selectorText == obj['selector']:
                # Update the color and background-color properties
                rule.style.setProperty(
                    'color', obj['suggested_colors']['color'], '')

                rule.style.setProperty(
                    'background-color', obj['suggested_colors']['background-color'], '')

    # Write the updated CSS rules back to the file
    write_css_rules_to_file(css_rules, filepath)


def get_modified_path(filepath):
    # Split the filepath by '\\' separator to get individual directories and filename
    directories, filename = filepath.rsplit('\\', 1)

    # Add the "downloads" directory at the beginning of the directories list
    directories = ["downloads"] + directories.split('\\')
    # Modify the first directory to add "_modified" suffix
    directories[1] = directories[1] + "_modified"

    # Join the directories list and filename using '\\' separator to form the final filepath
    modified_filepath = "\\".join(directories) + "\\" + filename

    return modified_filepath
