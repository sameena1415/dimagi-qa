from random import choice, shuffle
import datetime
import random
import string
import re
import uuid
import pandas as pd

#function to randomly generate form values
def instance_id_generator(total_case_counts):
    id_set=set() #declaring an empty set to store the unique household names

    for i in range(total_case_counts): #loop to generate the household names
        # generating 5 charaters long alphanumeric household  names
        ids=str(uuid.uuid4())

        #adding prefix to the random string: HH_ for household and CL_ for person
        id_set.add(ids)
    return id_set

def event_session_date_generator():
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2021, 9, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def counselling_type():
    counselling_range = ['personal_counselling','household_counselling','group_counselling']
    return random.choice(counselling_range)

def session_participants():
    session_participants_range = ['pregnant_women','parents_of_children_0-6_years_old',
                                  'general_population','traditional_health_practitoners',
                                  'community_religious_leaders','community_mobilizers','ngo',
                                  'government_officials','other']
    return random.choice(session_participants_range)

def event_topic():
    event_topic_range = ['vaccine_hesitancy_counselling','combatting_covid-19_misconceptions',
                         'general_immunization_awareness','awareness_about_adverse_events','other']
    return random.choice(event_topic_range)

def reasons_antivaccine():
    reasons_antivaccine_range = ['eligibility_doubt','vaccine_risks_greater_than_disease','no_prevention',
                                 'safety_concerns','diseases_normal_part_of_development',
                                 'reluctance_of_family','side_effects_scare','misconception_on_ingredients',
                                 'multiple_vaccines_overload_immunity','no_faith_in_vaccines',
                                 'prefer_disease_immunization','other']

    return random.choice(reasons_antivaccine_range)

def session_feedback():
    session_feedback_range = ['Vaccine hesitancy high','Good response from parents',
                              'Condition of vaccine administration facilities poor',
                              'Lack of vaccine administration facilities',
                              'Vaccine hesitancy due to side-effects','Negative response towards vaccine',
                              'Lack of awareness about vaccination services',
                              'Schools used as vaccination sites',
                              'Vaccination facilities not available nearby','High demand, low supply of vaccines',
                              'Awareness campaigns frequently held','Healthcare workers not trained']
    feedback = random.choice(session_feedback_range)
    return feedback

def add_remaining_columns(owner_list, output_path):
    # response_list = pd.read_csv(output_path + '/JSON_Response_filtered.csv')
    final_df=pd.DataFrame()
    add_se_injection_site_swell(owner_list, output_path)
    add_se_fever(owner_list, output_path)
    add_se_nausea(owner_list, output_path)
    add_se_diarrhea(owner_list, output_path)
    add_se_loss_of_taste(owner_list, output_path)
    add_se_breathing_difficulty(owner_list, output_path)
    add_se_other(owner_list, output_path)

    populated_response_list=pd.read_csv(output_path + '/List_with_other.csv')
    populated_response_list=populated_response_list.drop(populated_response_list.columns[[0, 1, 2,3,4,5]],
                       axis = 1)
    populated_response_list.to_csv(output_path + '/JSON_Response_filtered_populated.csv', index=False)

def add_side_effects(owner_list, output_path):
    sample = pd.read_csv(output_path + '/JSON_Response_filtered.csv')
    total = sample.shape[0]
    choice_range=['se_injection_site_swell','se_fever','se_nausea','se_diarrhea','se_loss_of_taste','se_breathing_difficulty','se_other']
    side_effects = random.choices(choice_range, weights=[20, 20, 20, 10, 10, 10, 10], k=total)
    sample['side_effects'] = side_effects
    sample.drop(sample.filter(regex="Unname"),axis=1, inplace=True)
    sample.to_csv(output_path+"/JSON_Response_filtered.csv", index=False)

def side_effect_dose_name_generator(all_conditional_vaccines):
    if all_conditional_vaccines=='Hepatitis B - Adult Covid-19(J&J)':
        vaccine='Hepatitis B - Adult Dose 3 Covid-19(J&amp;J) Dose 1'
    elif all_conditional_vaccines=='Tetanus Diptheria':
        vaccine='Tetanus Diptheria Dose 2'
    elif all_conditional_vaccines=='HPV Covid-19(Sinopharm)':
        vaccine='HPV Dose 2  Covid-19(Sinopharm) Dose 2'
    elif all_conditional_vaccines=='Tetanus Diptheria Booster':
        vaccine='Tetanus Diptheria Booster Dose'
    elif all_conditional_vaccines=='Covid-19(Astra Zeneca)':
        vaccine='Covid-19(Astra Zeneca) Dose 2'
    elif all_conditional_vaccines=='Covid-19(Covaxin)':
        vaccine='Covid-19(Covaxin) Dose 2'
    elif all_conditional_vaccines=='BCG':
        vaccine='BCG Dose 1'
    elif all_conditional_vaccines=='Hepatitis B - Infant':
        vaccine='Hepatitis B - Infant Dose 3'
    elif all_conditional_vaccines=='OPV DPT Hepatitis B - Infant':
        vaccine='OPV Dose 4  DPT Dose 3  Hepatitis B - Infant Dose 3'
    elif all_conditional_vaccines=='IPV (inactivated Polio Vaccine)':
        vaccine='IPV (inactivated Polio Vaccine) Dose 1'
    elif all_conditional_vaccines=='Haemophilus influenzae type b (Hib)':
        vaccine='Haemophilus influenzae type b (Hib) booster Dose 3'
    elif all_conditional_vaccines == 'Pneumococcal (Conjugate)':
        vaccine = 'Pneumococcal (Conjugate) booster Dose 3'
    elif all_conditional_vaccines == 'OPV':
        vaccine = 'OPV Dose 4'
    elif all_conditional_vaccines == 'Rotavirus':
        vaccine = 'Rotavirus Dose 3'
    elif all_conditional_vaccines == 'DPT':
        vaccine = 'DPT Dose 3'
    elif all_conditional_vaccines == 'Measles':
        vaccine = 'Measles Dose 2'
    elif all_conditional_vaccines == 'Rubella':
        vaccine = 'Rubella Dose 1'
    elif all_conditional_vaccines == 'DPT Booster':
        vaccine = 'DPT Booster Dose 3'
    elif all_conditional_vaccines == 'Japanese Encephalitis':
        vaccine = 'Japanese Encephalitis Dose 2'
    else:
        vaccine=""

    return vaccine


