class Appointments():

    def __init__(self, appointments:dict[str,dict])->None:
        self.appointments = appointments
    
    def schedule_appointments (self, app_id:str, data:str)->dict|str:

        if app_id in self.appointments:
            print("Errore")
        
        else:
            self.appointments[app_id] = {'data': "2 Ottobre", "programmato":True}

            return self.appointments[app_id]
    
    def reschedule_appointments (self, app_id:str, nuova_data:str)->dict|str:

        if app_id not in self.appointments:
            print("Errore")
        
        else:
            self.appointments[app_id] ["data"] = ["nuova_data" : "3 Ottobre"]

            return self.appointments[app_id]
    
    def cancel_appointments (self, app_id:str)->dict|str:

        if app_id in self.appointments:
            print("Errore")
        
        else:
            self.appointments[app_id] ["programmato"] = False

            return self.appointments[app_id]
    
    def remove_appointments (self, app_id:str, data:str)->dict|str:

        if app_id in self.appointments:
            print("Errore")
        
        else:
            x = self.appointments.pop(app_id) 

            return x