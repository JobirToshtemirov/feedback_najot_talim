import json


class FileManager:
    @staticmethod
    def read_func(file_name):
        try:
            with open(file_name, 'r') as f:
                data = json.load(fp=f)
                return data
        except FileNotFoundError:
            with open(file_name, 'w') as f:
                json.dump({}, fp=f)
                return {}

    @staticmethod
    def write_func(data, file_name):
        with open(file_name, 'w') as f:
            json.dump(data, fp=f, indent=4)
            return True


def get_key(file_name):
    data_index = 0
    file_manager = FileManager()
    result_read = file_manager.read_func(file_name=file_name)
    try:
        data_index = int(list(result_read.keys())[-1]) + 1
    except Exception:
        data_index += 1
    return data_index


class Teacher(FileManager):
    file_name = 'teacher.json'

    def create_teacher(self, name, phone, profession, age):
        result_data = super().read_func(file_name='teacher.json')
        result_get_key = str(get_key(file_name='teacher.json'))
        if self.get_teacher(phone=phone):
            print(f'This teacher is already registered')
            return show_menu()
        result_data.update({f"{result_get_key}": {
            'name': name,
            'phone': phone,
            'profession': profession,
            'age': age
        }})
        super().write_func(data=result_data, file_name='teacher.json')
        print(f'Teacher {name} created')
        return show_menu()

    def get_teacher(self, phone):
        result_read = super().read_func(file_name=self.file_name)
        isThere = False
        try:
            for data in result_read.values():
                if phone == data['phone']:
                    isThere = data
                    break
            return isThere

        except FileNotFoundError:
            return f'Teacher is not found'
        except IndexError:
            return f'Teacher is not found'
        except TypeError:
            return f'Teacher is not found'

    def get_all_teachers(self):
        result_read = super().read_func(file_name=self.file_name)
        try:
            for data in result_read.values():
                print(f'Teacher name: {data["name"]}, phone: {data["phone"]}')
        except IndexError:
            return f'Data is not found'

    def delete_teacher(self, phone_number):
        try:
            if not self.get_teacher(phone=phone_number):
                print(f'Teacher not found')
                return show_menu()
            result_read = self.read_func(file_name=self.file_name)
            for index, data in result_read.items():
                if phone_number == data['phone']:
                    result_read.pop(index)
                    break
            self.write_func(data=result_read, file_name=self.file_name)
            print(f'Teacher deleted')
            return show_menu()
        except KeyError:
            return False


class Course(FileManager):
    def add_course(self, course_name, course_price, teacher_phone):
        teacher = Teacher()
        result_data = super().read_func(file_name='courses.json')
        result_get_key = str(get_key(file_name='courses.json'))
        result_get_teacher = teacher.get_teacher(teacher_phone)
        if not result_get_teacher:
            print(f'Teacher not found')
            return show_menu()
        result_data.update({f"{result_get_key}": {
            'course_name': course_name,
            'course_price': course_price,
            'teacher': result_get_teacher
        }})
        super().write_func(data=result_data, file_name='courses.json')
        print(f'Course {course_name} added to database')
        return show_menu()

    def check_course(self, course_name):
        result_read = super().read_func(file_name='courses.json')
        try:
            for data in result_read.values():
                if data['course_name'].lower() == course_name.lower():
                    return True
            return False
        except IndexError:
            return False

    def get_all_courses(self):
        try:
            result_read = super().read_func(file_name='courses.json')
            for data in result_read.values():
                print(
                    f'Course name: {data["course_name"]}, course price: {data["course_price"]}, teacher: {data["teacher"]["name"]}')
            return True
        except IndexError:
            return False

    def get_one_course(self, course_name):
        result_read = super().read_func(file_name='courses.json')
        for data in result_read.values():
            if data['course_name'].lower() == course_name.lower():
                return data
        return False

    def delete_course(self, course_name):
        try:
            result_read = super().read_func(file_name='courses.json')
            if len(result_read) == 0:
                print(f'Course is not found')
                return show_menu()
            for index, data in result_read.items():
                if data['course_name'].lower() == course_name.lower():
                    result_read.pop(index)
                    break
            super().write_func(data=result_read, file_name='courses.json')
            print(f'Course {course_name} deleted')
        except IndexError:
            print('Course not found')
        return show_menu()

    def get_registered_course(self, phone_number):
        try:
            result_read = self.read_func(file_name='registered.json')
            isThere = False
            for data in result_read.values():
                if data['phone'] == phone_number:
                    isThere = True
                    print(
                        f'Name: {data["name"]}, course name: {data["course"]["course_name"]}, phone: {data["phone"]}, email: {data["email"]}, id: {data["id"]}')
            if not isThere:
                print(f'This number is not registered')
            return show_menu()
        except IndexError:
            print('Data is not found')
            return show_menu()

    def user_by_course(self, course_name):
        try:
            result_read = self.read_func(file_name='registered.json')
            isThere = False
            for data in result_read.values():
                if data['course']['course_name'].lower() == course_name.lower():
                    isThere = True
                    print(
                        f'Name: {data["name"]}, course name: {data["course"]["course_name"]}, phone: {data["phone"]}, email: {data["email"]}, id: {data["id"]}')
            if not isThere:
                print('This course is not registered')
        except IndexError:
            print('Data is not found')
        return show_menu()


