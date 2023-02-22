import cssutils
import logging
from color_contrast import getValidColor
cssutils.log.setLevel(logging.CRITICAL)


def get_new_colors(color, background_color):
    return getValidColor(color,background_color)


def get_css_rules(css_file_path):
    """
    Returns a list of CSSStyleRule objects from the given CSS file.
    """
    sheet = get_parsed_css(css_file_path)
    return [rule for rule in sheet if isinstance(rule, cssutils.css.CSSStyleRule)]


def get_parsed_css(css_file_path):
    """
    Parses the given CSS file and returns a CSSStyleSheet object.
    """
    with open(css_file_path, "r") as f:
        css_text = f.read()
        return cssutils.parseString(css_text)


def write_css_rules_to_file(css_rules, css_file_path):
    # Create a new CSSStyleSheet object
    stylesheet = cssutils.css.CSSStyleSheet()

    # Add the CSSStyleRule objects to the stylesheet
    for rule in css_rules:
        stylesheet.add(rule)

    # Serialize the stylesheet into CSS text
    css_text = stylesheet.cssText.decode('utf-8')  # convert bytes to string

    # Write the CSS text to the file
    with open(css_file_path, 'w') as f:
        f.write(css_text)


def replace_css_colors(css_file_path, output_file):
    """
    Replaces the "color" and "background-color" properties in the given CSS file with new colors returned by
    another function.
    """
    css_rules = get_css_rules(css_file_path)
    for rule in css_rules:
        # Check if the rule has both "color" and "background-color" properties
        if "color" in rule.style.cssText and "background-color" in rule.style.cssText:
            # Extract the current colors from the rule
            current_colors = {
                "color": rule.style.getPropertyValue("color"),
                "background-color": rule.style.getPropertyValue("background-color")
            }
            # Call another function to get the new colors
            new_colors = get_new_colors(
                current_colors["color"], current_colors["background-color"])
            # If the new colors are different, update the rule with the new colors
            if new_colors["color"] != current_colors["color"] or new_colors["background-color"] != current_colors["background-color"]:
                rule.style.setProperty("color", new_colors["color"])
                rule.style.setProperty(
                    "background-color", new_colors["background-color"])

    # Write the updated CSS file
    write_css_rules_to_file(css_rules, output_file)


def update_css_colors(css_file_path, objects):
    # Get the CSS rules from the file
    css_rules = get_css_rules(css_file_path)

    # Iterate over the objects and update the CSS rules
    for obj in objects:
        # Find the CSS rule with the matching class name
        for rule in css_rules:
            if rule.selectorText == obj['selector']:
                # Update the color and background-color properties
                rule.style.setProperty('color', obj['color'], '')
                rule.style.setProperty(
                    'background-color', obj['background-color'], '')

    # Write the updated CSS rules back to the file
    write_css_rules_to_file(css_rules, css_file_path)


# css_file_path = "test.css"
# # replace_css_colors(css_file_path)
# update_css_colors(css_file_path, [
#                   {'selector': '.navbar', 'color': '#123', 'background-color': "#456"}])


