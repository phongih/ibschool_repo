# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolFeeCategory(models.Model):
    _name = 'ibschool.school_fee_category'
    _description = 'SchoolFeeCategory model'

    name = fields.Char(string='Name', required=True)
