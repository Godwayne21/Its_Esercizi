'''
Sviluppa un sistema per la gestione dei contatti in Python che permetta agli utenti di
creare, modificare, e cercare contatti basati sui numeri di telefono. Il sistema dovrà
essere capace di gestire una collezione (dizionario) di contatti e i loro numeri di telefono.
'''

class ContactManager:

    def __init__(self, contacts:dict[str:list[str]])->None:
        if contacts is None:
            self.contacts = {}
        else:
            self.contacts = contacts

    
    def create_contact(self, name: str, phone_numbers: list[str]) -> dict:

        if name in self.contacts:
             
             raise FileExistsError('Errore: il contatto esiste già.')

        self.contacts[name] = phone_numbers
        return self.contacts  
    
    def add_phone_number(self, contact_name: str, phone_number: str) -> dict:

        if contact_name not in self.contacts:
            raise FileNotFoundError('Errore: il contatto non esiste.')
            
        if phone_number in self.contacts[contact_name]:
            raise FileExistsError ('Errore: il numero di telefono esiste già.')

        self.contacts[contact_name].append(phone_number)
        return self.contacts
            
    
    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict:

        if contact_name not in self.contacts:
            raise FileNotFoundError ('Errore: il contatto non esiste.')
            
        if phone_number not in self.contacts:
            raise FileNotFoundError ('Errore: il numero di telefono non è presente.')

        self.contacts [contact_name].remove(phone_number)
        return self.contacts
    
    def  update_phone_number(self,contact_name: str, old_phone_number: str, new_phone_number: str)-> dict:

        if contact_name not in self.contacts:
            raise FileNotFoundError ('Errore: il contatto non esiste.')
            
        if old_phone_number not in self.contacts[contact_name]:
            raise FileNotFoundError ('Errore: il numero di telefono non è presente.')

        old = self.contacts[contact_name].index(old_phone_number)
        self.contacts [contact_name] [old] = new_phone_number
        return self.contacts
    
    def list_contacts(self)->list:

        return list(self.contacts.keys())
    
    def list_phone_numbers(self, contact_name: str)->list:

        if contact_name not in self.contacts:
            raise FileNotFoundError ('Errore: il contatto non esiste.')

        return self.contacts [contact_name]
    
    def search_contact_by_phone_number(self, phone_number: str)->list:

        search = []

        for name,numbers in self.contacts.items():

            if phone_number in numbers:
                search.append(name)
            
            else:
                raise FileNotFoundError ("Nessun contatto trovato con questo numero di telefono.")
        
        return search

cm = ContactManager(None)
cm.create_contact("Giulia", ["12345"])
cm.add_phone_number("Giulia", "67890")
print(cm.list_contacts())  # ['Giulia']
print(cm.list_phone_numbers("Giulia"))  # ['12345', '67890']
cm.update_phone_number("Giulia", "12345", "99999")
print(cm.list_phone_numbers("Giulia"))  # ['99999', '67890']
print(cm.search_contact_by_phone_number("67890"))  # ['Giulia']