class University:
    def __init__(self, address, faculty_count, accreditation, rating):
        self.address = address
        self.faculty_count = faculty_count
        self.accreditation = accreditation
        self.rating = rating

    def get_address(self):
        return self.address

    def get_faculty_count(self):
        return self.faculty_count

    def get_accreditation(self):
        return self.accreditation

    def get_rating(self):
        return self.rating

    def get_info(self):
        print('{0}-{1}-{2}-{3}'.format(self.address, self.faculty_count, self.accreditation, self.rating))

class StudentsUni:
    def __init__(self):
        self.universities = []

    def add_uni(self, new_uni):
        self.universities.append(new_uni)

    def get_uni(self):
        return self.universities

students_universities = []

university1 = StudentsUni()
university1.add_uni(University('Uzhhorod, Universitetska, 14', 15, 4, 24))
university1.add_uni(University('Kyiv, Shevchenka, 123', 12, 4, 5))
university1.add_uni(University('Lviv, Lisova, 34', 12, 3, 34))
university1.add_uni(University('Kyiv, Franka, 135', 15, 3, 32))
students_universities.append(university1)

while True:
    print('Search by: (address, faculties, accreditation, rating), exit')
    choice = input('Search by: ')
    if choice == 'exit':
        break
    elif choice == 'address':
        user_address = input('Address: ')
        for uni in students_universities:
            for un in uni.get_uni():
                if un.get_address() == user_address:
                    print(un.get_info())
    elif choice == 'faculties':
        user_faculties = int(input('Count of faculties: '))
        for uni in students_universities:
            for un in uni.get_uni():
                if un.get_faculty_count() == user_faculties:
                    print(un.get_info())
    elif choice == 'accreditation':
        user_accreditation = int(input('Accreditation: '))
        for uni in students_universities:
            for un in uni.get_uni():
                if un.get_accreditation() == user_accreditation:
                    print(un.get_info())
    elif choice == 'rating':
        user_rating = int(input('Rating: '))
        for uni in students_universities:
            for un in uni.get_uni():
                if un.get_rating() == user_rating:
                    #print(un.get_info())
                    un.get_info()
    else:
        print('Try again!')