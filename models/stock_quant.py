# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import Warning


class StockQuant(models.Model):
    _inherit = 'stock.quant'


    @api.multi
    def creer_stock_picking(self):
        location_id=0
        for obj in self:
            if location_id==0:
                location_id=obj.location_id.id
            if location_id!=obj.location_id.id:
                raise Warning(u"Il n'est pas possible de sélectionner des articles de plusieurs emplacements")
        vals={
            'location_id'     : location_id,
            'location_dest_id': location_id,
            'picking_type_id' : 3,
        }
        picking=self.env['stock.picking'].create(vals)
        for obj in self:
            vals={
                'picking_id'      : picking.id,
                'location_id'     : 15,
                'location_dest_id': 18,
                'procure_method'  : 'make_to_stock',
                'picking_type_id' : 3,
                'name'            : obj.product_id.name,
                'product_id'      : obj.product_id.id,
                'product_uom'     : obj.product_id.uom_id.id,
                'product_uom_qty' : obj.quantity-obj.reserved_quantity,
            }
            move=self.env['stock.move'].create(vals)
        res= {
            'name': 'Transfert',
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'stock.picking',
            'res_id': picking.id,
            'type': 'ir.actions.act_window',
        }
        return res

