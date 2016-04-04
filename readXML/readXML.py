import xml.etree.ElementTree as et
tree = et.ElementTree(file="D:\\testxml.xml")
root = tree.getroot()
print(root.tag)
for child in root:
    print('tag:',child.tag,'attributes : ',child.attrib)
    for grandchild in child:
        print('\tgrandchild:',grandchild.tag,'attributes : ',grandchild.attrib,'item : ',grandchild.text)
        for grandchild1 in grandchild:
            print('\t\tgrandchild:',grandchild1.tag,'attributes : ',grandchild1.attrib,'item : ',grandchild1.text)
            for grandchild2 in grandchild1:
               print('\t\t\tgrandchild:',grandchild2.tag,'attributes : ',grandchild2.attrib,'item : ',grandchild2.text)