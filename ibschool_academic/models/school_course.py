# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolCourse(models.Model):
    _name = 'ibschool.school_course'
    _description = 'SchoolCourse model'

    name = fields.Char(string='Name', required=True)
