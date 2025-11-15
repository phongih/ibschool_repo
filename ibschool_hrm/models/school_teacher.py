# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolTeacher(models.Model):
    _name = 'ibschool.school_teacher'
    _description = 'SchoolTeacher model'

    name = fields.Char(string='Name', required=True)
