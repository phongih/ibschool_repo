# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AiLabCreation(models.Model):
    _name = 'ibschool.ai_lab_creation'
    _description = 'AiLabCreation model'

    name = fields.Char(string='Name', required=True)
