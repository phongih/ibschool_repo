# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolStudentFee(models.Model):
    _name = 'ibschool.school_student_fee'
    _description = 'SchoolStudentFee model'

    name = fields.Char(string='Name', required=True)
