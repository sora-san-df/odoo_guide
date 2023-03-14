from odoo import fields, models


class EstatePropertyType(models.Model):

    _name = "estate.property.type"

    _description = "This is the description of the estate property type"

    name = fields.Char(required=True)

    property_ids = fields.One2many("estate.property","property_type_id", string="Properties")
