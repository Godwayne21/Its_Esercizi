'''
Sviluppa un sistema per la gestione dei contatti in Python che permetta agli utenti di
creare, modificare, e cercare contatti basati sui numeri di telefono. Il sistema dovrà
essere capace di gestire una collezione (dizionario) di contatti e i loro numeri di telefono.
'''

class ContactManager:

    def __init__(self, contacts:dict[str:list[str]])->None:
        self.contacts = contacts

    
    def create_contact(self, name: str, phone_numbers: list[str]) -> dict:

        for name,phone_numbers in self.contacts.items():

            if name not in self.contacts:

                self.contacts[name] = list(phone_numbers)
                return self.contacts
            
            else:
                raise FileExistsError('Errore: il contatto esiste già.')
            
    
    def add_phone_number(self, contact_name: str, phone_number: str) -> dict:

        for contact_name, phone_number in self.contacts.items():

            if contact_name not in self.contacts:
                raise FileNotFoundError('Errore: il contatto non esiste.')
            
            elif phone_number in self.contacts[contact_name]:
                raise FileExistsError ('Errore: il numero di telefono esiste già.')
            
            else:
                self.contacts[contact_name] = list.append(phone_number)
                return self.contacts
            
    
    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict:

        for contact_name,phone_number in self.contacts.items():

            if contact_name not in self.contacts:
                raise FileNotFoundError ('Errore: il contatto non esiste.')
            
            elif phone_number not in self.contacts:
                raise FileNotFoundError ('Errore: il numero di telefono non è presente.')

            else:
                self.contacts [contact_name] = list.pop(phone_number)
                return self.contacts
    
    def  update_phone_number(self,contact_name: str, old_phone_number: str, new_phone_number: str)-> dict:

        for contact_name,old_phone_number in self.contacts.items():

            if contact_name not in self.contacts:
                raise FileNotFoundError ('Errore: il contatto non esiste.')
            
            elif old_phone_number not in self.contacts[contact_name]:
                raise FileNotFoundError ('Errore: il numero di telefono non è presente.')
            
            else:
                self.contacts [contact_name] = [new_phone_number]
                return self.contacts
    
    def list_contacts(self)->list:
        contacts = []
        for key in self.contacts:
            contacts.append(key)
        
        return contacts
    
    def list_phone_numbers(self, contact_name: str)->list:

        for contact_name in self.contacts:
            return self.contacts [contact_name]
    
    def search_contact_by_phone_number(self, phone_number: str)->list:

        for key in self.contacts:

            if phone_number in self.contacts [key]:

                return self.contacts[key]