# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolGradeEntry(models.Model):
    _name = 'ibschool.school_grade_entry'
    _description = 'SchoolGradeEntry model'

    name = fields.Char(string='Name', required=True)
