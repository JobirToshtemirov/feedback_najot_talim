# task1
#1. Foydalanuvchidan uning ismini so'rang, agar kiritilgan ism bo'sh satrga teng bo'lmasa, unda "Xush kelibsiz" matninig chiqaring va while o'z ishini to'xtatsin, agar ism kiritish o'rniga foydalanuvchi "Enter" tugmasini bosib o'tib ketsa (ism kiritmasda), unda qayta ism so'ralsin, toki ism sifatida uzunligi hech bo'lmaganda 1 ga teng bo'lmagan ism kiritilmagunicha.

# isim = input("Ismingizni kiriting: ")
# while isim.strip() == "":
#     print("Ismingizni kiriting.")
#     isim = input("Ismingizni kiriting: ")
# print("Xush kelibsiz,", isim)


# task2
# 2.while operatorini ishlatgan holda 1-100 gacha raqamlar orasida faqat juftlari chiqarilsin. Bunda for operatori yoki range ishlatilmasin, faqat while operatori orqali.


# a = 0 or 2       
# or 2 qilib ketganimni sababi 2 dan boshlasakham hato chiqmaydi 0 ni olib tashlab 2 ni qoysakham 100 gacha bolgan juft sonlarni chiqarib beradi
# while a <100:
#     print(a)
#     a +=2

# task3
#3. Foydalanuvchidan so'z kiritish so'ralsin, agar so'z "exit" so'ziga teng bo'lsa, unda dastur darhol to'xtasin, aks holatda kiritilgan so'zni uzunligi chiqarib berilsin, toki "exit" kiritilmagunicha. So'z uzunligini len() funksiyasi orqali olishingiz mumkin, masalan: len("salom") bizga 5 ni qaytaradi va shu print ga uzatilsa so'z uzunligi kelib chiqadi, masalan: print("So'z uzunligi:", len("salom")) # So'z uzunligi: 5


# a = input("biror soz kiriting:  ")
# while a !="exit":
#      print  ("soz uzunligi: ", len(a))
#      a = input("biror soz kiriting:  ")
