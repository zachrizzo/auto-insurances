from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from pynput.mouse import Button, Controller as ControllerM
from pynput.keyboard import Controller as ControllerK
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
service = ChromeService(executable_path=ChromeDriverManager().install())
mouse = ControllerM()
keyboard = ControllerK()
path = r"/Users/zachrizzo/Desktop/AMA Everyrthing/Automation for AMA/auto insurances /auto insurence.py"

# CareFirst Blue Cross and Blue Shield
# CarePlus (Florida Medicare)


class AddNewProvider:

    def __init__(self):
        options = webdriver.ChromeOptions()

        options.add_experimental_option("prefs", {
            "download.default_directory": path,
            "downloaded.extensions_to_open": "applications/pdf",
            # savefile
            "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],

            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True,
            "download.open_pdf_in_system_reader": False,
            "profile.default_content_settings.popups": 0,
            # "safebrowsing.enabled": False,
            # "profile.content_settings.exceptions.automatic_downloads.*.setting": True,


        })
        options.add_argument("--disable-extensions")

        options.add_argument('disable-component-cloud-policy')

        options.add_argument("plugins.always_open_pdf_externally")
        self.driver = webdriver.Chrome(options=options , service=service)
        self.mouse = ControllerM()
        self.keyboard = ControllerK()
        self.action = ActionChains(self.driver)
        self.driver.get('https://azamasapp.ecwcloud.com/mobiledoc/jsp/webemr/login/newLogin.jsp')
        self.driver.maximize_window()
        self.health_providers = [
        "AARP",
        "AmeriChoice (United Healthcare Community Plan)",
        "Anthem Blue Cross - California",
        "Anthem Blue Cross and Blue Shield",
        "Arizona Foundation for Medical Care",
        "Arkansas Blue Cross",
        "Banner Health Company",
        "Blue Bell Benefits Trust",
        "Blue Care Network of Michigan",
        "Blue Choice Health Plans",
        "Blue Cross - Idaho",
        "Blue Cross - Northeastern Pennsylvania",
        "Blue Cross and Blue Shield - Alabama",
        "Blue Cross and Blue Shield - Arizona",
        "Blue Cross and Blue Shield - Florida (Florida Blue)",
        "Blue Cross and Blue Shield - Georgia",
        "Blue Cross and Blue Shield - Illinois",
        "Blue Cross and Blue Shield - Kansas",
        "Blue Cross and Blue Shield - Kansas City",
        "Blue Cross and Blue Shield - Louisiana",
        "Blue Cross and Blue Shield - Massachusetts",
        "Blue Cross and Blue Shield - Michigan",
        "Blue Cross and Blue Shield - Minnesota",
        "Blue Cross and Blue Shield - Mississippi",
        "Blue Cross and Blue Shield - Nebraska",
        "Blue Cross and Blue Shield - New Mexico",
        "Blue Cross and Blue Shield - North Carolina",
        "Blue Cross and Blue Shield - Oklahoma",
        "Blue Cross and Blue Shield - Rhode Island",
        "Blue Cross and Blue Shield - South Carolina",
        "Blue Cross and Blue Shield - Tennessee",
        "Blue Cross and Blue Shield - Texas",
        "Blue Cross and Blue Shield - Vermont",
        "Blue Cross and Blue Shield - Western New York",
        "Blue Cross and Blue Shield - Wyoming",
        "Blue Cross and Blue Shield Federal Employee Program",
        "Bridgeway Health Solutions",
        "Cigna",
        "Community Health Choice",
        "Empire Blue Cross and Blue Shield",
        "Excellus Blue Cross and Blue Shield",
        "Gilsbar",
        "Golden Rule Insurance Company",
        "Government Employees Health Association (GEHA)",
        "GWH-Cigna (formerly Great West Healthcare)",
        "Health Choice - Arizona",
        "Health Choice Insurance",
        "HighMark Blue Cross and Blue Shield",
        "Highmark Blue Shield",
        "Horizon Blue Cross and Blue Shield - New Jersey",
        "Humana Care Plan",
        "Magellan Health Services",
        "Medicare",
        "Mercy Care",
        "Molina Healthcare",
        "Tricare",
        "Unicare",
        "University Family Care",
        "Wellcare",
        "Banner Health Choice Plus and Select",
        "CMS Medicare",
        "Humana Medicare Advantage",
        "Ambetter",
        "Blue Cross and Blue Shield of North Dakota",
        "Blue Cross and Blue Shield of Montana",
        "AARP Medicare Supplement",
        "Aetna Medicare Advantage",
        "Blue Cross blue Shield Medicare Advantage PPO",
        "CHAMPVA",
        "Humana PPO",
        "Medicare Railroad",
        "State Farm Medicare Supplement",
        "United Healthcare PPO",
        "UMR",
        "USAA Life Ins Co Medicate Supplement",
        "Medicaid RI",
        "United Healthcare",
        "United HealthCare Managed Medicaid Plan",
        "Humana",
        "Cigna APWU",
        "Cigna Local Plus",
        "Medicaid - United Healthcare",
        "Blue Cross and Blue Shield - Virginia",
        "Blue Cross and Blue Shield - West Virginia",
        "Bright Health Plans",
        "Medica",
        "Humana Choice MCR",
        "United Healthcare Medicare",
        "Aetna Medicare(HMO, PPO",
        "Cigna Medicare (MA HMO)",
        "Cigna Medicare PPO",
        "Humana ChoiceCare Commercial",
        "UnitedHealthcare MedicareComplete Choice (PPO)",
        "Ambetter Marketplace"
    ]


    def login(self, userName, password):
        Eclinical_loging = self.driver.find_element(By.XPATH, '//*[@id="doctorID"]')
        Eclinical_loging.send_keys(userName)
        time.sleep(2)
        loging_buttom_1 = self.driver.find_element(By.XPATH, '//*[@id="nextStep"]')
        loging_buttom_1.click()
        password_2 = self.driver.find_element(By.XPATH, '//*[@id="passwordField"]')
        password_2.send_keys(password)
        time.sleep(2)
        login_2 = self.driver.find_element(By.XPATH, '//*[@id="Login"]')
        login_2.click()
        time.sleep(8)
        # input("Press Enter to continue...")


    def add_insurance_with_mouse(self):


        time.sleep(4)
        # for i in list1:
        #     if i in list1:
        #         print(list1.count(i))
        for i in self.health_providers:
            time.sleep(2)
            print(i)

            mouse.position = (608, 546)

            time.sleep(1)
            mouse.click(Button.left, 3)
            # mouse.press(Button.left,)
            # mouse.release(Button.left,)nthem Blue Cross - California
            time.sleep(1)
            keyboard.type(i)
            mouse.position = (592, 572)
            time.sleep(1)
            mouse.press(Button.left,)
            mouse.release(Button.left,)
            print('complete')

    def Navigate_to_Healow_health_providers(self):
        time.sleep(6)
        menu_button = self.driver.find_element(By.CSS_SELECTOR, '#jellybean-panelLink4')
        menu_button.click()
        time.sleep(1)
        healow_tab = self.driver.find_element(By.CSS_SELECTOR, '#jcarousel2 > ul > li:nth-child(11)')
        healow_tab.click()
        time.sleep(.5)
        open_accsess_tab = self.driver.find_element(By.CSS_SELECTOR, '#jcarousel2 > ul > li.open > div > div.pad15.orange-list-lp > ul > li:nth-child(7)')
        open_accsess_tab.click()
        input("Select Provider and Press Enter to continue...")

    def add_insurance_with_No_Mouse(self):
        while True:
            time.sleep(2)
            parent_iframe = self.driver.find_element(By.CSS_SELECTOR, '#jtnRegistrationFrameOA')
            self.driver.switch_to.frame(parent_iframe)
            iframe = self.driver.find_element(By.CSS_SELECTOR, '#healowSettingFrame')
            self.driver.switch_to.frame(iframe)
            insurance_tab = self.driver.find_element(By.CSS_SELECTOR, '#insuranceTab')
            insurance_tab.click()

            insurance_dropdown = self.driver.find_element(By.CSS_SELECTOR, '#insSpecialtyDiv > div > div.add-insurance > div.col-sm-12 > button')
            insurance_dropdown.click()

            insurance_search_input = self.driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(34) > div > div > input[type=search]')
            insurance_search_input.click()
            insurance_search_input.clear()

            insurance_span = self.driver.find_element(By.CSS_SELECTOR, '#insSpecialtyDiv > div > div.add-insurance > div.col-sm-12 > button > span:nth-child(2)')
            current_providers = insurance_span.text.split(', ')
            #if the insurance provider is not in the list, remove it from the list
            for provider in current_providers:
                # if provider not in self.health_providers:
                    insurance_search_input.send_keys(provider)

                    options = self.driver.find_elements(By.CSS_SELECTOR, 'body > div:nth-child(34) > ul > li > label > input')
                    labels = self.driver.find_elements(By.CSS_SELECTOR, 'body > div:nth-child(34) > ul > li > label')

                    for i, option in enumerate(options):
                        if labels[i].text == provider:
                            if option.is_displayed():
                                self.driver.execute_script("arguments[0].click();", option)
                                break

                    insurance_search_input.click()
                    insurance_search_input.clear()



            #add the insurance providers
            for providers in self.health_providers:
                insurance_search_input.send_keys(providers)
                time.sleep(.2)

                options = self.driver.find_elements(By.CSS_SELECTOR, 'body > div:nth-child(34) > ul > li > label > input')
                labels = self.driver.find_elements(By.CSS_SELECTOR, 'body > div:nth-child(34) > ul > li > label')

                for i, option in enumerate(options):


                    if labels[i].text == providers:
                        # print(labels[i].text , len(labels[i].text))
                        # print(providers, len(providers))
                        #check if options is in view
                        if option.is_displayed():
                            # print('in view')

                            # Use JavaScript to click on the option
                            self.driver.execute_script("arguments[0].click();", option)
                            break


                insurance_search_input.click()
                insurance_search_input.clear()


                print(providers)
            input("Press Enter to continue...")




if __name__ == "__main__":
    bot  = AddNewProvider()
    bot.login('zachrizzo', 'Karen013074!')
    bot.Navigate_to_Healow_health_providers()
    bot.add_insurance_with_No_Mouse()

