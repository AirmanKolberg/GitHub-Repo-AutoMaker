from system_commands import *
from time import sleep
import pyautogui as pag


def link_to_ide(project_name, custom_commit):

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
    sleep(20)

    # The "VCS" button (which becomes "Git" afterwards)
    pag.click(x=582, y=13)
    sleep(0.5)

    # The "Share Project on GitHub" option
    pag.click(x=631, y=303)
    sleep(3)

    # The "Share" button
    pag.click(x=850, y=542)
    sleep(10)

    # Unselect everything
    pag.click(x=530, y=247)
    sleep(1)

    # Write custom commit, if applicable
    if custom_commit:

        # Click the text field
        pag.click(x=659, y=603)

        # Delete the default commit
        pag.hotkey('command', 'a')
        pag.press('backspace')

        # Insert the custom commit
        pag.write(custom_commit, interval=0.08)

    # Add initial commit
    pag.click(x=923, y=731)
    sleep(3)

    # Close the pop-up with the "Add" button
    pag.click(x=892, y=512)


if __name__ == '__main__':
    # Make way for the excitement to come
    clear_screen()

    # Get name/commit information from the user
    project_name = input('Repository name: ')
    custom_commit = input('Custom commit (leave blank if none): ')

    # Indicate no custom commit if left blank
    if custom_commit == '':
        custom_commit = False

    # Link the repo to your IDE
    link_to_ide(project_name, custom_commit)
