# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         sfp_elp_dns_resolver
# Purpose:      Spider Foot Module to get the IP from a given domain name.
# Module Name:  ELP (Enrique Lopez Patau) DNS Resolver
#
# Author:      Enrique Lopez Patau <enlopa@gmail.com>
#
# Created:     29/03/2023
# Copyright:   (c) Enrique Lopez Patau 2023
# Licence:     GPL
# -------------------------------------------------------------------------------

import socket
from spiderfoot import SpiderFootEvent, SpiderFootPlugin


class sfp_elpdnsresolver(SpiderFootPlugin):

    meta = {
        'name': "ELP DNS Resolver",
        'summary': "Resolves domain names and get the correspoding IP",
        'flags': [""],
        'useCases': ["Custom", "Investigate", "Passive"],
        'categories': ["DNS"]
    }

    # Default options
    opts = {
    }

    # Option descriptions
    optdescs = {
    }

    results = None

    def setup(self, sfc, userOpts=dict()):
        self.sf = sfc
        self.results = self.tempStorage()

        for opt in list(userOpts.keys()):
            self.opts[opt] = userOpts[opt]

    # What events is this module interested in for input
    def watchedEvents(self):
        # El módulo solo procesará eventos que envíen campos del tipo
        # DOMAIN_NAME e INTERNET_NAME
        return ["DOMAIN_NAME", "INTERNET_NAME"]
    
    # What events this module produces
    # This is to support the end user in selecting modules based on events
    # produced.
    def producedEvents(self):
        # El módulo retorna un dato del tipo IP_ADDRESS
        return ["IP_ADDRESS"]

    # Handle events sent to this module
    def handleEvent(self, event):
        # Obtenemos el ID del tipo de dato (INTERNET_NAME o DOMAIN_NAME)
        eventName = event.eventType
        # Obtenemos el nombre del modulo que produce el evento
        srcModuleName = event.module
        # Obtenemos el dato, es decir el dominio a resolver
        eventData = event.data

        if eventData in self.results:
            return

        self.results[eventData] = True

        self.sf.debug("Received event, {eventName}, from {srcModuleName}")

        try:
            # Inicializamos la variable de la respueta sin valor
            data = None

            self.sf.debug(f"We use the data: {eventData}")

            # Escribimos una traza con la información del dominio proporcionado para el que 
            # hay que obtener la IP
            self.info("Nombre de dominio a resolver: " + eventData)

            try:
                # Mediante la librería socket, consultamos la IP del dominio proporcionado
                dataToSearch = socket.gethostbyname(eventData)
                data = str(dataToSearch)
            except Exception:
                #Escribimos la traza de error sin añadir en principio el mensaje de la excepción
                self.error("Se ha producido un error o no se ha podido encontrar la IP del dominio: " + eventData)
            
            # Verificamos que la respuesta tiene algún valor
            if not data:
                # Escribimos un log de error indicando que el resultado no tiene valores
                self.sf.error("Unable to perform <ACTION MODULE> on " + eventData)
                return
        except Exception as e:
            # Escribimos la traza de error indicando el módulo y el mensaje de la excepción
            self.sf.error("Unable to perform the <ACTION MODULE> on " + eventData + ": " + str(e))
            return
        
        # Establecemos el tipo de respuesta a IP_ADDRESS
        typ = "IP_ADDRESS"

        self.info("IP encontrada para el dominio: " + eventData + ": " + data)
        
        # Generamos el evento creando una isntancia de SpiderFootEvent
        evt = SpiderFootEvent(typ, data, self.__name__, event)
        # Notificamos a todos los módulos que pueden estar interesados en el evento
        self.notifyListeners(evt)

# End of sfp_new_module class
