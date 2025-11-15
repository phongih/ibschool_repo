# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolClassSection(models.Model):
    _name = 'ibschool.school_class_section'
    _description = 'SchoolClassSection model'

    name = fields.Char(string='Name', required=True)
