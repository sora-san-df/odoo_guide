from odoo import fields, models


class EstatePropertyTag(models.Model):
     _name = "estate.property.tag"

     _description = "Model for estate property tag"

     _sql_constraints = [
          ('unique_tag_name', 'unique(name)', 'A property must have an unique tag')
     ]

     _order = "name"
     
     name = fields.Char(required=True)

     color = fields.Integer()

    