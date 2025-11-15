# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolAttendanceLine(models.Model):
    _name = 'ibschool.school_attendance_line'
    _description = 'SchoolAttendanceLine model'

    name = fields.Char(string='Name', required=True)
