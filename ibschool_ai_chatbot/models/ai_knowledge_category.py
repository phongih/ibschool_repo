# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AiKnowledgeCategory(models.Model):
    _name = 'ibschool.ai_knowledge_category'
    _description = 'AiKnowledgeCategory model'

    name = fields.Char(string='Name', required=True)
