# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolTimetable(models.Model):
    _name = 'ibschool.school_timetable'
    _description = 'SchoolTimetable model'

    name = fields.Char(string='Name', required=True)
