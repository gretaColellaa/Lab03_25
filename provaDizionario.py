import dictionary as d
import multiDictionary as md


d1 = d.Dictionary([], "english")
d1.loadDictionary("resources/English.txt")
#d1.printAll()



md1 = md.MultiDictionary()
print(md1.searchWordDichotomic("ciao belllll", "italiano"))
