# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolGradebook(models.Model):
    _name = 'ibschool.school_gradebook'
    _description = 'SchoolGradebook model'

    name = fields.Char(string='Name', required=True)
