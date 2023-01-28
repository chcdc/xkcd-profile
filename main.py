
'''
Readme With xkcd webcomic
'''
import sys
import traceback
import datetime
import requests


def xkcd_request():
    '''Gets API data and returns json'''
    try:
        request = requests.get("https://xkcd.com/info.0.json")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    resp_dict = request.json()
    return resp_dict


def update_readme(req):
    '''Generate a new Readme.md'''
    with open('README.md', 'r', encoding='utf-8') as file:
        readme = file.readlines()
    try:
        line_index = readme.index('<!-- xkcd -->\n') + 1
    except ValueError:
        sys.exit("Could not find '<!-- xkcd -->' in your README.md")

    rd_line = '<p align="center">'
    rd_line += '{}</br>'.format(req["title"])
    rd_line += '<img src="{}"></br>'.format(req["img"])
    rd_line += 'alt: {}</br>'.format(req["alt"])
    rd_line += '</p>'

    if (readme[line_index] == rd_line):
        sys.exit(0)
    else:
        rd_line = rd_line + '</table></p> \n'
        readme[line_index] = rd_line
    with open('README.md', 'w', encoding='utf-8') as file:
        file.writelines(readme)


if __name__ == '__main__':
    try:
        start_time = datetime.datetime.now().timestamp() * 1000
        r = xkcd_request()
        update_readme(r)
        print("Readme updated")
        end_time = datetime.datetime.now().timestamp() * 1000
        print("Program processed in {} miliseconds.".format(round(end_time - start_time, 0)))
    except Exception as e:
        traceback.print_exc()
        print("Exception Occurred " + str(e))

