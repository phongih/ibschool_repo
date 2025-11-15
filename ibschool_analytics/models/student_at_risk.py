# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StudentAtRisk(models.Model):
    _name = 'ibschool.student_at_risk'
    _description = 'StudentAtRisk model'

    name = fields.Char(string='Name', required=True)
