import os
from selenium import webdriver

def launch():
    try:
        # Automated Edge Window
        driver = webdriver.Edge(executable_path=os.path.join(os.getcwd(),'msedgedriver.exe'))
        
    except Exception:
        # 'options' stops the ignorable usb error(0x1F) to stop from clogging up the terminal
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Automated Chrome Window
        driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(),'chromedriver.exe'), options=options)
    
    # Instantiate the Automated Window
    driver.set_window_size(600,400)
    driver.get(os.path.join(os.getcwd(), 'Audio.html'))


if __name__=='__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(),'chromedriver.exe'), options=options)
    driver.set_window_size(600,400)
    driver.get(os.path.join(os.getcwd(), 'Audio.html'))
