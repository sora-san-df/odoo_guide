from odoo import models, fields


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"

    _description = "The offers that can be applied to a specific property"

    price = fields.Float()

    status = fields.Selection(selection=[('Accepted', 'Accepted'), ('Refused','Refused')], copy=False)

    partner_id = fields.Many2one('res.partner', requrired=True)

    property_id =fields.Many2one('estate.property', required=True)