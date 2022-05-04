import csv
import functools
import os
import time

from NYperformance.UserInputs.user_inputs import UserData

header_workflow = 'workflow'
header_load_time = 'load_time'
first_dump_filename = os.path.abspath(os.path.join(UserData.BASE_DIR, "NY_reading.csv"))


def timer(func):

    """This function captures the execution time of the function object passed and writes the readings to a csv"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):

        """Capture the execution time of the function"""

        start_time = time.perf_counter()  # Start capturing time
        result = func(*args, **kwargs)  # Run workflow
        end_time = time.perf_counter()  # Stop capturing time
        run_time = end_time - start_time
        print(f'Function {func.__name__!r} executed in {run_time :.2f}s')

        """Write the readings to csv"""

        file_exists = os.path.isfile(first_dump_filename)
        with open(first_dump_filename, 'a', newline='') as csvfile:
            fieldnames = [header_workflow, header_load_time]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({header_workflow: func.__name__, header_load_time: run_time})

        return result

    return wrapper_timer
