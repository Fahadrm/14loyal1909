# -*- coding: utf-8 -*-
# from odoo import http


# class PosSalesOrders(http.Controller):
#     @http.route('/pos_sales_orders/pos_sales_orders', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_sales_orders/pos_sales_orders/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_sales_orders.listing', {
#             'root': '/pos_sales_orders/pos_sales_orders',
#             'objects': http.request.env['pos_sales_orders.pos_sales_orders'].search([]),
#         })

#     @http.route('/pos_sales_orders/pos_sales_orders/objects/<model("pos_sales_orders.pos_sales_orders"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_sales_orders.object', {
#             'object': obj
#         })
