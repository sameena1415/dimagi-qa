import os

from common_utilities.path_settings import PathSettings


def generate_output_path():
    OUTPUT_PATH = "OutputFiles/"
    output_path = (os.path.abspath(os.path.join(PathSettings.BASE_DIR, OUTPUT_PATH)))
    print('Path not present')
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    print(output_path)
    return output_path
