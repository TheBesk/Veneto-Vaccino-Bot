# Veneto Vaccino Bot
Semplice script in python per velocizzare la prenotazione per i vaccini sul sito della Regione Veneto

## Utilizzo
Modificare il file informazioni.txt inserendo il proprio codice fiscale nella prima riga, e le ultime sei cifre della propria tessera sanitaria nella seconda riga.
Poi eseguire lo script passando come parametro il numero della ULSS di appartenenza:  
`python3 bot.py 1`
In questo caso verrà eseguito lo script caricando la pagina dell'azienda sanitaria locale n.1 Dolomiti.

## Requisiti
* Python 3
* Framework Selenium
* Avere Firefox installato

## Installare Selenium
`pip3 install selenium`
oppure
`python -m pip install -U selenium`

