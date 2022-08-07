import logging
logging.basicConfig(filename='Address_Book.log', encoding='utf-8', level=logging.DEBUG, filemode='a')

create_contacts = 1
display_contacts = 2
quit_program = 0
delete_contact = 4

class Contact:
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
               f"city = {self.city}, state = {self.state}, zipcode = {self.zipcode}, phone_number = {self.phone_number}," \
               f"email = {self.email_address}"


class AddressBook:

    def __init__(self):
        self.contact_dict = {}

    def create_contact(self, contact_obj):
        """
        create a function name as person_information in class AddressBook
        :return:
        """
        self.contact_dict.update({contact_obj.first_name: contact_obj})

        return contact_dict

    def display_contact(self, first_name):
        """
        create display_contact function
        :param first_name:
        :return:
        """
        print(self.contact_dict.get(first_name))

    def delete_contact(self):
        """
        create a function for delete the contact
        :return:
        """

        if first_name in self.contact_dict.keys():
            self.contact_dict.pop(first_name)
            print("contact is deleted")
        else:
            print("contact doesn't exist")

    def get_contact(self, first_name):
        return self.contact_dict.get(first_name)

    def edit_contact(self, person):

        self.contact_dict.update({person.first_name: person})

    # def choice(self, input_):
    #     options = {1: AddressBook.create_contact, 2: AddressBook.display_contact, 3: AddressBook.delete_contact}
    #     return options.get(input_)()

if __name__ == '__main__':
    try:
        address_book = AddressBook()

        while True:
            print("\n1: create new contact\n2: display contact\n3: quit\n4: delete contact")
            user_input = int(input("please choose your choice:- "))
            if user_input == create_contacts:
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
                contact = Contact(contact_dict)
                address_book.create_contact(contact)
            elif user_input == display_contacts:
                first_name = input("enter the first name:- ")
                address_book.display_contact(first_name)
            elif user_input == quit_program:
                print("you are quit the program")
            elif user_input == delete_contact:
                first_name = input("Enter the first name :- ")
                address_book.delete_contact()
            elif user_input == 6:
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
                        "first_name": first_name, "last_name": last_name, "address": address, "city": city, "state":state,
                        "zipcode": zipcode, "phone_number": phone_number, "email_address": email_address
                    })
                    address_book.edit_contact(person)
                else:
                    print("contact doesn't exist")
            else:
                print("invalid choice")

    except Exception as e:
        logging.exception(e)
        # print(e)
