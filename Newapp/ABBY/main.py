
import webapp2
import json
import logging


import urllib
import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        giphy_data_source = urllib.urlopen(
            "https://maps.googleapis.com/maps/api/directions/json?origin=75+9th+Ave+New+York+NY&destination=MetLife+Stadium+1+MetLife+Stadium+Dr+East+Rutherford,+NJ+07073&key=AIzaSyAhNTiS82HV5JfoIwC-7G53AqZ9XqCRr08")
        giphy_json_content = giphy_data_source.read()
        parsed_giphy_dictionary = json.loads(giphy_json_content)
        #gif_url = parsed_giphy_dictionary[0]
        self.response.write(parsed_giphy_dictionary)

class latlongHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('address.html')
        self.response.out.write(main_template.render())
    def post(self):
        o_address = self.request.get("o_address")
        d_address = self.request.get("d_address")
        logging.info("QUERY:" + o_address)
        #query = self.request.get('q')
        #logging.info("QUERY:" + query)

        base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
        url_params = {'address': o_address,'key': 'AIzaSyAhNTiS82HV5JfoIwC-7G53AqZ9XqCRr08'}

        geocode_response = urllib.urlopen(base_url + urllib.urlencode(url_params)).read()
        json_data = json.loads(geocode_response)
        logging.info(json_data['results'][0]['geometry']['location'])
        o_template_dicts = json_data['results'][0]['geometry']['location']

        url_params = {'address': d_address,'key': 'AIzaSyAhNTiS82HV5JfoIwC-7G53AqZ9XqCRr08'}

        geocode_response = urllib.urlopen(base_url + urllib.urlencode(url_params)).read()
        json_data = json.loads(geocode_response)
        logging.info(json_data['results'][0]['geometry']['location'])
        d_template_dicts = json_data['results'][0]['geometry']['location']


        lat_template = env.get_template('mapdir.html')
        template_dicts = {'o_lat': o_template_dicts['lat'], 'o_long' : o_template_dicts['lng'], 'd_lat':d_template_dicts['lat'], 'd_long' : d_template_dicts['lng'], 'uber_quote': 7.99}
        self.response.write(lat_template.render(template_dicts))
        #request_str='/mapdir?lat=%s&lng=%s' % (d_template_dicts['lat'],d_template_dicts['lng'])
        #self.redirect(request_str)

class MapHandler(webapp2.RequestHandler):
    def get (self):
        lat = self.request.get('lat')
        lng = self.request.get('lng')
        template_values = {'name':'YOUR_USER_NAME', 'lat': lat, 'lng': lng}

        template = env.get_template('map.html')
        self.response.write(template.render(template_values))



class GipHandler(webapp2.RequestHandler):
    def get(self):
        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q': 'cristiano ronaldo', 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}

        giphy_response = urllib.urlopen(base_url + urllib.urlencode(url_params)).read()
        json_data =json.loads(giphy_response)
        img_url = json_data['data'][0]['images']['original']['url']
        template_vars= {'url': img_url}

        main_template = env.get_template('abby.html')
        self.response.out.write(main_template.render(template_vars))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/gip', GipHandler),
    ('/lat', latlongHandler),
    ('/map', MapHandler)
], debug=True)
