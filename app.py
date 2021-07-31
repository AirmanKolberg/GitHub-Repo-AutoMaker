from github_api import create_github_repository
from system_functions import clear_screen, bash_command
from secrets import project_base_location, extra_files_location
from time import sleep


def determine_repo_name():

    # Get the repo name from the user
    repo_name = input('New repository name: ')

    # Get repo URL after creating repo
    repo_url = create_github_repository(repo_name)

    # In the event that the repo cannot be created...
    if not repo_name:

        print(f'"{repo_name}" is not valid, please try again...')
        repo_url = determine_repo_name()
    
    return repo_url, repo_name


# This will open the project in Visual Studio Code
def navigate_to_project_loation(repo_url, repo_name,
                                project_base_location):

    shell_commands = [f'cd {project_base_location}',
                      f'git clone {repo_url}',
                      f'cd {repo_name}',

                      # These files amount to a bot to help automatically keep track of file_names:descriptions for commits/pushes
                      f'cp {extra_files_location}/commit_and_push_all.py {project_base_location}/commit_and_push_all.py',
                      f'cp {extra_files_location}/masterCommit.json {project_base_location}/masterCommit.json',
                      f'cp {extra_files_location}/name_files_to_commit.py {project_base_location}/name_files_to_commit.py',
                      f'cp {extra_files_location}/system_functions.py {project_base_location}/system_functions.py',
                      f'cp {extra_files_location}/json_tools.py {project_base_location}/json_tools.py',

                      f'code .']

    # Iteratively execute each Shell command
    for command in shell_commands:

        bash_command(command)
        sleep(1)


if __name__ == '__main__':

    # Start the Terminal emulator with a fresh, beautiful, new slate
    clear_screen()

    bash_command('pwd')

    repo_url, repo_name = determine_repo_name()

    navigate_to_project_loation(repo_url, repo_name, 
                                project_base_location)
