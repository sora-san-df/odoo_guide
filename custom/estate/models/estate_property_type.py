from odoo import fields, models


class EstatePropertyType(models.Model):

    _name = "estate.property.type"

    _description = "This is the description of the estate property type"

    _order = "sequence,name"

    name = fields.Char(required=True)
    
    sequence = fields.Integer()

    property_ids = fields.One2many("estate.property","property_type_id", string="Properties")
