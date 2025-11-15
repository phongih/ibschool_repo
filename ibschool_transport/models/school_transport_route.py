# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolTransportRoute(models.Model):
    _name = 'ibschool.school_transport_route'
    _description = 'SchoolTransportRoute model'

    name = fields.Char(string='Name', required=True)
