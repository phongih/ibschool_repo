# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrEmployee(models.Model):
    _name = 'ibschool.hr_employee'
    _description = 'HrEmployee model'

    name = fields.Char(string='Name', required=True)
