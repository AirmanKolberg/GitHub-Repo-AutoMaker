# GitHub Repository Helper!  (Visual Studio Code Edition)

This is the automatic GitHub repository maker that I often use, and I'm just here to share it with you if anyone wants a quick, and simple solution to automating the process of creating new
repositories.  Though there is something fun about just doing it yourself... either way!  Here's some code, enjoy it if you wish!

## How it Works

Rename `secrets_example.py` to `secrets.py` with a simple `mv secrets_example.py secrets.py` within the project directory, and within that file, you will need to insert your information for
the four variables:

- `github_token`
- `github_username`
- `project_base_location`
- `extra_files_location`

Next, install all required dependencies with `pip install -r requirements.txt` (or `pip3` if that's what your machine prefers.)

One that is done, simply run `python3 app.py` to create a new repository and open the project in Visual Studio Code.  You could, of course, go one step further and create a global Shell script
that runs `python3 fileLocation/app.py` so that you could create a repo no matter where in your computer you are (if you're like me and still access the computer via the Terminal emulator the
vast majority of the time)!  This bot will also setup another bot within your new repo's project directory to help automate the task of committing/pushing updates.  Enjoy.

## The PyCharm GUI-Version for the 2015 15" MacBook Pro (specifically)

Just a simple script written specifically for the 15" 2015 MacBook Pro, but can be configured for any screen (using the pointerPixels.py application).  This script will open a new project in PyCharm and link it up to your GitHub account for you, nice and simple.

A lot of PyCharm is GUI in nature, so this utilises PyAutoGUI quite extensively.  Please take the time to configure the application to your screen, unless of course you also happen to be on one of those 2015 15" Retina MacBook Pros.  If not, the (x, y) PyAutoGUI coordinates are not difficult to ammend.

---

### Donations!
Consider donating, though of course not necessary!  :)

Cardano (ADA):
addr1q9jxsfd87g4f9rcl7x43lwxnkmklek279yw0fhwrsm3pjjal23me7f9yesnhs2fhpf05xd0deta3csgn4z433rze7yjsav8ejn


BitCoin (BTC): 
33XbUGgEGx3oQ8wZEsdWBtZ6jncTPWoNtq


Etherium (ETH): 
0x68D8928631f697820cf2bd9B275e5b39D6Cba020


Dogecoin (DOGE):
DNJoCDAwwVcpRMH3wCeeCwRMpzUHW6uvbH


Ripple (XRP):
rahunjARy7sb2AEc75xdzqSRuMeUPqXxF2


VeChain (VET):
0xeD36284Fb479F15620f5c8Af0996A723c6b5dc43