import requests
from secrets import github_token, project_location, readme_body
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
    # Navigate to newly created project directory
    bash_command('cd')
    bash_command(f'cd {project_location} && mkdir {project_name}')
    bash_command(f'cd {project_name}')

    # Create startup files
    bash_command('touch secrets.py')
    bash_command('touch required.txt')
    bash_command('touch test.py')

    # Create main and readme files
    bash_command("""echo "if '__name__' == '__main__':\n" >> main.py""")
    bash_command(f"echo '# {project_name}{readme_body}' >> README.md")

    # Add private files to the .gitignore
    bash_command("echo 'secrets.py\ntest.py' >> .gitignore")

    # Make initial commit
    bash_command('git init')
    bash_command('git add README.md')
    bash_command("git commit -m 'first commit'")
    bash_command('git branch -M main')
    bash_command(f'git remote add origin https://github.com/AirmanKolberg/{project_name}.git')
    bash_command('git push -u origin main')

    # Open project in Visual Studio Code
    bash_command(f"open -a 'Visual Studio Code' main.py")


if __name__ == '__main__':
    clear_screen()

    project_name = input('Repository name: ')
    create_the_repo(project_name)
    setup_project_directory(project_name)
