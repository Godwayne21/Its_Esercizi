class AppointmentScheduler():

    def __init__(self, appointments:dict[str,dict])->None:
        self.appointments = appointments
    
    def schedule_appointment (self, app_id:str, data:str)->dict|str:

        if app_id in self.appointments:
            return  "Errore: appuntamento esiste già."
        
        else:
            self.appointments[app_id] = {'data': data, "programmato":True}

            return self.appointments[app_id]
    
    def reschedule_appointment (self, app_id:str, nuova_data:str)->dict|str:

        if app_id not in self.appointments:
            return "Errore: appuntamento non trovato."
        
        else:
            self.appointments[app_id] ["data"] = nuova_data

            return self.appointments[app_id]
    
    def cancel_appointment (self, app_id:str)->dict|str:

        if app_id not in self.appointments:
            return "Errore: appuntamento non trovato."
        
        else:
            self.appointments[app_id] ["programmato"] = False

            return self.appointments[app_id]
    
    def remove_appointment (self, app_id:str)->dict|str:

        if app_id in self.appointments:
            return "Errore: appuntamento non trovato."
        
        else:
            return self.appointments.pop(app_id)
    
    def list_appointment (self)->dict:
        return self.appointments
    
    def get_appointment (self, app_id:str)->dict|str:

        if app_id not in self.appointments:
            return "Errore: appuntamento non trovato."
        
        else:
            return self.appointments[app_id]