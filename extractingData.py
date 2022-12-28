import xml.etree.ElementTree as ET


# Pass the path of the xml document
tree = ET.parse('comments_42.xml')

# get the parent tag
root = tree.getroot()
# print(root[1].tag)
# print(len(root[1]))

num_count = 0
num_list = []
for num in root.iter('count'):
    num_list.append(int(num.text))

for x in num_list:
    num_count = num_count + x


print(num_count)
