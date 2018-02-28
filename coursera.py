import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


def get_courses_list():
    number_of_courses = 1
    courses_list_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    response_xml = requests.get(courses_list_url).content.decode()

    xml_page = BeautifulSoup(response_xml, 'xml')

    courses_urls = []
    for num, loc in enumerate(xml_page.find_all('loc')):
        if num < number_of_courses:
            courses_urls.append(loc.text)
    return courses_urls


def get_course_info(course_url):
    course_page_html = requests.get(course_url).content.decode()
    course_soup = BeautifulSoup(course_page_html, 'lxml')

    course_name = course_soup.find(attrs={'class': 'course-title'}).text
    course_lang = course_soup.find(attrs={
        'class': 'rc-Language'}).text.split()[0]
    start, month, day = course_soup.find(attrs={
        'class': 'startdate'}).text.split()
    course_startdate = '{} {}'.format(month, day)
    course_duration = course_soup.find_all(attrs={
        'class': 'td-data'})[1].text
    course_rating = course_soup.find(attrs={
        'class': 'ratings-text'}).text.split()[0]
    return [
        course_name,
        course_lang,
        course_startdate,
        course_duration,
        course_rating
    ]


def output_courses_info_to_xlsx(path_to_output_xlsx, courses_info_list):
    wb = Workbook()
    ws = wb.active

    for course in courses_info_list:
        ws.append(course)

    wb.save(path_to_output_xlsx)


if __name__ == '__main__':
    path_to_output_xlsx = 'courses_info.xlsx'

    courses_url_list = get_courses_list()
    courses_info_list = []
    for course in courses_url_list:
        courses_info_list.append(get_course_info(course))
