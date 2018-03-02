from random import sample
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


def get_page_from_coursera(url):
    coursera_page = requests.get(url).content.decode()
    return coursera_page


def get_random_courses_url_list(xml_courses_page, number_of_courses):
    xml_course_soup = BeautifulSoup(xml_courses_page, 'xml')

    full_courses_urls = []
    for loc in xml_course_soup.find_all('loc'):
        full_courses_urls.append(loc.text)

    random_courses_urls = sample(full_courses_urls, number_of_courses)

    return random_courses_urls


def get_course_info(html_course_page):
    course_soup = BeautifulSoup(html_course_page, 'lxml')

    course_name = course_soup.find(attrs={'class': 'course-title'}).text

    course_lang = course_soup.find(
        attrs={'class': 'rc-Language'},
    ).text.split(',')[0]

    course_startdate = course_soup.find(attrs={'class': 'startdate'}).text

    course_duration = '{} weeks'.format(
        len(course_soup.find_all('div', attrs={'class': 'week-heading'})))

    try:
        course_rating = course_soup.find(attrs={'class': 'ratings-text'}).text
    except AttributeError:
        course_rating = None

    return {
        'course_name': course_name,
        'course_lang': course_lang,
        'course_startdate': course_startdate,
        'course_duration': course_duration,
        'course_rating': course_rating,
    }


def output_courses_info_to_xlsx(courses_info_list):
    wb = Workbook()
    ws = wb.active

    headers = [
        'Course name',
        'Language',
        'Start date',
        'Course duration',
        'Course rating',
    ]
    ws.append(headers)

    for course in courses_info_list:
        current_course = [
            course['course_name'],
            course['course_lang'],
            course['course_startdate'],
            course['course_duration'],
            course['course_rating'],
        ]
        ws.append(current_course)

    return wb


if __name__ == '__main__':
    courses_list_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    number_of_courses = 20
    path_to_output_xlsx = 'courses_info.xlsx'

    xml_courses_page = get_page_from_coursera(courses_list_url)

    courses_url_list = get_random_courses_url_list(
        xml_courses_page,
        number_of_courses,
    )

    courses_info_list = []
    for course_url in courses_url_list:
        courses_info_list.append(get_course_info(
            get_page_from_coursera(course_url)))

    current_workbook = output_courses_info_to_xlsx(courses_info_list)
    current_workbook.save(path_to_output_xlsx)
