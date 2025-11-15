# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolUnitPlan(models.Model):
    _name = 'ibschool.school_unit_plan'
    _description = 'SchoolUnitPlan model'

    name = fields.Char(string='Name', required=True)
