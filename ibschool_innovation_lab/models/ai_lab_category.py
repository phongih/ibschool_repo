# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AiLabCategory(models.Model):
    _name = 'ibschool.ai_lab_category'
    _description = 'AiLabCategory model'

    name = fields.Char(string='Name', required=True)
