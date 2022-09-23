# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    from_pos = fields.Boolean(string="Created From POS", default=False)

    def create_so_from_pos(self, orders):
        order_id = self.create(orders)
        order_ref = order_id.name
        return order_ref


class PosConfig(models.Model):
    _inherit = 'pos.config'

    warehouse_value = fields.Many2one('stock.warehouse', string="Warehouse")
