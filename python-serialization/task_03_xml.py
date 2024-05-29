#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Method that serialize the dictionary into XML
    and save it to the given filename.

    Args:
        dictionary: the data list python to convert in XML
        filename: the file when we save the dictionary converted
    """
    def dict_to_xml(elem_racine, dic):
        """
        Convert a simple dict of key/value pairs into XML.

        Args:
            elem_racine: element racine to construct a file xml
            dic: the dictionnary to convert in xml
        """
        elem = ET.Element(elem_racine)
        for key, val in dic.items():
            child = ET.SubElement(elem, key)
            child.text = str(val)
        return elem

    # Create root element
    root = dict_to_xml('data', dictionary)

    # Create an ElementTree object and write it to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Method that read the XML data from that file,
    and return a deserialized Python dictionary.

    Args:
        filename: the file name contains the xml data
    Returns:
        dictionary deserialized
    """
    dict_data = {}
    try:
        #parse le fichier xml
        tree = ET.parse(filename)
        #recuperer l'element racine du fichier xml
        root = tree.getroot()
        #parcourir les sous elements sur l'element racine
        for child in root:
            # Récupère le nom de l'élément enfant
            key = child.tag
            # Récupère le texte de l'élément enfant
            value = child.text
            # Ajoute la paire clé/valeur au dictionnaire désérialisé
            dict_data[key] = value
        return dict_data
    except Exception as e:
        # Gère les exceptions, telles que le fichier non trouvé ou le fichier XML mal formé
        print(f"An error occurred: {e}")
        return None
