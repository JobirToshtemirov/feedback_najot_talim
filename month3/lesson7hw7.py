# hw7 vazifasi
""" Student nomli class yarating va unda quyidagi amallarni bajara olishim uchun dunder methodlar yozing
undan quyidagicha attributelar bo'lishi kerak: 
full_name, 
age, 
birthday, 
gender, 
courses=[] 
biror bir objectni chaqarib unga yangi object ni berib yuborsam o'zini ichidagi courses listiga shu objectni qo'shib qo'ysin
 +, -, *, /, +=, -=, /=, *=, ** object ni uzunligini o'lchasam jami courselarni sonini chiqarib bersin
   heh qanday menyu yasash kerak emas shunchaki har bir methodni tekshirib ko'rish kerak """

# hw7 yechimi

class Student:
    def __init__(self, full_name, age, birth_day, gender):
        self.full_name = full_name
        self.age = age
        self.birth_day = birth_day
        self.gender = gender
        self.courses = []

    def __str__(self):
        return f'Student(Fullname: {self.full_name}, Age: {self.age}, Birth day: {self.birth_day}, Gender: {self.gender}, Courses: {self.courses})'

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.courses)

    def __iadd__(self, other):  # += metodi
        if isinstance(other, str): 
            self.courses.append(other)
        elif isinstance(other, Student):
            self.courses.extend(other.courses)
        return self

    def __isub__(self, other): # -= metodi
        if isinstance(other, str) and other in self.courses:
            self.courses.remove(other)
        elif isinstance(other, Student):
            for course in other.courses:
                if course in self.courses:
                    self.courses.remove(course)
        return self

    def __add__(self, other):   #qoshish metodi
        if isinstance(other, Student):
            return len(self.courses) + len(other.courses)
        return NotImplemented

    def __sub__(self, other):   #ayirish funksiyasi
        if isinstance(other, Student):
            return len(self.courses) - len(other.courses)
        return NotImplemented

    def __mul__(self, other):    # kopaytirish metodi
        if isinstance(other, Student):
            return len(self.courses) * len(other.courses)
        return NotImplemented

    def __truediv__(self, other): #bolish metodi
        if isinstance(other, Student) and len(other.courses) != 0:
            return len(self.courses) / len(other.courses)
        return NotImplemented

    def __pow__(self, other):    # darajaga oshirish metodi
        if isinstance(other, Student):
            return len(self.courses) ** len(other.courses)
        return NotImplemented

 #obyekt
student1 = Student("Toshtemirov Jobir", 21, "2003-10-06", "Male")
student2 = Student("Jobirni qarindoshi", 20, "2004-09-19", "Female")

#kurslarni qoshish yoki yaratish desaham boladi
student1 += "Math"
student1 += "Science"
student2 += "Literature"
student2 += "Art"

#kursni ayrib tashlash yoki ochirish desaham boladi
student1 -= "Math"
student2 -= "Art"

total_courses = student1 + student2  #kurslarni umumiy soni
diff_courses = student1 - student2  # kurslar sonini farqi
mul_courses = student1 * student2   #kurslar kopaytmasi
div_courses = student1 / student2  # kurslar bolinmasi
pow_courses = student1 ** student2  # kurslarni  darajaga oshirish




# print(student1, student2, total_courses, diff_courses, mul_courses, div_courses, pow_courses)

print(f" obyekt haqida malumot: {student1}")
print(f" obyekt haqida malumot: {student2}")
print(f" Jami Kurslar: {total_courses}")
print(f" kurslar sonini farqi: {diff_courses}")
print(f" kurslar kopaytmasi: {mul_courses}")
print(f" kurslar bolinmasi: {div_courses}")
print(f" kurslarni darajaga oshirish: {pow_courses}")


