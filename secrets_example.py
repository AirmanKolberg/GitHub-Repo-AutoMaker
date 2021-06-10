github_token = 'put your token string here'
github_username = 'and your username as a string here'

"""
This next variable should be a list containing all of the
normal Shell commands you'd run upon creating your project,
the following is a quick, simple example.
"""

custom_commands = [f"""echo "{readme_body}" >> README.md""",
                   "touch main.py", "touch secrets.py",
                   "echo 'secrets.py' >> .gitignore",
                   "git status"]
