from lxml import etree
import xml.etree.ElementTree as ET

# 1) Validation DTD
print("🔍 Validation DTD…")
dtd = etree.DTD('data/portfolio.dtd')
xml_doc = etree.parse('portfolio.xml')
if dtd.validate(xml_doc):
    print(" portfolio.xml est conforme à portfolio.dtd")
else:
    print(" Erreurs de validation DTD:")
    for err in dtd.error_log.filter_from_errors():
        print(f" - Ligne {err.line}, Col {err.column} : {err.message}")

# 2) Parsing pour vérifier les contenus
print("\n🔍 Parsing et extraction des blocs pour la langue 'fr'…")
tree = ET.parse('portfolio.xml')
root = tree.getroot()
for block in root.findall('block'):
    bid = block.get('id')
    el = block.find("./content[@lang='fr']")
    text = el.text if el is not None else "[MANQUE]"
    print(f"{bid}: {text}")
