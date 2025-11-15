# -*- coding: utf-8 -*-
from odoo import models, fields, api

class DisciplineCategory(models.Model):
    _name = 'ibschool.discipline_category'
    _description = 'DisciplineCategory model'

    name = fields.Char(string='Name', required=True)
