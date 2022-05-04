import csv
import xml.etree.ElementTree as ET
from DataGeneration.Vaccine.Tests.RandomFormValueGenerator import *
from DataGeneration.Vaccine.Tests.APITests import post_form_API
from DataGeneration.Vaccine.Config.config import TestData


def create_forms(output_path, input_xml,owner,form_counts,instance_id_list):
    tree = ET.parse(input_xml)
    root = tree.getroot()

    XML_TEMPLATE = ET.tostring(root, encoding='unicode')

    ## code to remove namespaces
    #it = ET.iterparse(input_xml)
    # for _, el in it:
    #     if '}' in el.tag:
    #         el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
    #     for at in list(el.attrib.keys()):  # strip namespaces of attributes too
    #         if '}' in at:
    #             newat = at.split('}', 1)[1]
    #             el.attrib[newat] = el.attrib[at]
    #             del el.attrib[at]
    # myroot = it.root

    for form_index in range(form_counts):

            # generating the data
            event_session=event_session_date_generator()
            counselling=counselling_type()
            sessionparticipant=session_participants()
            eventtopic=event_topic()
            reasonsantivaccine=reasons_antivaccine()
            feedback=session_feedback()
            beneficiary_vaccination_centre_id=owner
            instance=instance_id_list.pop(0) if instance_id_list else False
            xml_string = XML_TEMPLATE.format(event_session=event_session,counselling=counselling,
                                       sessionparticipant=sessionparticipant,eventtopic=eventtopic,
                                       reasonsantivaccine=reasonsantivaccine,feedback=feedback,
                                       beneficiary_vaccination_centre_id=beneficiary_vaccination_centre_id,
                                       instance=instance)

            # calling API Post method
            result=post_form_API(xml_string, TestData.CC_API_URL)

            #writing responses to csv file
            with open(output_path + '/Responses.csv', 'a+', newline='') as csvfile:
                writer = csv.writer(csvfile)
                list_response=[beneficiary_vaccination_centre_id, instance,result]
                writer.writerow(list_response)
            print(instance, result)

