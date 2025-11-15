# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolTransportStop(models.Model):
    _name = 'ibschool.school_transport_stop'
    _description = 'SchoolTransportStop model'

    name = fields.Char(string='Name', required=True)
