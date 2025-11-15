# -*- coding: utf-8 -*-
from odoo import models, fields, api

class IbschoolAcademicInherit(models.Model):
    _name = 'ibschool.ibschool_academic_inherit'
    _description = 'IbschoolAcademicInherit model'

    name = fields.Char(string='Name', required=True)
