# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolParent(models.Model):
    _name = 'ibschool.school_parent'
    _description = 'SchoolParent model'

    name = fields.Char(string='Name', required=True)
