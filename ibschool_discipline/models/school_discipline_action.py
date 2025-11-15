# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolDisciplineAction(models.Model):
    _name = 'ibschool.school_discipline_action'
    _description = 'SchoolDisciplineAction model'

    name = fields.Char(string='Name', required=True)
