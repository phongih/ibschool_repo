# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LibraryCheckout(models.Model):
    _name = 'ibschool.library_checkout'
    _description = 'LibraryCheckout model'

    name = fields.Char(string='Name', required=True)
