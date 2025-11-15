# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = 'ibschool.library_book'
    _description = 'LibraryBook model'

    name = fields.Char(string='Name', required=True)
