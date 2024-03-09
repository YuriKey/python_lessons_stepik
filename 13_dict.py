# # список
#
family_1 = ['Frank', 'Fiona', 'Lip', 'Yan', 'Deby', 'Karl', 'Fiona']
print(family_1)
print(len(family_1))
#
# # множества
family_2 = {'Frank', 'Fiona', 'Lip', 'Yan', 'Deby', 'Karl', 'Fiona'}
print(family_2)
print(len(family_2))

# словарь (ключ:значение)
family_3 = {'dad': 'Frank', 'daughter': 'Fiona', 'son': 'Lip', 'son2': 'Yan'}
print(family_3['daughter'])
print(len(family_3))
for k, v in family_3.items():
    print(k)
