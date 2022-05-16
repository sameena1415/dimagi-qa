import pandas as pd

from NYperformance.WorkflowActions.base.decorators import header_load_time, \
    header_workflow, header_username, header_app, first_dump_filename


def filter_data(workflow, application_name, username):
    data = pd.read_csv(first_dump_filename)
    workflow_dataframe = data.loc[(data[header_workflow] == workflow) &
                                  (data[header_username] == username) &
                                  (data[header_app] == application_name)]
    print('\nResult dataframe :\n', workflow_dataframe)
    return workflow_dataframe


def avg_of(workflow, application_name, username):
    filtered_dataframe = filter_data(workflow, application_name, username)
    load_time_mean = filtered_dataframe.loc[:, header_load_time].mean()
    print("Mean load time of:", workflow, "is:", load_time_mean)
    return round(load_time_mean, 2)


def round_(workflow, application_name, username, _round_):
    try:
        filtered_dataframe = filter_data(workflow, application_name, username)
        load_time = filtered_dataframe[header_load_time].values[_round_]
        return round(load_time, 2)
    except IndexError:
        print("Not run")


def write_readings_for(workflow, application_name, username,):
    first_run = 0
    second_run = 1
    third_run = 2
    list_ = [workflow,
             round_(workflow, application_name, username, first_run),
             round_(workflow, application_name, username, second_run),
             round_(workflow, application_name, username, third_run),
             avg_of(workflow, application_name, username)]
    return list_
