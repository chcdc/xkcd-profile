
'''
Readme With xkcd webcomic
'''
import sys
import traceback
import datetime
import requests


def get_xkcd_data():
    """Gets xkcd comic data from the API"""
    try:
        request = requests.get("https://xkcd.com/info.0.json")
    except requests.exceptions.RequestException as error:
        raise SystemExit(error) from error
    resp_dict = request.json()
    return resp_dict


def update_readme(xkcd_data):
    """Updates the README file with the latest xkcd comic"""
    with open('README.md', 'r', encoding='utf-8') as file:
        readme = file.readlines()
    try:
        line_index = readme.index('<!-- xkcd -->\n') + 1
    except ValueError:
        sys.exit("Could not find '<!-- xkcd -->' in your README.md")

    rd_line = '<p align="center">'
    rd_line += f'{xkcd_data["title"]}</br>'
    rd_line += f'<img src={xkcd_data["img"]}></br>'
    rd_line += f'<font size =2>alt: {xkcd_data["alt"]}</br></font>'
    rd_line += '</p>'

    if readme[line_index] == rd_line:
        sys.exit(0)
    else:
        rd_line = rd_line + '</table></p> \n'
        readme[line_index] = rd_line
    with open('README.md', 'w', encoding='utf-8') as file:
        file.writelines(readme)


if __name__ == '__main__':
    try:
        start_time = datetime.datetime.now().timestamp() * 1000

        # Get the latest xkcd comic data
        xkcd_data = get_xkcd_data()

        # Update the README file with the latest xkcd comic
        update_readme(xkcd_data)

        # Print a success message and the processing time
        print("Readme updated")
        end_time = datetime.datetime.now().timestamp() * 1000
        print(f"Program processed in"
              f"{round(end_time - start_time, 0)} miliseconds.")
    except Exception as error:
        traceback.print_exc()
        print("Exception Occurred " + str(error))
