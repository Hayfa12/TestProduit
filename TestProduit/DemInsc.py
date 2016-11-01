# -*- coding: utf-8 -*-
import logging
import re
import uuid
import smtplib
from urlparse import urljoin
from collections import Counter, OrderedDict
from itertools import product

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError

from odoo.addons.website.models.website import slug

class DemInsc(models.Model):
    _name='deminsc.custom'

   
    nom = fields.Char('Nom',required=True)
    prenom = fields.Char('Prénom', required=True)
    tel = fields.Char('Téléphone',required=True)
    entreprise = fields.Char('Entreprise',required=True)
    adresse = fields.Char('Adresse',required=True)
    produit = fields.Many2one('product.template','Produits',required=True)
   
    login = fields.Char('Login',required=True)
    pwd = fields.Char('Mot de passe',required=True)
		
    def sendemail():
        
 
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("uuser1874@gmail.com", "MASGHOUNIhayfa12")
 
        msg = "YOUR MESSAGE!"
        server.sendmail("uuser1874@gmail.com", "masghouni.haifa@gmail.com", msg)
        server.quit()
    
