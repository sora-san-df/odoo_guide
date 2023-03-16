from datetime import timedelta

from odoo import models, fields, api 
from odoo.exceptions import ValidationError, UserError
from odoo.tools.float_utils import float_compare, float_is_zero


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"

    _description = "The offers that can be applied to a specific property"

    _sql_constraints = [
         ('price_must_positive', 
          'check( price > 0)', 
          'A property selling must be positive.')]
    _order = "price desc"
    
    price = fields.Float()

    status = fields.Selection(selection=[('Offer Accepted', 'Offer Accepted'), ('Refused','Refused')], copy=False)

    partner_id = fields.Many2one('res.partner', required=True)

    property_id =fields.Many2one('estate.property', required=True)

    create_date = fields.Date(string="Created Date", default=lambda self: fields.Datetime.today())

    validity = fields.Integer(default=7)

    date_deadline = fields.Date(compute="_date_deadline_func", inverse="_inverse_date_deadline_func")

    property_type_id = fields.Many2one('estate.property.type', related="property_id.property_type_id", store=True)




    @api.depends("create_date", "validity")
    def _date_deadline_func(self):
        for record in self: 
            record.date_deadline = record.create_date + timedelta(days=record.validity)
    
    def _inverse_date_deadline_func(self):
        for record in self: 
            record.validity = (record.date_deadline - record.create_date).days

            
    #Confirm or cancel offers  and Set the buyer and its offer to the selling price and the buyer name.

    def offer_confirm(self):
        for record in self:
                record.status = 'Offer Accepted'

        if record.status == 'Offer Accepted':
             #Techincally we set the accepted price to selling price
             record.property_id.selling_price = record.price

             #and we set the partener tothe Buyer
             record.property_id.buyer_person_id = record.partner_id



    def offer_canceled(self):
        for record in self: 
                record.status = 'Refused'

    #Validation of selling price so it is at least 90% close to the expected price 

    @api.constrains('property_id')
    def _selling_price_close_to_expected_price(self):
         for record in self: 
              if float_is_zero(record.property_id.selling_price,3):
                   return 
              
              comparation =  float_compare(record.property_id.selling_price,record.property_id.expected_price, 2)
                
              if comparation == -1: 
                    raise ValidationError("The selling price must be at least 90'%' of the expected price. You should change your expected price to accept this offer")

    #Method that set the state to offer recieved if an offer was made, raise an error if an user create an offer lower than the existing offer.
    @api.model
    def create(self, vals):

        price = vals.get('price')
        if price:
            existing_offer = self.env['estate.property.offer'].search([('property_id', '=', vals['property_id']), ('price', '>', price)], limit=1)
            if existing_offer:
                raise UserError(f"The offer amount should be greater than {existing_offer.price}")

        offer_recived = self.env['estate.property'].browse(vals['property_id'])
        if offer_recived:
             offer_recived.write({'state':'Offer Received'})

    

        return super(EstatePropertyOffer, self).create(vals)         
    
    
