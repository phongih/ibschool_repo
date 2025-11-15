# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolAttendanceSheet(models.Model):
    _name = 'ibschool.school_attendance_sheet'
    _description = 'SchoolAttendanceSheet model'

    name = fields.Char(string='Name', required=True)
