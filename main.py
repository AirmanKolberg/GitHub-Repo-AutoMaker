import requests
from secrets import github_token, project_location, readme_body, base_location
from system_commands import *
from pprint import pprint

api_url = 'https://api.github.com'


def create_payload(project_name):
    payload_segmented = ["""{"name": """, '"', project_name, '"', "}"]
    payload = str()

    for segment in payload_segmented:
        payload += segment

    return payload


def create_the_repo(project_name):
    payload = create_payload(project_name)
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": 'application/vnd.github.v3+json'
    }

    r = requests.post(api_url + '/user/repos', data=payload, headers=headers)
    pprint(r.json())


def setup_project_directory(project_name):
    bash_commands = ['cd',
                     f'cd {project_location} && mkdir {project_name}',
                     f'cd {project_name}',
                     'touch secrets.py',
                     'touch required.txt',
                     'touch test.py',
                     """echo "if '__name__' == '__main__':\n" >> main.py""",
                     f"echo '# {project_name}{readme_body}' >> README.md",
                     "echo 'secrets.py\ntest.py' >> .gitignore",
                     'git init',
                     'git add README.md',
                     "git commit -m 'first commit'",
                     'git branch -M main',
                     f'git remote add origin https://github.com/AirmanKolberg/{project_name}.git',
                     'git push -u origin main']

    for command in bash_commands:
        bash_command(command)


if __name__ == '__main__':
    clear_screen()

    project_name = input('Repository name: ')
    create_the_repo(project_name)
    setup_project_directory(project_name)

    # Open project in PyCharm
    bash_command(f"open -a 'PyCharm CE' {base_location}{project_location}{project_name}")
