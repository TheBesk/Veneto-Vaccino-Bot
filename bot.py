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
casella='/html/body/div/form/div[2]/div[4]/div[2]/input'
bottone='/html/body/div/form/div[2]/div[6]/div[2]/button'
errmsg='/html/body/div/form/div[3]/div[1]'

servizio2='/html/body/div/form/div[3]/button[2]'

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
 #else:
  #errore=False
 browser.find_element_by_xpath(servizio2).click()
 sedi_tot=(browser.find_elements_by_class_name("btn-full"))
 count=0
 for i in sedi_tot:
  if i.is_enabled()==True:
   count+=1
 
 if count==0: #confrontare con il numero di bottoni disabled
  browser.refresh()
  print("nessun posto libero")
 else:
  print("Puoi prenotare il vaccino!")
  errore=False

 #os.system("python3 bot.py")
 #sys.exit()

 #ricaricare la pagina e ricominciare in caso compaia il messaggio di errore
