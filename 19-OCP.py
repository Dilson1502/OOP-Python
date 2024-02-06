class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError
    

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"enviando mensaje por mail a: {self.usuario}, contenido: {self.mensaje}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"enviando mensaje por sms a: {self.usuario}, contenido: {self.mensaje}")

sms=NotificadorSMS("dalto","sms test")
mail=NotificadorEmail("pepe","mail test")

sms.notificar()
mail.notificar()