from selenium import webdriver
import time
import os
import sys
import platform
if platform.system() == 'Linux':
 browser = webdriver.Firefox(executable_path="./driver/geckodriver")
if platform.system() == 'Windows':
 browser = webdriver.Firefox(executable_path="./driver/geckodriver.exe")

browser.get('https://vaccinicovid.regione.veneto.it/ulss'+sys.argv[1])

cf='//*[@id="cod_fiscale"]'
team='//*[@id="num_tessera"]'
casella='/html/body/div/form/div[2]/div[3]/div[2]/input'
bottone='/html/body/div/form/div[2]/div[5]/div[2]/button'
errmsg='/html/body/div/form/div[3]/div[1]'

with open('informazioni.txt', 'r') as f:
 mycf=f.readline()
 myteam=f.readline()

errore=True

while errore:

 browser.find_element_by_xpath(cf).send_keys(mycf)
 browser.find_element_by_xpath(team).send_keys(myteam)
 browser.find_element_by_xpath(casella).click()
 browser.find_element_by_xpath(bottone).click()
 time.sleep(1)
 if browser.find_elements_by_css_selector(".alert"):
  browser.refresh()
 else:
  errore=False

 #os.system("python3 bot.py")
 #sys.exit()

 #ricaricare la pagina e ricominciare in caso compaia il messaggio di errore