def create_adverse_events_forms(output_path, input_xml):
    tree = ET.parse(input_xml)
    root = tree.getroot()

    XML_TEMPLATE = ET.tostring(root, encoding='unicode')
    with open(output_path+'/JSON_Response_filtered.csv', 'r') as read_obj:

        csv_dict_reader = csv.DictReader(read_obj)
        for row in csv_dict_reader:
            se_injection_site_swell = se_fever = se_nausea = se_diarrhea = se_loss_of_taste = se_breathing_difficulty = se_other=''
            case_id=row['case_id']
            vaccination_centre_id=row['owner_id']
            all_conditional_vaccines=row['all_conditional_vaccines']
            dob=date_format(row['dob'])
            date_of_registration=row['date_of_registration']
            vaccines_completed=row['vaccines_completed']
            side_effect_dose_name=side_effect_dose_name_generator(vaccines_completed)
            has_adverse_side_effect='yes'
            side_effects_reported_date=side_effects_reported_date_generator(date_of_registration)
            side_effects=row['side_effects']

            if side_effects=='se_injection_site_swell':
                se_injection_site_swell='yes'
                se_fever= se_nausea= se_diarrhea= se_loss_of_taste= se_breathing_difficulty= se_other=''
            elif side_effects=='se_fever':
                se_fever='yes'
                se_injection_site_swell=se_nausea= se_diarrhea= se_loss_of_taste= se_breathing_difficulty= se_other = ''
            elif side_effects=='se_nausea':
                se_nausea='yes'
                se_injection_site_swell= se_fever= se_diarrhea= se_loss_of_taste=se_breathing_difficulty= se_other = ''
            elif side_effects=='se_diarrhea':
                se_diarrhea='yes'
                se_injection_site_swell=se_fever= se_nausea= se_loss_of_taste= se_breathing_difficulty= se_other = ''
            elif side_effects=='se_loss_of_taste':
                se_loss_of_taste='yes'
                se_injection_site_swell=se_fever=se_nausea= se_diarrhea= se_breathing_difficulty= se_other = ''
            elif side_effects=='se_breathing_difficulty':
                se_breathing_difficulty='yes'
                se_injection_site_swell=se_fever= se_nausea= se_diarrhea= se_loss_of_taste= se_other = ''
            elif side_effects=='se_other':
                se_other='yes'
                se_injection_site_swell=se_fever=se_nausea= se_diarrhea= se_loss_of_taste= se_breathing_difficulty = ''
            side_effect_dose_received_date=side_effects_reported_date
            hospitalized_check='no'
            instance=row['instance_id']
            xml_string = XML_TEMPLATE.format(case_id=case_id, has_adverse_side_effect=has_adverse_side_effect,
                                             dob=dob, owner_id=vaccination_centre_id,
                                             side_effect_dose_name=side_effect_dose_name,
                                             side_effects_reported_date=side_effects_reported_date,
                                             se_injection_site_swell=se_injection_site_swell,se_fever=se_fever,
                                             se_nausea=se_nausea,se_diarrhea=se_diarrhea,
                                             se_loss_of_taste=se_loss_of_taste,
                                             se_breathing_difficulty=se_breathing_difficulty,se_other=se_other,
                                             side_effect_dose_received_date=side_effect_dose_received_date,
                                             hospitalized_check=hospitalized_check,instance=instance)
            # calling the API post method
            result=post_form_API(xml_string, TestData.AE_API_POST_URL)

            #writing response to csv file
            with open(output_path + '/Responses.csv', 'a+', newline='') as csvfile:
                writer = csv.writer(csvfile)
                list_response=[vaccination_centre_id, instance,result]
                writer.writerow(list_response)
            print(instance, result)

            # code to write xml string to xml files
            # with open(output_path + '/' + instance+'.xml', "wb") as f:
            #    f.write(xml_string.encode('UTF-8'))
            #tree.write(output_path + '/' +instance+'.xml',default_namespace=None)
            #print(owner+'_'+str(form_index)+'.xml created successfully.')


def create_vaccine_stock_forms(output_path, input_xml, filename):
    tree = ET.parse(input_xml)
    root = tree.getroot()

    XML_TEMPLATE = ET.tostring(root, encoding='unicode')
    with open(output_path+'/'+filename+'.csv', 'r') as read_obj:
        csv_dict_reader = csv.DictReader(read_obj)
        for row in csv_dict_reader:
            date_of_stock_input=date_of_stock_generator()
            report_potential_stockout_check=row['report_potential_stockout_check']
            report_oversupply_check=report_oversupply_check_generator(report_potential_stockout_check)
            vaccination_centre_id=row['owner_id']
            vaccine_name=vaccine_name_generator()
            vaccine_id=vaccine_id_generator(vaccine_name)
            instance=row['instance_id']
            xml_string = XML_TEMPLATE.format(date_of_stock_input=date_of_stock_input,
                                             report_potential_stockout_check=report_potential_stockout_check,
                                             report_oversupply_check=report_oversupply_check,
                                             vaccination_centre_id=vaccination_centre_id,
                                             vaccine_name=vaccine_name,vaccine_id=vaccine_id,
                                             instance=instance)

            # calling the API post method
            result=post_form_API(xml_string, TestData.VSM_API_POST_URL)

            # writing response to csv file
            with open(output_path + '/Responses.csv', 'a+', newline='') as csvfile:
                writer = csv.writer(csvfile)
                list_response=[vaccination_centre_id, instance,result]
                writer.writerow(list_response)
            print(instance, result)

            # code to write xml string to xml files
            # with open(output_path + '/' + instance+'.xml', "wb") as f:
            #    f.write(xml_string.encode('UTF-8'))
            #tree.write(output_path + '/' +instance+'.xml',default_namespace=None)
            #print(owner+'_'+str(form_index)+'.xml created successfully.')







