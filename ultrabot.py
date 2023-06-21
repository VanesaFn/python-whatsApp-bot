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
    Ing_civil,
    inscripcion,
    homologacion,
    reingreso,
    gestion_integral,
    proyectos_de_desarrollo,
    pedagogia,
    defensa_derechos_humanos
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
        info_programa="Genial, ¿qué carrera quieres conocer?\n\n 1. Derecho \n\n 2. Administración de Empresas \n\n 3. Licenciatura en Educación Infantil \n\n 4. Contaduría Pública \n\n 5. Ingeniería de Software y Computación \n\n 6. Ingeniería Ambiental y de Saneamiento \n\n 7. Ingeniería Electrónica \n\n 8. Finanzas y negocios Internacionales \n\n 9. Ingeniería civil \n\n 💙 Para regresar a nuestro menú principal escribe: menú 💙 "
        return self.send_message(chatID,info_programa)
    
    def Info_especializacion(self,chatID):
        info_especializacion="Genial, ¿En qué especialización estás interesado?\n\n 10. Especialización en Gestión Integral del Riesgo de Desastres \n\n 11. Especialización en Proyectos de Desarrollo \n\n 12. Especialización en Pedagogía \n\n 13. Especialización en Promoción y Defensa de los Derechos Humanos \n\n 💙 Para regresar a nuestro menú principal escribe: menú 💙 "
        return self.send_message(chatID,info_especializacion)
    
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
    
    def Finanzas_(self, chatID):
        Info_Finanzas = Finanzas
        return self.send_message(chatID, Info_Finanzas)
    
    def Civil_(self, chatID):
        Info_Civil = Ing_civil
        return self.send_message(chatID, Info_Civil)
    
    def Gestion_(self, chatID):
        Info_gestion = gestion_integral
        return self.send_message(chatID, Info_gestion)
    
    def Proyectos_(self, chatID):
        Info_proyectos = proyectos_de_desarrollo
        return self.send_message(chatID, Info_proyectos)
    
    def Pedagogia_(self, chatID):
        Info_pedagogia = pedagogia
        return self.send_message(chatID, Info_pedagogia)
    
    def Defensa_(self, chatID):
        Info_defensa = defensa_derechos_humanos
        return self.send_message(chatID, Info_defensa)
    
    ######################
    
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
            welcome_string = "💙¡Bienvenido al ChatBot de la Uniautónoma del Cauca!💙"
        else:
            welcome_string = """💙¡Hola Soy kime, Bienvenido a la Uniautónoma del Cauca!💙
                Estoy listo para ayudarte.
                Elige una opción:
            
a. ¿Quieres conocer nuestros programas? 
b. ¿Cómo realizo mi inscripción?
c. ¿Quieres regresar a la UniAutonoma?
d. ¿Quieres hacer un proceso de Homologación?
e. ¿Deseas conocer nuestras especializaciones?
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
                    return self.Reingreso(chatID)
                elif text[0].lower() == 'd':
                    return self.Homologacion_(chatID)
                elif text[0].lower() == 'e':
                    return self.Info_especializacion(chatID)
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
                    return self.Finanzas_(chatID)
                elif text[0].lower() == '9':
                    return self.Civil_(chatID)
                elif text[0].lower() == '10':
                    return self.Gestion_(chatID)
                elif text[0].lower() == '11':
                    return self.Proyectos_(chatID)
                elif text[0].lower() == '12':
                    return self.Pedagogia_(chatID)
                elif text[0].lower() == '13':
                    return self.Defensa_(chatID)
                else:
                    return self.welcome(chatID, True)
            else: return 'NoCommand'


        
        