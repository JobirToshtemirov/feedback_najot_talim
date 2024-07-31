"""
Skuturlarni ijaraga minish uchun dastur tuzish kerak
admin odam sukuturlar haqida malumot kiritadi
masalan, qancha zaryadi bor ekani, qayerda turgani, 1 daqiqalik narxi, id(random bo'lgani yaxshi)

Foydalanuvchi esa skuterni id si orqali banq qilishi mumkin bo'ladi
Va unda to'xtatish degan funksiya ham bo'lishi kerak
agar u ushani ishlatsa unga necha pul bo'lganini hisoblab chiqarib berish kerak

Uning uchun ijaraga olgan vaqtini file da saqlab ketish kerak, va to'xtatish vaqtidan uni ayirib hisoblab berish kerak
Qo'shimcha qulayliklar qo'shishingiz ham mumkin

"""
"""
Arxitektura:
    1.class file manager for save data
        1.1 load data
        1.2 save data
        1.3 get data 
        1.4 update data
        1.5 delete data
    2.class admin
        2.1 add skuter
        2.2 delete skuter
    3.class user 
        3.1 rent skuter 
        3.2 return skuter 
        3.3 show all skuter
        3.4 exit
    4.menu: 
        4.1.1 rent skuter 
        4.1.2 return skuter 
        4.1.3 show all skuter
        4.1.4 admin menu:
            4.2.1 add skuter
            4.2.2 delete skuter
            4.2.3 exit main menu
        5.exit
"""
