# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolYearGroup(models.Model):
    _name = 'ibschool.school_year_group'
    _description = 'SchoolYearGroup model'

    name = fields.Char(string='Name', required=True)
