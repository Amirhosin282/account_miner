from config.config import *

id =""
numb = open("data/.save_file.txt", "a+")
numb.close()
numb = open("data/.save_file.txt", "r+")
if str(numb.read()) == "":
    numb.writable()
    numb.write("1")
numb.close()

data = open("data/output.txt", "a+")
data.close()
data = open ("data/output.txt", "r+")
if str(data.read()) == "":
    data.writable()
    data.write(f"id         username                password          E-mail             date and time \n {line} \n")
data.close()

os.system(cl())
a = 5
while a != 0:
    print(Fore.YELLOW, "If you encounter problems running the program, try again with a virtual environment (for Linux users) or with Selenium version 4.10.0.\n")
    print(Fore.GREEN, a)
    sleep(1)
    a -= 1
    os.system(cl())

target = "amirhosin282"
guess = ''


for index, character in enumerate(target): # this code for loding animaition
    j = ord(' ')
    while True:
        print(f'\r{text(figlet_format(guess, font="slant"))}{text(figlet_format(chr(j), font="slant"))}')
        os.system(cl())
        sys.stdout.flush()
        sleep(0.000001)
        if chr(j) == character:
            guess += character
            break
        j += 1

view(real_date, real_time())

# get data from user
print(Fore.GREEN)
email1 = input("print your Email or phone number for verify accounts (1 of 3): ").strip()
email2 = input("print your Email or phone number for verify accounts (2 of 3): ").strip()
email3 = input("print your Email or phone number for verify accounts (3 of 3): ").strip()
if email1 == '' or email2 == '' or email3 == '':
    print (Fore.RED, "inputs can't be empty!")
    sleep(5)
    os._exit(0)

print(Fore.YELLOW, line, Fore.GREEN)
send_number = int(input("Enter the number of accounts you want to create(just number): ").strip())

# open selenium driver
path = ''
if platform.system == 'Linux': # select os for chose driver type
    path = Service('./config/chromedriver')
elif platform.system == 'Windows':
    path = Service('./config/chromedriver.exe')

print (Fore.YELLOW, line, Fore.GREEN)
# start procses
for i in range(send_number):

    # open number and id file
    with open ("./data/.numb.txt", "r+", encoding="utf-8") as account_numb:
        ac_numb = str(account_numb.read())

    with open ("./data/.save_file.txt", "r") as id_file:
        account_id = str(id_file.read())

    # generating username
    username = str(RandomWords().get_random_word() + ac_numb)
    password = "Aa@123456"
    email = random.choice([email1, email2, email3])

    # get use selenium 
    try :
        # set chrome driver
        driver = webdriver.Chrome(service=path)
    except :
        print(Fore.RED, "You do not have the required drivers, please download the Selenium driver for Google Chrome from the relevant site or GitHub at: github.com/amirhosin282/account-maker and place it in the main directory of the tool, next to the main file.")
        sleep(10)
        os._exit(0)

    try:
        # open link in chrome
        driver.get("https://www.instagram.com/accounts/emailsignup/")

        # send email or phone to fild 1
        f1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[2]/div/label/input"))
        ).send_keys(email)

        # send password to fild 2
        f2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[3]/div/label/input"))
        ).send_keys(password)

        # send random word to fild 3
        f3 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[4]/div/label/input"))
        ).send_keys(str(RandomWords().get_random_word()))

        # send random username to last fild (4)
        f4 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[5]/div/label/input"))
        ).send_keys(username)

        # click on next bottom
        b1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[6]/div"))
        ).click()
        sleep(10)

        # get birthday
        b2 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div/div/div[4]/div/div/span/span[3]/select"))
        )
        Select(b2).select_by_value("2000")

        # click to next bottom
        b3 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div/div/div[6]"))
        ).click()

        # skip reCAPTCHA
        input("skip reCAPTCHA and pres on enter")

        # click to next bottom
        b4 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div/div/div[4]/button"))
        ).click()

        # get confirm code
        input("input confirm code and press enter")

        # click to next bottom
        b5 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div/div[2]/form/div/div[2]/div"))
        ).click()

        # create log
        log = f"{account_id}   {username}              {password}        {email}            {real_date} ----- {real_time()} \n"

        # show to user
        print(Fore.GREEN, "Success", Fore.WHITE, log)

        # save log on output file
        with open("./data/output.txt", "a+") as log_file:
            log_file.writable()
            log_file.write(str(log))

        # remove and rebuild number file
        os.remove("./data/.numb.txt")
        with open("data/.numb.txt", "w+", encoding="utf-8") as account_numb:
            account_numb.write(str(int(ac_numb) + 1))

        # remove and rebuild id file
        os.remove("./data/.save_file.txt")
        with open("data/.save_file.txt", "w+", encoding="utf-8") as save_file:
            save_file.write(str(int(account_id) + 1))

    except:
        log = f"{account_id}   {username}              {password}        {email}            {real_date} ----- {real_time()} \n"
        # show to user
        print(Fore.RED, "Faild", Fore.WHITE, log)
