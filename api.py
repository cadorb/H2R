# -*- coding: UTF-8 -*-
import json

import cherrypy
import BaseHTTPServer


class RestAPI(object):
    def index(self):

        return '<form action="stepper" method="GET">' \
           '<p>Combien de tour (en degré, pas de 10) ?</p>' \
           '<p><input type="numeric" name="step" value="{}"/></p>' \
           '<p><input type="submit" value="OK" /></p>' \
           '</form>'
    index.exposed = True


    def users(self):
        # reply with json
        json_response = json.dumps([{"_id":"56db4f9090ce705d656513af","index":0,"picture":"http://placehold.it/32x32","age":23,"name":{"first":"Page","last":"Alston"},"email":"page.alston@undefined.io","phone":"+694044422","address":"836 Vernon Avenue, Ruckersville, Arkansas, 5972","registered":"Tuesday, January 7, 2014 7:59 AM"},{"_id":"56db4f9064a7c7e6aa9b528d","index":1,"picture":"http://placehold.it/32x32","age":28,"name":{"first":"Pruitt","last":"George"},"email":"pruitt.george@undefined.ca","phone":"+685646322","address":"148 High Street, Blende, Oregon, 9502","registered":"Friday, October 10, 2014 2:42 PM"},{"_id":"56db4f90b8387f37ab52df08","index":2,"picture":"http://placehold.it/32x32","age":20,"name":{"first":"Flossie","last":"Phillips"},"email":"flossie.phillips@undefined.tv","phone":"+680459224","address":"364 Hamilton Walk, Gibbsville, Virginia, 2881","registered":"Sunday, May 17, 2015 6:32 AM"},{"_id":"56db4f90bfca9b00b72586cc","index":3,"picture":"http://placehold.it/32x32","age":36,"name":{"first":"Gay","last":"Ross"},"email":"gay.ross@undefined.biz","phone":"+684757123","address":"627 Taylor Street, Wadsworth, South Carolina, 470","registered":"Thursday, February 27, 2014 5:21 PM"},{"_id":"56db4f9090324aba1f0054f5","index":4,"picture":"http://placehold.it/32x32","age":40,"name":{"first":"Colleen","last":"Carroll"},"email":"colleen.carroll@undefined.com","phone":"+696951035","address":"326 Aurelia Court, Chesterfield, Vermont, 6802","registered":"Wednesday, April 15, 2015 7:22 AM"}])
        return bytes(json_response)

    users.exposed = True

cherrypy.quickstart(RestAPI(), config ="conf.txt")