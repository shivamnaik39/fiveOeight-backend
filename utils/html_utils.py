from bs4 import BeautifulSoup
import os
import urllib.parse
from model.get_alt import get_alt
from utils.video_utils import transcribe_audio

# Load the HTML file into a BeautifulSoup object.


def get_soup(input_file_path):
    with open(input_file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser', format=None)

    return soup

# Modify the attributes of elements in the HTML.


def modify_elements_attributes(soup, elements):
    """
    Modify the attributes of elements in the HTML.

    :param soup: The BeautifulSoup object.
    :param elements: A list of elements to modify. Each element should be a dictionary with 'name' and 'attributes' keys.
    """
    # Loop over the elements
    for element in elements:
        # Find all elements in the HTML that match the selector
        elems = soup.select(element['name'])
        # Check if any elements were found
        if elems:
            # Loop over the elements
            for elem in elems:
                # Loop over the expected attributes
                for attr_name, attr_value in element['attributes'].items():
                    # Replace the attribute if it exists, or add it if it doesn't
                    elem[attr_name] = attr_value

    return soup


# Convert deprecated HTML tags to span tags.
def convert_deprecated_tags(soup, deprecated_tags):
    """
    Convert deprecated HTML tags to span tags.

    :param soup: The BeautifulSoup object.
    :param deprecated_tags: A list of deprecated HTML tags.
    """
    # Create a queue to store the elements that need to be processed
    elem_queue = soup.find_all(deprecated_tags)
    # Loop until the queue is empty
    while elem_queue:
        # Pop an element from the queue
        elem = elem_queue.pop()
        # Replace the deprecated tag with a span tag
        span = soup.new_tag('span')
        span.attrs = elem.attrs
        span.contents = elem.contents
        elem.replace_with(span)
        # Add any children of the replaced element to the queue
        try:
            elem_queue.extend(span.find_all(deprecated_tags))
        except AttributeError:
            pass

    return soup


def extract_image_names(soup):
    """
    This function takes in an HTML document as a string and returns a modified version of the HTML document
    with the `alt` attribute set to the name of the image from the `src` attribute.
    """
    tmp = {"img-alt": []}
    changes = tmp['img-alt']
    # Find all the img tags in the HTML document
    images = soup.find_all('img')
    # Loop through each img tag
    for img in images:
        # Get the src attribute
        src = img.get('src')

        # Use urllib.parse.urlsplit to split the src into components
        # and extract the path component
        # path = urllib.parse.urlsplit(src).path

        # Use os.path.basename to extract the file name from the path
        # filename = os.path.basename(path)

        if not img.has_attr('alt'):
            # Set the alt attribute to the file name
            new_alt = get_alt(src)
            line_number = img.sourceline
            issue = "img tag missing alt attribute"
            old_value = img.get('alt')
            new_value = new_alt
            img['alt'] = new_alt
            change = {'sourceline': line_number, 'selector': 'img[src="{0}"]'.format(
                src), 'old_value': old_value, 'new_value': new_value, "issue": issue}
            changes.append(change)

    return soup, tmp


def add_name_and_label(soup):
    """
    Add name and label to input elements if they are missing
    """
    # Find all input elements in the soup object
    inputs = soup.find_all("input")

    # Iterate over all the input elements
    for input_element in inputs:
        # Get the value of "id" attribute of the input element
        id_value = input_element.get("id")
        if id_value:
            # Get the value of "name" attribute of the input element
            name_value = input_element.get("name")
            # If "name" attribute is missing, add "name" attribute with the same value as "id"
            if not name_value:
                input_element["name"] = id_value
            # If there's no label with "for" attribute matching the "id" of the input element, create a new label
            if not soup.find("label", {"for": id_value}):
                new_label = soup.new_tag("label")
                new_label["for"] = id_value
                new_label.string = id_value
                # Insert the new label before the input element
                input_element.insert_before(new_label)

    return soup


def add_alt_to_anchor_tags(soup):
    """
    This function takes in an HTML document as a string and adds an `alt` attribute to any anchor tags that don't
    already have one. The value of the `alt` attribute is set to the text content of the anchor tag, if present,
    or the value of the `href` attribute if the text is not present or not in a readable format.
    """

    # Find all the anchor tags in the HTML document
    anchors = soup.find_all('a')
    # Loop through each anchor tag
    for anchor in anchors:
        # Check if the anchor tag already has an alt attribute
        if anchor.has_attr('title'):
            continue

        # Get the text content of the anchor tag
        text = anchor.get_text().strip()
        if not text or not text.isprintable():
            # Extract title from the href attribute if the text is not present or not in a readable format
            href = anchor.get('href', '')
            title = os.path.basename(href)
        else:
            # Use the text content as the title attribute if present and in a readable format
            title = text

        # Set the title attribute to the value determined above
        anchor['title'] = title

    return soup


def add_lang_attr(soup, lang="en"):
    """
    This function takes in a BeautifulSoup object and a language code (defaulting to "en") and adds a `lang`
    attribute to the <html> element if it does not already have one.
    """
    # Find the <html> tag
    html_tag = soup.find('html')

    # Check if the <html> tag exists
    if html_tag is None:
        return soup

    # Check if the <html> tag already has a lang attribute
    if html_tag.has_attr('lang'):
        return soup

    # Add the lang attribute to the <html> tag with the specified language code
    html_tag['lang'] = lang

    return soup


def process_video(soup, input_file_path, output_file_path):
    # find the first video element in the soup object
    video = soup.find('video')
    print(f"Video: {video}")
    if video:
        # get the src attribute of the source element within the video element
        video_src = video.find('source')['src']
        final_path = join_paths(input_file_path, video_src)
        # call the function with the video source URL
        output_path = join_paths(output_file_path, video_src)
        processed_src = transcribe_audio(final_path, output_path)

        # add a track element to the video element with the processed URL
        video_name = os.path.basename(video_src)
        track_src = os.path.splitext(video_name)[0] + '.srt'
        print(track_src)
        track = soup.new_tag('track', src=track_src,
                             kind='captions', srclang='en')
        video.append(track)

    return soup


def join_paths(html_path, video_path):
    # Normalize the paths
    html_path = os.path.normpath(html_path)
    video_path = os.path.normpath(video_path)

    # Get the directory of the HTML file
    html_dir = os.path.dirname(html_path)

    # Join the directory of the HTML file with the relative video path
    abs_video_path = os.path.join(html_dir, video_path)

    # Normalize the resulting path
    abs_video_path = os.path.normpath(abs_video_path)

    return abs_video_path
