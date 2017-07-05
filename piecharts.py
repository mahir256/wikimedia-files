#!/usr/bin/python3
# This script is intended to replace the ToolScript originally used
# to form the pie graphs in d:Wikidata:Statistics/Wikipedia.
# It is supposed to output the data in a form identical to
# that in d:Module:Statistical data/by project/classes.

import requests
import json

langs = ['bn'] # for testing, will be expanded later

headings = ['total', 'none', 'Q11266439', 'Q4167836', 'Q15184295',
'Q16521', 'Q11173', 'Q5', 'Q56061', 'Q1190554',
'Q811979', 'Q13406463', 'Q4167410', 'Q11424', "Q83620",
"Q6999", "Q16686448", "timestamp"]

suffixes = ['noclaim[31,279]',
'claim[31:(tree[11266439][][279])]',
'claim[31:(tree[4167836][][279])]',
'claim[31:(tree[15184295][][279])]',
'claim[31:(tree[16521][][279])]',
'claim[31:(tree[11173][][279])]',
'claim[31:5]',
'claim[31:(tree[56061][][279])]',
'claim[31:(tree[1190554][][279])]',
'claim[31:(tree[811979][][279])] and noclaim[31:(tree[56061][][279])]',
'claim[31:(tree[13406463][][279])]',
'claim[31:4167410]',
'claim[31:(tree[11424][][279])]',
'claim[31:(tree[83620][][279])]',
'claim[31:(tree[6999][][279])]',
'claim[31:(tree[16686448][][279])] and noclaim[31:(tree[5,16521,56061,811979,1190554,11173,13406463,4167410,11424,83620,6999,17633526][][279])]']

# Get query templates from Stas's conversion tool.
# First for the total...
querytemplates = []
querytemplates.append(requests.get("https://tools.wmflabs.org/wdq2sparql/w2s.php?wdq=link[bpywiki]").text.replace('?item', '(COUNT(?item) as ?count)', 1))
# ...and then for the rest
for i in suffixes:
    x = requests.get("https://tools.wmflabs.org/wdq2sparql/w2s.php?wdq=link[bpywiki] and "+i)
    querytemplates.append(x.text.replace('?item', '(COUNT(?item) as ?count)', 1))

# Then for each language defined above...
for i in langs:
    print(i+"wiki = {")
    for j in range(0,len(querytemplates)-1):
        # Get the values for each P31.
        # The exception handling is temporary.
        x = requests.get("https://query.wikidata.org/sparql?query="+querytemplates[j].replace('bpy',i)+"&format=json")
        try:
            y = json.loads(x.text)
        except json.decoder.JSONDecodeError:
            continue
        print(headings[j],"=",y["results"]["bindings"][0]["count"]["value"])
    print("},")
