# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolAcademicYear(models.Model):
    _name = 'ibschool.school_academic_year'
    _description = 'SchoolAcademicYear model'

    name = fields.Char(string='Name', required=True)
