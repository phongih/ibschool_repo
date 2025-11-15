# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolTransportRegistration(models.Model):
    _name = 'ibschool.school_transport_registration'
    _description = 'SchoolTransportRegistration model'

    name = fields.Char(string='Name', required=True)
