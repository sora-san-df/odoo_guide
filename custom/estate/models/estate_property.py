from odoo import fields, models, api


class EstateProperty(models.Model):

    _name = "estate.property"

    _description = "this is a estate property module"


    name = fields.Char(required=True)

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")

    property_tag_id = fields.Many2many("estate.property.tag", string="Property Tag")

    sales_person_id = fields.Many2one('res.users', string='Sales person', default=lambda self: self.env.user)

    buyer_person_id = fields.Many2one('res.partner', string="Buyer", copy="False")

    offers_id = fields.One2many("estate.property.offer", "property_id", string="Property Offer")

    description = fields.Text()

    postcode = fields.Char()

    date_availability = fields.Date(copy=False, default=lambda self: fields.Datetime.today())

    expected_price = fields.Float(required=True)

    #This should be read only

    selling_price = fields.Float(readonly=True, copy=False)

    bedrooms = fields.Integer(default=2)

    living_area = fields.Integer()

    facades = fields.Integer()

    garage = fields.Boolean()

    garden = fields.Boolean()

    garden_area = fields.Integer()

    garden_orientation = fields.Selection(

        selection=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West')]
    )

    #active 

    active = fields.Boolean(string="Active", default=False)

    #State field

    state = fields.Selection(
        selection=[('New','New'), ('Offer Received','Offer Received'), ('Offer Accepted','Offer Accepted'), ('Sold','Sold'), ('Canceled','Canceled')],
        required=True, copy=False, default='New')

    total_area = fields.Integer(compute="_compute_area")

    best_price = fields.Float(compute="_best_price")

    @api.depends("living_area", "garden_area")
    def _compute_area(self):
        for record in self: 
            record.total_area = record.living_area + record.garden_area

    @api.depends("offers_id.price")
    def _best_price(self):
        for record in self: 
            record.best_price = max(record.offers_id.mapped('price'))

    
