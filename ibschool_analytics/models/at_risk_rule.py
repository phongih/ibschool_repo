# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AtRiskRule(models.Model):
    _name = 'ibschool.at_risk_rule'
    _description = 'AtRiskRule model'

    name = fields.Char(string='Name', required=True)
