# XML
import xml.etree.ElementTree as ET
xml_file = ET.parse('ready_xml.xml')
# print(xml_file)
root = xml_file.getroot()
#print(root)
# print(type(root))

# attrib, tag, parse, index
# print(root[0].attrib) #{'id': 'bk101'}
#
# print(root[0].tag) #{'id': 'bk101'}

# print(root[0].parse) #{'id': 'bk101'}
#
# print(root[0].index) #{'id': 'bk101'}

# xml_str = ET.fromstring('<a x="test_attribute">123</a>')
# print(xml_str)
# print(xml_str.tag)
# print(xml_str.text)
# print(xml_str.attrib)
# ET.dump(xml_file)   #only used for debugging

# iter, find, findall
# print(root.find('book').attrib)

# for book in root.find('book'):
#     print(book.text)

# for book in root.findall('book'):
#     print(book[1].text)
#     print(book.attrib)

# for price in root.iter('price'):
#     print(price.tag,price.text)
    # print(price.text)
#text get and set
# for genre in root.iter():
#     # print(genre.tag)
#     # print(genre.get('price'))
#     if genre.get('id') == 'bk102':
#         print(genre.attrib)
#         genre.set('view','super')
#         print(genre.attrib)
#         print(genre.text)
#         for t in genre:
#             print(t.text)
#             t.text = 'ismail'
# for genre in root.iter('price'):
#     genre.text = f"${float(genre.text.replace('$',''))+10}"
    # float(genre.text.replace("$",""))+10


# write, remove
# xml_file.write('newxmlfile.xml')  # this is for saving the file
# root.remove(root.find('id'))
# root.remove(root.find('id'))
# ET.dump(root)

#write
# new_element = ET.Element('testing element')
# new_element.text = 'text text'
# root.insert(0,new_element)
# ET.dump(root)

# for elem in root.findall('.//title'):
#     print(elem.tag)
#
# for elem in root.findall('.//*[@id]'):
#     print(elem.tag)


