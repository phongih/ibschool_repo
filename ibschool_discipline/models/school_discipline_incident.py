# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolDisciplineIncident(models.Model):
    _name = 'ibschool.school_discipline_incident'
    _description = 'SchoolDisciplineIncident model'

    name = fields.Char(string='Name', required=True)
