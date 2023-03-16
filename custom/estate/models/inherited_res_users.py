from odoo import models, fields


class InheritedResUsers(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many("estate.property", "sales_person_id", domain ="['|', ('state', '=', 'New'), ('state', '=', 'Offer received')]")