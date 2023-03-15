from odoo import fields, models,api


class EstatePropertyType(models.Model):

    _name = "estate.property.type"

    _description = "This is the description of the estate property type"

    _order = "sequence,name"

    name = fields.Char(required=True)
    
    sequence = fields.Integer()

    property_ids = fields.One2many("estate.property","property_type_id", string="Properties")

    offer_ids = fields.One2many("estate.property.offer", "property_type_id")

    offer_count = fields.Integer(compute="_given_offers_to_a_property")

    @api.depends('offer_ids')
    def _given_offers_to_a_property(self):
        for record in self: 
            record.offer_count = len(record.offer_ids)
