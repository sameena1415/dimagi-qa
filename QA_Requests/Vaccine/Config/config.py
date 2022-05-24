class TestData:
    # scenario_type="household"
    # input_file_path="./InputFiles/Household.csv"
    # output_path="./OutputFiles/Household"

    #scenario_type="person"
    # input_file_path="./InputFiles/Person.csv"
    # output_path="./OutputFiles/Person"
    #

    ## input values for household and person forms
    ### scenario types can be either "household" or "person" or "household_and_person"
    #scenario_type = "household_and_person"
    input_file_path1 = "./InputFiles/Household.csv"
    input_file_path2 = "./InputFiles/Person.csv"
    output_path1 = "./OutputFiles/Household"
    output_path2 = "./OutputFiles/Person"

    ### input values for Community Counselling Form submission ###
    #scenario_type = "CommunityCounsellingForm"
    # input_xml_path = "./InputFiles/input_sample.xml"
    # input_file_path = "./InputFiles/Form_InputData.csv"
    # output_path = "./OutputFiles/Forms"

    # CC_API_URL = "https://www.commcarehq.org/a/dimagi-vaccine-solution/receiver/9d022bfecb6b402a9bfa84ebee73e204/"
    # myHeader= {'Content-Type': 'application/xml'}
    # credentials = '@dimagi-vaccine-solution.commcarehq.org'
    # name='demo_data_va'
    # password='123'

    ### input values for Adverse Events Form submission ###
   #  scenario_type = "AdverseEventsForm"
   #  input_xml_path = "./InputFiles/Adverse_Event_Sample.xml"
   #  input_file_path = "./InputFiles/Adverse_Event_Input.csv"
   #  output_path = "./OutputFiles/AdverseEvents"
   #  AE_API_GET_URL = "https://www.commcarehq.org/a/dimagi-vaccine-solution/api/v0.5/case/?type=person&owner_id="
   #  AE_API_POST_URL = "https://www.commcarehq.org/a/dimagi-vaccine-solution/receiver/9d022bfecb6b402a9bfa84ebee73e204/"
   # # API_KEY ="9bf02e988d3dcfa10658357a4d6f4baab6b4f43b"
   #  API_KEY = "9260208c7ac754a111250618dac15267c923c416"
   #  UserName= "kbordoloi@dimagi.com"
   #  AE_GET_Header={'Authorization': 'application/xml'}
   #  myHeader = {'Content-Type': 'application/xml'}
   #  name = 'demo_data_va'
   #  password = '123'
   #  credentials = '@dimagi-vaccine-solution.commcarehq.org'

    ###for vaccine stock management
    scenario_type = "VaccineStockManagement"
    input_xml_path = "./InputFiles/Vaccine_Stock_Sample.xml"
    input_file_path = "./InputFiles/Vaccine_Stock_Management.csv"
    output_path = "./OutputFiles/VaccineStockManagement"
    credentials = '@dimagi-vaccine-solution.commcarehq.org'
    VSM_API_POST_URL = "https://www.commcarehq.org/a/dimagi-vaccine-solution/receiver/9d022bfecb6b402a9bfa84ebee73e204/"
    myHeader = {'Content-Type': 'application/xml'}
    name = 'demo_data_va'
    password = '123'


