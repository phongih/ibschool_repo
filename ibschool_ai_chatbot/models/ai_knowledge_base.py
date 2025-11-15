# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AiKnowledgeBase(models.Model):
    _name = 'ibschool.ai_knowledge_base'
    _description = 'AiKnowledgeBase model'

    name = fields.Char(string='Name', required=True)
