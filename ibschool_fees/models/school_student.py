# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolStudent(models.Model):
    _name = 'ibschool.school_student'
    _description = 'SchoolStudent model'

    name = fields.Char(string='Name', required=True)
