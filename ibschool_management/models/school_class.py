# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolClass(models.Model):
    _name = 'ibschool.school_class'
    _description = 'SchoolClass model'

    name = fields.Char(string='Name', required=True)