def show_menu():
    text = ''' 
1. Create a new teacher: name, phone_number, profession, age
2. Crate a course: name, price, teacher_phone_number
3. Register to course: name, email, phone_number, id
4: Delete a course: name
5: Delete a teacher: phone_number
6: Get registered courses: phone_number
7. Get users by course: course_name
8. Exit
    '''
    print(text)
    try:
        teacher = Teacher()
        course = Course()
        user_input = int(input('Enter your choice: '))
        if user_input == 1:
            teacher_name = input('Enter teacher name: ').strip()
            teacher_phone_number = int(input('Enter teacher phone number: ').strip())
            teacher_profession = input('Enter teacher profession: ').strip()
            teacher_age = int(input('Enter teacher age: ').strip())
            teacher.create_teacher(name=teacher_name, phone=teacher_phone_number, profession=teacher_profession, age=teacher_age)
        elif user_input == 2:
            teacher.get_all_teachers()
            name = input("Enter cource name: ").strip()
            price = input("Enter cource price: ").strip()
            phone_number = int(input("Enter teacher phone number: ").strip())
            if course.check_course(course_name=name):
                print(f'Course {name} already registered')
                return show_menu()
            course.add_course(course_name=name, course_price=price, teacher_phone=phone_number)
        elif user_input == 3:
            course.get_all_courses()
            user_course_name = input("Enter course name: ").strip()
            if not course.check_course(course_name=user_course_name):
                print(f'Course {user_course_name} not found')
                return show_menu()
            user_name = input("Enter your name: ").strip()
            user_phone = int(input("Enter your phone number: ").strip())
            user_email = input("Enter your email address: ").strip()
            user_id = int(input("Enter your user id: ").strip())
            result_get_key = str(get_key(file_name='registered.json'))
            result_get_course = course.get_one_course(course_name=user_course_name)
            data = {
                result_get_key: {
                    'course': result_get_course,
                    'name': user_name,
                    'phone': user_phone,
                    'email': user_email,
                    'id': user_id
                }
            }
            teacher.write_func(data=data, file_name='registered.json')
            return show_menu()
        elif user_input == 4:
            course.get_all_courses()
            user_course_name = input("Enter course name: ").strip()
            if not course.check_course(course_name=user_course_name):
                print(f'Course {user_course_name} not found')
                return show_menu()
            course.delete_course(course_name=user_course_name)
        elif user_input == 5:
            teacher_number = int(input("Enter teacher number: ").strip())
            teacher.delete_teacher(teacher_number)
        elif user_input == 6:
            user_phone = int(input("Enter your phone number: ").strip())
            course.get_registered_course(user_phone)
        elif user_input == 7:
            user_course_name = input("Enter course name: ").strip()
            course.user_by_course(user_course_name)
        elif user_input == 8:
            print("Good bye!")
            return
    except ValueError:
        print("Invalid input")
        show_menu()


if __name__ == '__main__':
    show_menu()
