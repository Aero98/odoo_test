from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Supplier(models.Model):
    _name = 'material.supplier'
    _description = 'Supplier'

    name = fields.Char(string='Name', required=True)
