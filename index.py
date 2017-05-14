# -*- coding: UTF-8 -*-
import cherrypy
import functions
 
class Bienvenue(object):
    def index(self):
        step = functions.readfile()
        return '<form action="stepper" method="GET">' \
           '<p>Combien de tour (en degré, pas de 10) ?</p>' \
           '<p><input type="numeric" name="step" value="{}"/></p>' \
           '<p><input type="submit" value="OK" /></p>' \
           '</form>'.format(step)
    index.exposed = True


    def stepper(self, step):
        old_step = functions.readfile() # 360
        new_step = int(step) # 60
        if new_step > 360 : new_step = 0
        functions.writefile(new_step)

        if functions.rotor(old_step,new_step):

            return '''
            <p>Tour terminé</p>
            <p><a href="./">Retour</a></p>
            '''
        else :
            return '''
            <p>Erreur</p>
            <p><a href="./">Retour</a></p>
            '''
    stepper.exposed = True

cherrypy.quickstart(Bienvenue(), config ="conf.txt")




