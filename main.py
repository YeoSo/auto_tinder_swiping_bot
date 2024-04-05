from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Facebook login email and password
fb_email = "your email"
fb_pw = "your pw"

# Keep Chrome browser opens
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initializing Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://tinder.com/")

# Waiting for the login button to appear and clicking it
sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="q1887506695"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login_button.click()

# Waiting for the Facebook login button to appear and clicking it
sleep(1)
fb_login_button = driver.find_element(By.XPATH, '//*[@id="q159125619"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div/div')
fb_login_button.click()

# Switching to Facebook login popup window
sleep(1)
fb_login_popup = driver.window_handles[1]
driver.switch_to.window(fb_login_popup)
print(driver.title)

# Fill up login info and hitting enter to log in
email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
pw_field = driver.find_element(By.XPATH, '//*[@id="pass"]')
email_field.send_keys(fb_email)
pw_field.send_keys(fb_pw)
pw_field.send_keys(Keys.ENTER)

# Switching back to main window
base_window = driver.window_handles[0]
driver.switch_to.window(base_window)
print(driver.title)

sleep(4)

# Allow location button
location_allow_button = driver.find_element(By.XPATH, '//*[@id="q159125619"]/main/div[1]/div/div/div[3]/button[1]')
location_allow_button.click()

sleep(1)
# Decline button for notification
notification_button = driver.find_element(By.XPATH, '//*[@id="q159125619"]/main/div[1]/div/div/div[3]/button[2]')
notification_button.click()

sleep(1)
# Decline button for cookies
cookie_button = driver.find_element(By.XPATH, '//*[@id="q1887506695"]/div/div[2]/div/div/div[1]/div[2]/button')
cookie_button.click()

# Delays enough until you'll be able to click like button
sleep(5)

for i in range(100):

    # Arrow right key to swipe right
    try:
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_RIGHT)
        sleep(2)

    # After get matched, click go back to the swipe mode again
    except ElementClickInterceptedException:
        try:
            back_to_tinder_button = driver.find_element(By.XPATH,
                                                        '//*[@id="q-2077089400"]/main/div/div[1]/div/div[3]/button')
            back_to_tinder_button.click()
        # Catches the cases when the "like" button hasn't yet loaded
        except NoSuchElementException:
            sleep(2)

driver.quit()




