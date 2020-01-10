class Confectionery_enterprise:
    def __init__(self, address, faculty_count, accreditation, rating):
        self.address = address
        self.faculty_count = name
        self.accreditation = spicial
        self.rating = rating

    def get_address(self):
        return self.address

    def get_name(self):
        return self.name

    def get_special(self):
        return self.special

    def get_rating(self):
        return self.rating

    def get_info(self):
        print('{0}-{1}-{2}-{3}'.format(self.address, self.name, self.special, self.rating))

class Confectioner:
    def __init__(self):
        self.confectionery_enterprises = []

    def add_uni(self, new_uni):
        self.confectionery_enterprises.append(new_uni)

    def get_uni(self):
        return self.confectionery_enterprises


confectionery_enterprises_confectioner = []

confectionery_enterprises1 =confectioner ()
confectionery_enterprises1.add_con(University('Uzhhorod, Universitetska, 14', 15, 4, 24))
confectionery_enterprises1.add_con(University('Kyiv, Shevchenka, 123', 12, 4, 5))
confectionery_enterprises1.add_con(University('Lviv, Lisova, 34', 12, 3, 34))
confectionery_enterprises1.add_con(University('Kyiv, Franka, 135', 15, 3, 32))
confectionery_enterprises.append(university1)

while True:
    print('Search by: (address, name, special, rating), exit')
    choice = input('Search by: ')
    if choice == 'exit':
        break
    elif choice == 'address':
        user_address = input('Address: ')
        for con in confectionery_enterprises:
            for co in con.get_con():
                if co.get_address() == user_address:
                    print(co.get_info())
    elif choice == 'name':
        user_name = int(input('name: '))
        for con in confectionery_enterprises:
            for co in con.get_con():
                if co.get_name() == user_name:
                    print(co.get_info())
    elif choice == 'special':
        user_special = int(input('special: '))
        for con in confectionery_enterprises:
            for co in con.get_con():
                if co.get_special() == user_special:
                    print(co.get_info())
    elif choice == 'rating':
        user_rating = int(input('Rating: '))
        for con in confectionery_enterprises:
            for co in con.get_con():
                if co.get_rating() == user_rating:
                    #print(un.get_info())
                    co.get_info()
    else:
        print('Try again!')