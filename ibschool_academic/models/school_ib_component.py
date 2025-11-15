# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolIbComponent(models.Model):
    _name = 'ibschool.school_ib_component'
    _description = 'SchoolIbComponent model'

    name = fields.Char(string='Name', required=True)