def date_format(date_old_format):
    try:
        new_date = datetime.datetime.strptime(date_old_format,"%Y-%m-%d").strftime("%Y-%m-%d")
    except:
        new_date = datetime.datetime.strptime(date_old_format, "%d-%m-%Y").strftime("%Y-%m-%d")
    print(new_date)
    return new_date

def side_effects_reported_date_generator(date_of_registration):
    try:
        reg_date = datetime.datetime.strptime(date_of_registration, "%d-%m-%Y").strftime("%Y-%m-%d")
    except:
        reg_date = datetime.datetime.strptime(date_of_registration, "%Y-%m-%d").strftime("%Y-%m-%d")
    # calculating side_effect_reported_date adding 10 days
    print(reg_date)
    side_effect_reported_date = datetime.datetime.strptime(reg_date, "%Y-%m-%d") + datetime.timedelta(days=10)
    side_effect_reported_date = datetime.datetime.strftime(side_effect_reported_date,"%Y-%m-%d")
    print(side_effect_reported_date)
    return side_effect_reported_date

def add_stockout_check_to_csv(output_path,filename):
    sample = pd.read_csv(output_path + '/'+filename+'.csv')
    total = sample.shape[0]
    choice_range = ['yes','no']
    stock = random.choices(choice_range, weights=[60,40], k=total)
    sample['report_potential_stockout_check'] = stock
    sample.drop(sample.filter(regex="Unname"), axis=1, inplace=True)
    sample.to_csv(output_path + '/'+filename+'.csv', index=False)

def date_of_stock_generator():
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2021, 9, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    print(random_date)
    return random_date

def report_oversupply_check_generator(report_potential_stockout_check):
    if report_potential_stockout_check=='yes':
        oversupply_check='no'
    else:
        oversupply_check= 'yes'

    return oversupply_check

def vaccine_name_generator():
    choice_range=['Hepatitis B - Adult','Tetanus Diptheria','Covid-19(Sinopharm)',
                  'Tetanus Diptheria Booster','Covid-19(Astra Zeneca)','Covid-19(Covaxin)',
                  'BCG','OPV','IPV (inactivated Polio Vaccine)','Haemophilus influenzae type b (Hib)',
                  'Pneumococcal (Conjugate)','Rotavirus','DPT','Measles','Rubella',
                  'DPT Booster','Japanese Encephalitis','Covid-19(J&amp;J)','Hepatitis B - Infant','DPT','HPV']

    vaccine_name=random.choice(choice_range)

    return vaccine_name

def vaccine_id_generator(vaccine_name):
    if vaccine_name == 'Hepatitis B - Adult':
        vaccine_id='hep_b_adult'
    elif vaccine_name == 'Tetanus Diptheria':
        vaccine_id ='td'
    elif vaccine_name == 'Covid-19(Sinopharm)':
        vaccine_id = 'covid_19_sinopharm'
    elif vaccine_name == 'Tetanus Diptheria Booster':
        vaccine_id = 'td_booster'
    elif vaccine_name == 'Covid-19(Astra Zeneca)':
        vaccine_id = 'covid_19_astrazeneca'
    elif vaccine_name == 'Covid-19(Covaxin)':
        vaccine_id = 'covid_19_covaxin'
    elif vaccine_name == 'BCG':
        vaccine_id = 'bcg'
    elif vaccine_name == 'OPV':
        vaccine_id = 'opv'
    elif vaccine_name == 'IPV (inactivated Polio Vaccine)':
        vaccine_id = 'ipv'
    elif vaccine_name == 'Haemophilus influenzae type b (Hib)':
        vaccine_id = 'hib'
    elif vaccine_name == 'Pneumococcal (Conjugate)':
        vaccine_id = 'pc'
    elif vaccine_name == 'Rotavirus':
        vaccine_id = 'rotavirus'
    elif vaccine_name == 'DPT':
        vaccine_id = 'dpt'
    elif vaccine_name == 'Measles':
        vaccine_id = 'measles'
    elif vaccine_name == 'Rubella':
        vaccine_id = 'rubella'
    elif vaccine_name == 'DPT Booster':
        vaccine_id = 'dpt_booster'
    elif vaccine_name == 'Japanese Encephalitis':
        vaccine_id = 'je'
    elif vaccine_name == 'Covid-19(J&amp;J)':
        vaccine_id = 'covid_19_jj'
    elif vaccine_name == 'Hepatitis B - Infant':
        vaccine_id = 'hep_b_infant'
    elif vaccine_name == 'HPV':
        vaccine_id = 'hpv'
    else:
        vaccine_id = ''

    return vaccine_id