# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LibraryBookCopy(models.Model):
    _name = 'ibschool.library_book_copy'
    _description = 'LibraryBookCopy model'

    name = fields.Char(string='Name', required=True)
