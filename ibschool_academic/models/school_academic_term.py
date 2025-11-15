# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolAcademicTerm(models.Model):
    _name = 'ibschool.school_academic_term'
    _description = 'SchoolAcademicTerm model'

    name = fields.Char(string='Name', required=True)
