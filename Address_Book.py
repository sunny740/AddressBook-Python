class Contact:
    def __init__(self, contact_dict):
        """
        create constructor for class create contact
        :param contact_dict:
        """
        self.first_name = contact_dict.get("first_name")
        self.last_name = contact_dict.get("last_name")
        self.address = contact_dict.get("address")
        self.city = contact_dict.get("city")
        self.state = contact_dict.get("state")
        self.zipcode = contact_dict.get("zip_code")
        self.phone_number = contact_dict.get("phone_number")
        self.email_address = contact_dict.get("emailaddress")

    def __str__(self) -> str:
        """
        read input of the class and get output s all the class members
        :return:
        """
        return f"first_name = {self.first_name}\n,last_name = {self.last_name}\n,address = {self.address}\n," \
               f"city = {self.city}\n,state = {self.state}\n,zipcode = {self.zipcode}\n,phone_number = {self.phone_number}," \
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

        return contact

    def display_contact(self, first_name):
        """
        create display_contact function
        :param first_name:
        :return:
        """
        print(self.contact_dict.get(first_name))


if __name__ == '__main__':
    try:
        address_book = AddressBook()
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
            "emailaddress": email_address
        }
        contact = Contact(contact_dict)
        address_book.create_contact(contact)
        first_name = input("Enter your first name : ")
        address_book.display_contact(first_name)
    except Exception as ex:
        print(ex)