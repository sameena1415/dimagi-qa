import csv
import datetime
import pandas as pd

def read_owner_id(loc):

    #reading values from input CSV file and storing in a dictionary
     with open(loc) as f:
        next(f)  # Skip the header
        inputCSV = csv.reader(f, skipinitialspace=True)
        owner_dict = dict(inputCSV)

    #converting the dictionary values from string to int
     for owner in owner_dict:
        owner_dict[owner] = int(owner_dict[owner])

    #returning the final dictionary to the main program
     return owner_dict

def write_ids_to_csv(instance_id_list,output_path,output_filename):
    ## function to generate the instance_ids and write them to the input csv file
    filename=''
    if output_filename == None:
        filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

        with open(output_path+'/InstanceID_'+filename+'.csv', 'w', newline='') as csvfile: #creating the output files
           #defining the headers
            fieldnames = ['instance_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            #writing the header to the files
            writer.writeheader()

            for instances in instance_id_list:
                writer.writerow({'instance_id':instances})

    else:
        filename=output_filename
        sample = pd.read_csv(output_path +'/'+ filename+'.csv')
        sample['instance_id'] = instance_id_list
        sample.drop(sample.filter(regex="Unname"), axis=1, inplace=True)
        sample.to_csv(output_path +'/'+ filename+'.csv', index=False)

    print('Instance_IDs.csv successfully generated.')

def delete_empty_vaccine_rows(output_path):
    # remove blank vaccine_complete rows
    response_list = pd.read_csv(output_path + '/JSON_Response.csv')
    response_list=response_list.dropna(subset=['vaccines_completed'])
    response_list.to_csv(output_path + '/JSON_Response.csv',index=False)

def group_by_owners(owners,output_path):

    response_list = pd.read_csv(output_path + '/JSON_Response.csv')
    dict_item={}

    for owner in owners:
        actual_count=len(response_list[response_list['owner_id'] == owner])
        dict_item[owner] = actual_count-round(actual_count*0.3)

    column_list=list(response_list.columns)
    for owner in owners:
        n=dict_item[owner]
        result1=response_list.groupby("owner_id", as_index=False).apply(lambda x: x.iloc[:-n])
        #result1 = response_list.drop(response_list.groupby('owner_id').tail(dict_item[owner]), axis=0, inplace=True)

    result1.to_csv(output_path + '/JSON_Response_filtered.csv', index=False)

def add_owners_to_csv(owner_dict,owner_list,output_path):
    filename='Form_Input_VSM'
    with open(output_path + '/'+filename+'.csv', 'w',
              newline='') as csvfile:  # creating the output files
        # defining the headers
        fieldnames = ['owner_id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # writing the header to the files
        writer.writeheader()
        for owners in owner_list:
            count=owner_dict[owners]

            for n in range(count):
                writer.writerow({'owner_id': owners})

    return filename


