# hw9

"""
1.Cheksiz takrorlanish operatori yordamida foydalanuvchidan uninig ismi va yoshini so'ralsin.
2. Kiritilgan ism va yosh users.csv fayliga saqlanib borsin.
3. Ism yoki yosh probel bilan ajratilgan holda kiritilsin.
4. Agar kiritilgan qiymat "exit" ga teng bo'lsa, unda dastur to'xtatilsin va users.csv fayli natijasi foydalanuvchiga ko'rsatilsin
"""

def write_to_csv(name, age):
    with open("users.csv", mode="a", encoding="UTF-8") as file:
        file.write(f"name {name},age {age}\n")

while True:
    user_input = input("Enter your name and age: ")
    if user_input.lower() == "exit":
        print("Program finished.")
        break

    name, age = user_input.split()

    write_to_csv(name, age)

print("Users in the CSV file:")
with open("users.csv", mode="r", encoding="UTF-8") as file:
    for line in file:
        print(line.strip())


