# -*- coding: utf-8 -*-
# !/usr/bin/env
# !/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import sys
#print(sys.path)
from modules.split_data_from_xls import splitdatafromxls
from modules.create_lollipop_graph import createlollipopgraph
from modules.create_spider_graph import createspidergraph
from modules.create_radar_graph import createradargraph
from modules.create_doc_template import createdoctemplate
from modules.create_generic_radar_graph import creategenericradargraph

d = splitdatafromxls()
createlollipopgraph(d)
createspidergraph(d)
createradargraph(d)
creategenericradargraph('Gestione Aziendale','%','Priorities', 
	d['Strutturazione aziendale'][:-1], 
    d['Ottimizzazione risorse umane'][:-1], 
    d['Gestione degli scarti di produzione (se presenti)'][:-1], 
    d['Miglioramento gestione magazzino (se presente)'][:-1], 
    d['Controllo Qualità (se presente)'][:-1],
    d['Automatizzazione processi'][:-1],
    'gestione_aziendale')

# last because it needs images created by prev funct
createdoctemplate(d)