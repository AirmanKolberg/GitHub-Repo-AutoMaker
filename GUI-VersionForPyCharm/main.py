from system_commands import *
from time import sleep
import pyautogui as pag
from github import Github
from secrets import github_token, github_username, custom_commands


def link_to_ide(repo_link, project_name):

    # Open the IDE/text editor of your choice
    bash_command("open -a 'PyCharm CE'")

    # Wait until the application is open
    sleep(6)

    """
    To get the coordinates below, use the
    pointerPixels.py file to obtain the
    exact (x, y) coordinates for your
    mouse to click on the screen.
    """

    # The "New Project" button
    pag.click(x=857, y=83)
    sleep(3)

    # Type the project name w/ interval to prevent errors
    pag.write(project_name, interval=0.08)

    # The "Create" button
    pag.click(x=1079, y=880)
    sleep(25)

    # Open the Terminal in PyCharm
    pag.hotkey('option', 'f12')
    sleep(3)
    
    # Clone the repo
    pag.write(f'git clone {repo_link}', interval=0.08)
    sleep(0.1)
    pag.press('return')
    sleep(5)

    # Change directory into repo
    pag.write(f'cd {project_name}', interval=0.08)
    sleep(0.1)
    pag.press('return')
    sleep(0.1)

    # Iterates through all custom commands to run in the Terminal
    def execute_custom_terminal_commands(commands):

        for command in commands:
            pag.write(command, interval=0.08)
            sleep(0.1)
            pag.press('return')
            sleep(0.1)

    execute_custom_terminal_commands(custom_commands)
    

def create_github_repository(project_name):
    g = Github(github_token)
    u = g.get_user()

    try:
        u.create_repo(project_name)
        return f'https://github.com/{github_username}/{project_name}.git'
    except Exception:
        return False


if __name__ == '__main__':

    clear_screen()

    # Get name/commit information from the user
    project_name = input('Repository name: ')

    # Create the repo
    repo_link = create_github_repository(project_name)

    if repo_link:
        link_to_ide(repo_link, project_name)
