# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolPersonAbstract(models.Model):
    _name = 'ibschool.school_person_abstract'
    _description = 'SchoolPersonAbstract model'

    name = fields.Char(string='Name', required=True)
