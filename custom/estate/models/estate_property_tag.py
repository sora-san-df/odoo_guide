from odoo import fields, models


class EstatePropertyTag(models.Model):
     _name = "estate.property.tag"

     _description = "Model for estate property tag"

     name = fields.Char(required=True)

    