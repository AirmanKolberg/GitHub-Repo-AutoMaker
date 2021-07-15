from github import Github
from secrets import github_token, github_username


# Returns string of the .git project URL and the project name
def create_github_repository(project_name):

    g = Github(github_token)
    u = g.get_user()

    try:

        u.create_repo(project_name)
        
        return f'https://github.com/{github_username}/{project_name}.git', project_name

    except Exception:

        return False


if __name__ == '__main__':

    pass
