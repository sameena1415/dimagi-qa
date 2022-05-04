import pandas as pd

from NYperformance.WorkflowActions.base.decorators import header_load_time, header_workflow, first_dump_filename

""""Contains data manipulation actions"""


def avg_of(workflow):
    data = pd.read_csv(first_dump_filename)
    workflow_datframe = data.loc[data[header_workflow] == workflow]
    print('\nResult dataframe :\n', workflow_datframe)
    load_time_mean = workflow_datframe.loc[:, header_load_time].mean()
    print("Mean load time of:", workflow, "is:", load_time_mean)
    return round(load_time_mean, 2)


def round_(workflow, _round_):
    try:
        data = pd.read_csv(first_dump_filename)
        workflow_datframe = data.loc[data[header_workflow] == workflow]
        load_time = workflow_datframe[header_load_time].values[_round_]
        return round(load_time, 2)
    except IndexError:
        print("Not run")


def write_readings_for(workflow):
    first_run = 0
    second_run = 1
    third_run = 2
    list_ = [workflow,
             round_(workflow, first_run),
             round_(workflow, second_run),
             round_(workflow, third_run),
             avg_of(workflow)]
    return list_
