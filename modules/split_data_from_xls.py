# -*- coding: utf-8 -*-
# !/usr/bin/env
# !/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import xlrd, sys, os
from docx import Document
from docx.shared import Inches


def splitdatafromxls():
    print('Opening file..')
      # Give the location of the xls file 
    cur_path = os.path.dirname(__file__)
    rel_path = os.path.relpath('datasource/PMI-network-data.xlsx')
    #loc = ("/Users/andre/Google Drive/Projects/Python/Useful Python Stuff/word and docs/PMI-network-data.xlsx")
    #loc = ('PMI-network-data.xlsx')

    wb = xlrd.open_workbook(rel_path)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    # Extracting number of rows in xls
    # print('Number of Rows: ' + str(sheet.nrows))

    # Extracting number of columns 
    # print('Number of Cols: ' + str(sheet.ncols))

    # Creating a Dictionary with keys as column names and values 
    # taken from the second row (first is header)
    d = dict()
    for i in range(sheet.ncols): 
        # print(sheet.cell_value(0, i)) 
        d[sheet.cell_value(0, i)] = sheet.cell_value(1,i)
        # print('added')
    print('\n ------- \n')
    print(d)

    # Print All the values in dictionary
    for i in d : 
        print("%s  %s" %(i, d[i]))

    # Extract a single Row, all values.
    # print(sheet.row_values(1))
    id_azienda = d['ID']
    nome_azienda = d['Nome']
    settore_azienda = d['Qual è il tuo settore di riferimento?'] 
    strategia_azienda = d['Priorità/Necessità: Altro']
    partita_iva = d['Partita IVA']
    segmento_mercato = d['Segmento di mercato:']


    # Valori Verificati 
    print(d['I clienti dell\'impresa sono:'])
    print(d['Il vantaggio competitivo dell\'azienda è:']    )
    print(d['In azienda è presente un\'attività di formazione permanente del personale?']      )
    print(d['Numero di laureati presenti in azienda'])
    print(d['Numero di consulenti esterni di tipo tecnico (numero di persone, no commercialista o avvocato)']  )
    print(d['Nella sua azienda è presente un ufficio R&D?']    )
    print(d['L\'azienda ha mai partecipato a bandi di finanziamento pubblici?'])
    print(d['L\'impresa ha mai svolto progetti finanziati con bandi pubblici?'])
    print(d['I bandi a cui l\'azienda ha partecipato erano in ambito:'])
    print(d['L\'impresa desidera in futuro partecipare a bandi di finanziamento pubblici?']      )
    print(d['La Sua azienda è (in maggioranza):'])
    print(d['La pianificazione delle attività e/o della produzione avviene tramite un software gestionale?']  )
    print(d['Vengono eseguiti studi per allocare le voci di costo di ogni singolo prodotto? (O è già possibile allocarle)']  )
    print(d['Che altri tipologie di software vengono utilizzati in azienda?'])
    print(d['Quanto si sente industria 4.0 da 0 a 100?']    )
    print(d['In azienda sono presenti macchinari interconnessi?']    )
    print(d['In azienda viene utilizzata la manifattura additiva (stampa 3D)?'])
    
    # Tecnologie 4.0 presenti in azienda
    print(d['Realtà aumentata'])
    print(d['Integrazione orizzontale/verticale'])
    print(d['Simulazione'])
    print(d['Internet delle cose (IOT)'])
    print(d['Cloud'])
    print(d['Cyber-Security'])
    print(d['Big data e analitiche'])

    print(d['La gestione e pianificazione delle attività avviene tramite un software gestionale?'])
    print(d['Vengono eseguiti studi per allocare le voci di costo di ogni singola attività o servizio offerto? (O è già possibile allocarle)'])
    
    # Tipi di Sftw
    print(d['Quale tipologie di software vengono utilizzate in azienda?'])
    
    print(d['L\'azienda sta puntando principalmente a innovazione:'])
    print(d['Negli ultimi 3 anni l’azienda ha introdotto:']    )
    print(d['Qual è il livello di familiarità dell’azienda con la Proprietà Industriale?'])
    print(d['L’impresa è in grado di attribuire un valore economico al proprio patrimonio intangibile?'])
    
    # Priorità - Produzione
    print(d['Aumento capacità produttiva'])
    print(d['Aumento efficienza produttiva'])
    print(d['Diversificazione Servizi'])
    print(d['Diversificazione Prodotti'])
    
    # Priorità - Ricerca e Innovazione
    print(d['Proprietà industriale'])
    print(d['Collaborazioni'])
    print(d['Miglioramento comunicazione INTERNA'])
    print(d['Miglioramento comunicazione ESTERNA'])
    print(d['Ricerca e Sviluppo'])

    # Priorità - Gestione Aziendale
    print(d['Strutturazione aziendale'])
    print(d['Ottimizzazione risorse umane'])
    print(d['Gestione degli scarti di produzione (se presenti)'])
    print(d['Miglioramento gestione magazzino (se presente)'])
    print(d['Controllo Qualità (se presente)'])
    print(d['Automatizzazione processi'])
    
    # Strategie - Open
    print(d['Priorità/Necessità: Altro'])

    return(d)
