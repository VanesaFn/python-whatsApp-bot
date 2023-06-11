import json
import requests
import datetime

from Info_carreer import (
    Administracion_de_Empresas,
    Derecho,
    Licenciatura_en_Educacion_Infantil,
    Contaduria_Publica,
    Software,
    Ambiental,
    Electronica,
    Finanzas,
    Ingeniería_Energetica,
    Gobierno_Relaciones_Internacionales,
    Matematicas,
    Ing_civil,
    inscripcion,
    Oferta,
    homologacion,
    reingreso,
)

class ultraChatBot():    
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['data']
        self.ultraAPIUrl = 'https://api.ultramsg.com/instance50370/'
        self.token = '2830g2heterp7efd'

   
    def send_requests(self, type, data):
        url = f"{self.ultraAPIUrl}{type}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def send_message(self, chatID, text):
        data = {"to" : chatID,
                "body" : text}  
        answer = self.send_requests('messages/chat', data)
        return answer

    ############# #informacion carreras ##########
    def Info_carrera(self,chatID):
        info_programa="Genial, ¿que carrera quieres conocer?\n\n 1) Derecho \n\n 2) Administración de Empresas \n\n 3) Licenciatura en Educación Infantil \n\n 4) Contaduría Pública \n\n 5) Ingeniería de Software y Computación \n\n 6) Ingeniería Ambiental y de Saneamiento \n\n 7) Ingeniería Electrónica \n\n 8) Ingeniería Energética \n\n 9) Gobierno y Relaciones Internacionales \n\n 10) Finanzas y negocios Internacional \n\n 11) Ingeniería civil \n\n  l2) Matemáticas aplicadas en Ciencias de datos "
        return self.send_message(chatID,info_programa)
    
    def Derecho_(self, chatID):
        Info_Derecho = Derecho 
        return self.send_message(chatID, Info_Derecho)
    
    def Administracion_(self, chatID):
        Info_Administracion = Administracion_de_Empresas
        return self.send_message(chatID, Info_Administracion)
    
    def Licenciatura_(self, chatID):
        Info_Licenciatura = Licenciatura_en_Educacion_Infantil 
        return self.send_message(chatID, Info_Licenciatura)

    def Contaduria_(self, chatID):
        Info_Contaduria = Contaduria_Publica
        return self.send_message(chatID, Info_Contaduria)

    def Software_(self, chatID):
        Info_Software = Software
        return self.send_message(chatID, Info_Software)
    
    def Ambiental_(self, chatID):
        Info_Ambiental = Ambiental
        return self.send_message(chatID, Info_Ambiental)
    
    def Electronica_(self, chatID):
        Info_Electronica = Electronica
        return self.send_message(chatID, Info_Electronica)

    def Enegertica_(self, chatID):
        Info_Enegertica = Ingeniería_Energetica
        return self.send_message(chatID, Info_Enegertica)
    
    def Gobierno_y_relaciones_int_(self, chatID):
        Info_Gobierno_y_relaciones_int_ = Gobierno_Relaciones_Internacionales
        return self.send_message(chatID, Info_Gobierno_y_relaciones_int_)
    
    def Finanzas_(self, chatID):
        Info_Finanzas = Finanzas
        return self.send_message(chatID, Info_Finanzas)
    
    def Civil_(self, chatID):
        Info_Civil= Ing_civil
        return self.send_message(chatID, Info_Civil)

    def Matematicas_(self, chatID):
        Info_Matematicas= Matematicas
        return self.send_message(chatID, Info_Matematicas)
    
    ######################

    def Oferta_academica(self,chatID):
        oferta=Oferta
        return self.send_message(chatID,oferta)
    
    def Inscripcion(self,chatID):
        inscripcion_= inscripcion
        return self.send_message(chatID,inscripcion_)

    def Reingreso(self,chatID):
        reingreso_= reingreso
        return self.send_message(chatID,reingreso_)

    def Homologacion_(self,chatID):
        homologacion_= homologacion
        return self.send_message(chatID,homologacion_)



    def welcome(self,chatID, noWelcome = False):
        welcome_string = ''
        if (noWelcome == False):
            welcome_string = "💙¡Bienvenido al ChatBot de la Uniautonoma del Cauca!💙"
        else:
            welcome_string = """💙¡Bienvenido al ChatBot de la Uniautonoma del Cauca!💙
            ¿Que deseas saber?:
a.Información por programa 
b.Información Proceso de inscripción
c.Oferta Academica
d.Solicitud Reingreso 
e.Proceso Homologación
            """
        return self.send_message(chatID, welcome_string)


    def Processingـincomingـmessages(self):
        if self.dict_messages != []:
            message =self.dict_messages
            text = message['body'].split()
            if not message['fromMe']:
                chatID  = message['from'] 
                if text[0].lower() == '':
                    return self.welcome(chatID)
                elif text[0].lower() == 'a':
                    return self.Info_carrera(chatID)
                elif text[0].lower() == 'b':
                    return self.Inscripcion(chatID)
                elif text[0].lower() == 'c':
                    return self.Oferta_academica(chatID)
                elif text[0].lower() == 'd':
                    return self.Reingreso(chatID)
                elif text[0].lower() == 'e':
                    return self.Homologacion_(chatID)
                elif text[0].lower() == '1':
                    return self.Derecho_(chatID)
                elif text[0].lower() == '2':
                    return self.Administracion_(chatID)
                elif text[0].lower() == '3':
                    return self.Licenciatura_(chatID)
                elif text[0].lower() == '4':
                    return self.Contaduria_(chatID)
                elif text[0].lower() == '5':
                    return self.Software_(chatID)
                elif text[0].lower() == '6':
                    return self.Ambiental_(chatID)
                elif text[0].lower() == '7':
                    return self.Electronica_(chatID)
                elif text[0].lower() == '8':
                    return self.Enegertica_(chatID)
                elif text[0].lower() == '9':
                    return self.Gobierno_y_relaciones_int_(chatID)
                elif text[0].lower() == '10':
                    return self.Finanzas_(chatID)
                elif text[0].lower() == '11':
                    return self.Civil_(chatID)
                elif text[0].lower() == '12':
                    return self.Matematicas_(chatID)
                else:
                    return self.welcome(chatID, True)
            else: return 'NoCommand'


        
        