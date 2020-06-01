import json
import yaml
from xml.etree.ElementTree import Element
with open ("sample.json","r") as file:
    data_p=json.load(file)
with open('sample.yml','w') as f:
    yaml.dump(data_p,f,default_flow_style=False)

from dicttoxml import dicttoxml
xml = dicttoxml(data_p)
with open('sample.xml','w') as f:
    f.write(xml.decode("utf-8"))
    

