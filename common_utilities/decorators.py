import csv
import functools
import os
import time

from common_utilities.path_settings import PathSettings

header_workflow = 'workflow'
header_load_time = 'load_time'
header_username = 'username'
header_app = 'application'
first_dump_filename = os.path.abspath(os.path.join(PathSettings.BASE_DIR, "reading.csv"))


def timer(func):
    """This function captures the execution time of the function object passed and writes the readings to a csv"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):

        """Capture the execution time of the function"""

        start_time = time.perf_counter()  # Start capturing time
        result = func(*args, **kwargs)  # Run workflow
        print(func.__name__, kwargs)
        end_time = time.perf_counter()  # Stop capturing time
        run_time = end_time - start_time
        print(f'Function {func.__name__!r} executed in {run_time :.2f}s')

        """Write the readings to csv"""

        file_exists = os.path.isfile(first_dump_filename)
        with open(first_dump_filename, 'a', newline='') as csvfile:
            fieldnames = [header_workflow, header_load_time, header_username, header_app]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            try:
                writer.writerow({header_workflow: func.__name__, header_load_time: run_time,
                                 header_username: kwargs["username"], header_app: kwargs["application_name"]})
            except:
                writer.writerow({header_workflow: func.__name__, header_load_time: run_time})

        return result

    return wrapper_timer
