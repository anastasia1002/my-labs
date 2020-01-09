class University:
    def __init__(self, address, faculty, accreditation, rating):
        self.address=address
        self.faculty=faculty
        self.accreditation=accreditation
        self.rating=rating


    def get_address(self):
        return self.address


    def get_faculty(self):
        return self.faculty


    def get_accreditation(self):
        return self.accreditation


    def get_rating(self):
        return self.rating


    def get_info(self):
        return " address- {0}\n faculty - {1}\n" \
               " accreditation - {2}\n rating - {3}".format(self.address, self.faculty,self.accreditation, self.rating)


class Student:
    def __init__(self):
        self.university = []

    def add_university(self):
        self.university.append()

    def get_university(self):
        return self.university

a=University()
print(a)
b=Student()
print(b)
