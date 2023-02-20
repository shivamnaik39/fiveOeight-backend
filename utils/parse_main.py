import os
import shutil
from file_utils import process_files


def main(input_dir, output_dir):
    """
    Main function to process HTML and CSS files.

    :param input_dir: path to the input directory to traverse
    :param output_dir: path to the output directory to write the modified files
    """
    if input_dir == output_dir:
        raise ValueError(
            "Input directory and output directory cannot be the same.")
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    process_files(input_dir, output_dir)


if __name__ == '__main__':
    input_dir = 'angular-demo'
    output_dir = 'modified'
    main(input_dir, output_dir)
