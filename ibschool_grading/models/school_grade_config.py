# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolGradeConfig(models.Model):
    _name = 'ibschool.school_grade_config'
    _description = 'SchoolGradeConfig model'

    name = fields.Char(string='Name', required=True)
