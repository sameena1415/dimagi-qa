import csv
import os
import names
import pytest

from QA_Requests.MultiSelectPerf.hq_workflows import AppCreationPage
from common_utilities.import_data_using_api import post_import_cases_from_excel


def generate_path(output_path):
    if not os.path.isdir(output_path):
        print('Path not present')
        os.mkdir(output_path)


def generate_import_file(case_load_per_case_type, case_type_name, num_prop):
    OUTPUT_PATH = "OutputFiles/"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    generate_path(os.path.abspath(os.path.join(BASE_DIR, OUTPUT_PATH)))
    file = os.path.abspath(os.path.join(BASE_DIR, OUTPUT_PATH + f'{str(case_type_name)}.csv'))
    col_list = ["caseid", "name"] + ['prop{}p'.format(i) for i in range(0, num_prop)]
    with open(file, 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=col_list)
        writer.writeheader()
        for cases in range(0, int(case_load_per_case_type)):
            value_list = ["", names.get_full_name()] + ['val{}'.format(i) for i in range(0, num_prop)]
            dic = dict(zip(col_list, value_list))
            writer.writerow(dic)
        return file


"""This function is a one time script to create desired load on a domain. Call the function to run it"""


def multi():
    domain_case_load = 100
    case_types_and_properties = {"case1": 50, "case2": 100, "case3": 200}
    case_load_per_case_type = domain_case_load / len(case_types_and_properties)
    for case_type, prop_count in case_types_and_properties.items():
        file = generate_import_file(case_load_per_case_type, case_type, prop_count)
        print(case_type, prop_count, "generated")
        post_import_cases_from_excel(file, case_type, './settings.cfg')
        print(file, case_type, "uploaded")


"""This function is a one time script to pass properties into forms depepending on user defined load"""

# def test_pass_prop_to_form(driver):
#     print("Add property to form for all case types")
#     create = AppCreationPage(driver)
#     form = "https://www.commcarehq.org/a/casesearch/apps/view/e2373071215846318db147ca6ea88e69/form/c9260fe2bf244099b067556d73c111a4/source/#form/here_are_your_cases/item/prop_name_prop98p"
#     create.pass_prop_to_case_list(form, 101, 200)


"""Capture sync time"""


def test_first_sync(driver):
    create = AppCreationPage(driver)
    create.sync_user()


"""Capture timing for the variious  actions for various menu, with different case-per-page load"""


@pytest.mark.parametrize("pages", ["10", "25", "50", "100"])
@pytest.mark.parametrize("menus", ['Case1 - (multi select, normal)', 'Case2 - (multi select, normal)',
                                   'Case3 - (multi select, normal)', 'Case1 - (multi select, search-first)',
                                   'Case2 - (multi select, search-first)', 'Case3 - (multi select, search-first)'])
def test_multiselect_perf(driver, pages, menus):
    create = AppCreationPage(driver)
    print(pages, menus)
    create.open_app()
    create.open_case_list_menu(menus)
    create.search_all_cases()
    create.search_all_cases_on_case_search_page()
    create.change_page_number(pages)
    create.switch_bw_pages()
    create.omni_search("val0")
    create.omni_results()
    create.multi_select_cases()
    create.open_and_load_form()
    create.submit_the_form()
