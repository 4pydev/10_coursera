import requests
from bs4 import BeautifulSoup


def get_courses_list():
    courses_list_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    response_xml = requests.get(courses_list_url).content.decode()

    xml_page = BeautifulSoup(response_xml, 'xml')

    courses_urls = []
    for num, loc in enumerate(xml_page.find_all('loc')):
        if num < 20:
            courses_urls.append(loc.text)
    return courses_urls


def get_course_info(course_slug):
    pass


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    print(get_courses_list())
