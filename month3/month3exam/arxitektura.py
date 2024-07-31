"""Odamlar uylarini ijaraga bermoqchi kimdirlar esa ijaraga uy kidirmoqda. 
Sizning vazifangiz ushbu muommoga yechim berish. 
Muommoga qanday yondashish o'zingizning ixtiyoringiz, lekin unda quyidagi imkoniyatlar bo'lishi kerak.

`*- register, login, logout*`
`*- hamma ijaraga beriladigan uylarni ko'rish*`
`*- uyni ijaraga berish*`
`*- xonalar soni bo'yicha qidirish*`
`*- shahar nomi bo'yicha qidirish*`
`*- ijaraga berilayotgan uyga so'rov qoldirish(qandaydir ko'rinishda men shu uyga qiziqish bildirganimni mana shu uyni ijaraga bergan odamga bildirish kerak)*`
`*- o'zini ijaraga bergan uylarini ro'yxatini ko'rish*`
`*- ijaraga bermoqchi bo'lgan uyni o'chirib tashlash*`
`*- Qiziqish bildirganlarni ro'yxatini ko'rish*`
"""

""" Arxitektura:
1.class Filemanager
2.class RentHouse
3. main menu:
    3.1 register
    3.2 login
         rent menu:
         3.2.1 show all rent  houses
         3.2.2 rent house
         3.2.3 search with room quantity
         3.2.4 search house with city name
         3.2.5 application
         3.2.6 my rented houses
         3.2.7 delete my house
         3.2.8 my applications
         3.2.9 exit main menu
    3.3 logout
""" 