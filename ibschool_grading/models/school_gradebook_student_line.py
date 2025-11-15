# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolGradebookStudentLine(models.Model):
    _name = 'ibschool.school_gradebook_student_line'
    _description = 'SchoolGradebookStudentLine model'

    name = fields.Char(string='Name', required=True)
