import os
import jinja2
import webapp2
from models import City
import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        izbira = random.randint(0, 7)
        izbrana_drzava = seznam[izbira].drzava
        izbrano_mesto = seznam[izbira].mesto
        izbrana_slika = seznam[izbira].slika

        params = {"drzava": izbrana_drzava, "mesto": izbrano_mesto, "slika": izbrana_slika}

        return self.render_template("hello.html", params=params)

    def post(self):
        poskus = self.request.get("vnos")
        pravilen_odg = self.request.get("pravilen-odg")
        #   pravilen_drz = self.request.get("drzava-odg")
        if poskus.lower() == pravilen_odg.lower():
            iznos = "Bravo, pravilen odgovor...Uganili ste mesto ! Poskusite za novo sliko ?"
        else:
            iznos = "Napacen odgovor ! Poskusite za novo sliko ?"

        izbira = random.randint(0, 7)
        izbrana_drzava = seznam[izbira].drzava
        izbrano_mesto = seznam[izbira].mesto
        izbrana_slika = seznam[izbira].slika

        params = {"drzava": izbrana_drzava, "mesto": izbrano_mesto, "slika": izbrana_slika, "iznos": iznos}

        return self.render_template("hello.html", params=params)

seznam = []

seznam.append(City("Srbija", "Beograd", "http://www.projects.aegee.org/suct/su2015/images/SUs/BEO1_1_naslovnapozadinabeograd.jpg"))
seznam.append(City("Slovenija", "Ljubljana", "http://www.sloveniatattooconvention.com/wp-content/uploads/2015/02/Ljubljana-Dragon-Bridge-A.-Frelih.jpg"))
seznam.append(City("Hrvaska", "Zagreb", "http://www.globaltrekkers.ca/wp-content/uploads/IMG_3709-2.jpg"))
seznam.append(City("Avstrija", "Dunaj", "https://www.viennasightseeing.at/fileadmin/_processed_/csm_4_Schoenbrunn-10__c__VIENNA_SITGHTSEEING_TOURS_Bernhard_Luck_l_neu_c62a68e5ea.jpg"))
seznam.append(City("Nemcija", "Berlin", "http://travelercorner.com/wp-content/uploads/2016/06/Berlin.jpg"))
seznam.append(City("Italija", "Rim", "http://www.amalficoastdestination.com/wp-content/uploads/Stedentrip-Rome-The-Eternal-City-in-Italy.jpg"))
seznam.append(City("Angleska", "London", "http://www.universal-tourguide.com/wp-content/uploads/2016/09/discoverlondon.jpg"))
seznam.append(City("Francija", "Pariz", "http://www.socialeconomy.eu.org/sites/default/files/Paris.jpg"))

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)

# Del kode posojen iz Tilove "from Tilen import" aplikacije...Drugac pa ni slo...Hvala :)