import logging
logging.basicConfig(filename='Address_Book.log', encoding='utf-8', level=logging.DEBUG, filemode='a')

class Contact:
    create_contacts = 1
    display_contacts = 2
    display_company = 3
    delete_contacts = 4
    edit_contacts = 5
    quit_program = 6

    def __init__(self, contact_dict):
        """
        create constructor for class contact
        :param contact_dict:
        """
        self.first_name = contact_dict.get("first_name")
        self.last_name = contact_dict.get("last_name")
        self.address = contact_dict.get("address")
        self.city = contact_dict.get("city")
        self.state = contact_dict.get("state")
        self.zipcode = contact_dict.get("zipcode")
        self.phone_number = contact_dict.get("phone_number")
        self.email_address = contact_dict.get("email_address")

    def __str__(self) -> str:
        """
        read input of the class and get outputs all the class members
        :return:
        """
        return f"first_name = {self.first_name}, last_name = {self.last_name}, address = {self.address}," \
               f"city = {self.city}, state = {self.state}, zipcode = {self.zipcode}, " \
               f"phone_number = {self.phone_number}," \
               f"email = {self.email_address}"

class AddressBook:

    def __init__(self, addressbook_name):
        self.addressbook_name = addressbook_name
        self.contact_dict = {}

    def create_contact(self, contact_obj):
        """
        create a function name as person_information in class AddressBook
        :return:
        """
        self.contact_dict.update({contact_obj.first_name: contact_obj})

        return self.contact_dict

    def display_contact(self, first_name):
        """
        create display_contact function
        :param first_name:
        :return:
        """

        # contact_obj = self.get_contact(first_name)
        if self.get_contact(first_name) is not None:
            for k, v in self.get_contact(first_name).items():
                print(k, v.last_name, v.address, v.city, v.state, v.zipcode, v.phone_number, v.email_address)
        else:
            print("Address book not exit")

    def get_contact(self, first_name):
        """
        create get contact function
        :param first_name:
        :return:
        """
        return self.contact_dict.get(first_name)

    def delete_contact(self, fir_name):
        """
        create a function for delete the contact
        :return:
        """
        if self.get_contact(first_name=fir_name) is None:
            print("Contact not exist")
        else:
            self.contact_dict.pop(fir_name)

    def edit_contact(self, person):
        """
        create edit contact function
        :param person:
        :return:
        """
        self.contact_dict.update({person.first_name: person})


class MultipleAddressBook:

    def __init__(self):
        self.addressbook_dict = {}

    def create_contact(self):
        """
        create a function name as create_contact
        :return:
        """
        address_book_name = input("address_book_name:- ")
        address_book_obj = self.addressbook_dict.get(address_book_name)
        if address_book_obj is None:
            address_book_obj = AddressBook(address_book_name)
        first_name = input("Enter your first name:- ")
        last_name = input("Enter your last name:- ")
        address = input("Enter your address here:- ")
        city = input("Enter your city name:- ")
        state = input("Enter your state name:- ")
        zipcode = int(input("Enter your zipcode:- "))
        phone_number = int(input("Enter your phone number:- "))
        email_address = input("Enter your email_address:- ")
        contact_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "city": city,
            "state": state,
            "zip_code": zipcode,
            "phone_number": phone_number,
            "email": email_address
        }
        contact_instance = Contact(contact_dict)
        address_book_obj.create_contact(contact_instance)
        self.addressbook_dict.update({address_book_name: address_book_obj})

    def display_addressbook(self):
        """
        create a function name as display_company
        :return:
        """
        for key, value in self.addressbook_dict.items():
            print(key, value)

    def display_contact(self):
        """
        create a function name as display_contact
        :return:
        """
        input_field = input("enter addressbook name :- ")
        address_book = self.addressbook_dict.get(input_field)
        if address_book:
            address_book_name = input("enter the first name:- ")
            address_book.display_contact(address_book_name)
        else:
            print("addressbook not exist")

    def delete_contact(self):
        """
        create delete_contact function
        :return:
        """
        address_book_name = input("Enter the first name :- ")
        addressbook_obj = self.addressbook_dict.get(address_book_name)
        if addressbook_obj:
            first_name = input("Enter the first name :- ")
            addressbook_obj.delete_contact(first_name)
        else:
            print("name doesn't exist")

    def edit_contact(self):
        """
        create edit_contact function
        :return:
        """
        input_field = input("enter addressbook name :- ")
        address_book = self.addressbook_dict.get(input_field)
        if address_book:
            first_name = input("please enter the whose contact you want to edit:- ")
            if address_book.get_contact(first_name) is not None:
                last_name = input("Enter your last name:- ")
                address = input("Enter your address here:- ")
                city = input("Enter your city name:- ")
                state = input("Enter your state name:- ")
                zipcode = int(input("Enter your zipcode:- "))
                phone_number = int(input("Enter your phone number:- "))
                email_address = input("Enter your email_address:- ")

                person = Contact({
                    "first_name": first_name, "last_name": last_name, "address": address, "city": city,
                    "state": state,
                    "zipcode": zipcode, "phone_number": phone_number, "email_address": email_address
                })
                address_book.edit_contact(person)
            else:
                print("contact doesn't exist")
        else:
            print("addressbook not exit")

if __name__ == '__main__':
    multiple_add_book = MultipleAddressBook()
    try:
        # address_book = AddressBook("address")
        while True:
            print("\n1: create new contact\n2: display contact\n3: display company\n4: delete contact\n5: edit_contact"
                  "\n6: quit")
            user_input = int(input("please choose your choice:- "))
            if user_input == 1:
                multiple_add_book.create_contact()
            elif user_input == 2:
                multiple_add_book.display_contact()
            elif user_input == 3:
                multiple_add_book.display_addressbook()
            elif user_input == 4:
                multiple_add_book.delete_contact()
            elif user_input == 5:
                multiple_add_book.edit_contact()
            elif user_input == 6:
                print("you are quit the program")
            else:
                print("invalid choice")
    except Exception as e:
        logging.exception(e)
        # print(e)
