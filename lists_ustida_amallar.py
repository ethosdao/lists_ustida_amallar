#number = [1, 3, 6, 7, 9, 10]
#list ichida nechta element borligini aniqlash uchun len() funksiyasi bajariladi
#count = len(number)
#print(count)

#list ustida amallar 2 daraja oxirgi elementni chiqarish
#mevalar = ["olma", "behi", "shaftoli", "gilos"]
#pytonda oxirgi elementni chiqarish uchun list(-1) amali bajariladi
#oxirgi_nom = mevalar[-1]
#print(oxirgi_nom.title())

#lists ustida amallar 3 daraja yangi element qoshish
#list = ["sham", "guruch", "lartoshka", "piyoz"]
#biron bir element qoshish uchun quydagi amallar bajariladi. append() bu element oxiriga qoshadi, insert(boshiga yoki ortasiga qoshadi),
#list.append("sabzi")
#list.insert(0, "sabzi")
#list.insert(2, "sabzi")
#print(list)

#lists ustida amallar 4 daraja Eng katta sonni topish
#number = [12, 3, 6, 9, 20, 25, 36, 99, 100]
#birinchi elementni Eng katta son deb olamiz. Agar son katta bolsa almashtiradi
#max_num = number[0]
#for n in number:
#    if n > max_num:
#        max_num = n
#print(max_num)   

#lists ustida amallar 5 daraja listni teskari chiqarish
#number = [12, 3, 6, 9, 20, 25, 36, 99, 100]
 #listni teskari olish uchun reverse() usuli
#number.reverse()
#print(number)
#agaeda uni osuvchi tartibda joylab teskari tartibda chiqaradigan bolsak reversed() funksiyasi qollaniladi
#teskari_iterator = reversed(number)
#teskari_royxat = list(teskari_iterator)
#print(teskari_royxat)
# Yana bitta usual slicing usuli [: :-1]
#reversed_list = number[: :-1]
#print(reversed_list)

#lists ustida amallar sonlarni 6 daraja juft va toq sonlarni ajrarish
#number = [12, 3, 6, 9, 20, 25, 36, 99, 100]
#event_number = []
#for n in number:
   # if n % 2 == 0:
        #event_number.append(n)
#print(event_number)
#toq sonlarni ajrarish
#odd_number = []
#for n in number:
 #   if n % 2  == 0:
#        pass
  #  else:
    #    odd_number.append(n)
       # print(odd_number)
    
    #sonlar ustida amallar 7 daraja takrorlanadigan elementlarni olib tashlab
#list = [1, 2, 1, 9, 5, 0, 0, 11, 19, 11] 
#yangi_list = []
#for n in list:
   #  if n not in yangi_list:
       #  yangi_list.append(n)
     #print(yangi_list)
     
     #sonlar ustida amallar 8 daraja ikki listni takrorlarsiz va takrorlanadigan qilib birlashtirish
     #takrorlanmaydigan qilib birlashtirish
#list1 = [1, 3, 6, 9, 11]
#list2 = [2, 3, 5, 10, 11]
#result = []
#for x in list1:
   # if x not in result:
       # result.append(x)
#for x in list1:
   # if x not in result:
        #result.append(x)
#print(result)
#extend() funksiyasidan foydalanib qoshish
#list1.extend(list2)
#print(list1)

#lists ustida amallar 9 daraja list ichidagi elementlarni almashtirish
#list = [1, 3, 6, 9, 11, 15, 19]
#start = 0
#end = len(list) - 1
#while start < end:
 #   list[start], list[end] = list[end], #list[start]
  #  start += 1
 #   end-= 1
#print(list)

#list ustida amallar 10 daraja elementlarni indexiga kopaytirish
list = [1, 3, 6, 9, 11, 15, 19]
new = []
for i, val in enumerate(list):
    new. append(i * val)
print(new)