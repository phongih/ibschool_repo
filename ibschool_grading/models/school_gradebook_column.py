# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolGradebookColumn(models.Model):
    _name = 'ibschool.school_gradebook_column'
    _description = 'SchoolGradebookColumn model'

    name = fields.Char(string='Name', required=True)
