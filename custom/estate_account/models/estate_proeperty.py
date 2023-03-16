from odoo import models,Command


class EstatePropertyStatus(models.Model):

    _inherit = "estate.property"

    
    def sold_button_test(self):
        print("Watashi was vampire")

        self.env['account.move'].create({
            'move_type': 'out_invoice',
            'name': 'Test',
            "invoice_line_ids":[
                Command.create({
                    "name": "Porpety Sold",
                    "price_unit": self.selling_price * 0.06 + 100.00,
                    "quantity": 1
                }),
                Command.create({
                    "name": "Administrative Fees",
                    "price_unit": 100.00,
                    "quantity": 1
                })
            ]
        })
        
        return super(EstatePropertyStatus,self).sold_button_test()
