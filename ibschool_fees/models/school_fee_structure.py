# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolFeeStructure(models.Model):
    _name = 'ibschool.school_fee_structure'
    _description = 'SchoolFeeStructure model'

    name = fields.Char(string='Name', required=True)
