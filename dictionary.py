# List
addressBookList = ["공덕", "고터"]

print(addressBookList[0])
print(addressBookList[1])

# List Test
testList = list()
testList.append("파이썬")
testList.append("C언어")
print(testList)

# Dictionary
addressBook = {"한승욱": "공덕", "류은진": "고터", "김유준": 35}

print(addressBook["한승욱"])
print(addressBook["류은진"])
print(addressBook["김유준"])

dictionaryTest = {('유선님', '성악') : '이태원',
                  ('광우님', '스타트업') : '수원'}

print(dictionaryTest[('유선님', '성악')])
print(dictionaryTest[('광우님', '스타트업')])

# Dictionary Test
testDictionary = dict()
testDictionary['Dog'] = 'Animal'
testDictionary['Human'] = 'Animal'
print(testDictionary)

is_dog_exist = "Dog" in testDictionary
print(is_dog_exist)

is_animal_exist = "Animal" in testDictionary
print(is_animal_exist)

testDictionary.pop('Dog')
print(testDictionary)

del testDictionary['Human']
print(testDictionary)

# Dictionary 3
testDictionary2 = {'아침': '주먹밥', '점심': '도시락', '저녁': '무언가'}
print(testDictionary2.keys())
print(testDictionary2.values())
print(testDictionary2.items())

