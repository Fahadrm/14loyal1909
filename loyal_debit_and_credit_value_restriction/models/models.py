# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError,AccessError,ValidationError
from odoo.tools import float_compare


class AccountMove(models.Model):
    _inherit = 'account.move'


    def action_post(self):
        """To check the selected customers due amount is exceed than
        blocking stage"""
        creditdebit_restriction = self.env["ir.config_parameter"].sudo().get_param(
            "loyal_debit_and_credit_value_restriction.creditdebit_restriction")

        if creditdebit_restriction == 'True':

            pay_type = ['in_refund', 'out_refund']
            for rec in self:
                reverse_moves = self.env['account.move'].search([('reversed_entry_id','=',rec.reversed_entry_id.id)])
                total_reverse_moves=0
                for revers in reverse_moves:
                    total_reverse_moves+=revers.amount_total

                if rec.reversed_entry_id and rec.move_type in pay_type:
                    if rec.amount_total > rec.reversed_entry_id.amount_total:
                        raise UserError(_(
                                "Exceeds the Invoice amount"))
                    if rec.reversed_entry_id.amount_total < total_reverse_moves:
                        raise UserError(_(
                                "Exceeds the Invoice amount"))
        return super(AccountMove, self).action_post()

class ReturnPicking(models.TransientModel):
    _inherit = "stock.return.picking"

    @api.model
    def _prepare_stock_return_picking_line_vals_from_move(self, stock_move):
        val = super()._prepare_stock_return_picking_line_vals_from_move(stock_move)
        return_lines = self.env["stock.return.picking.line"]
        creditdebit_restriction = self.env["ir.config_parameter"].sudo().get_param(
            "loyal_debit_and_credit_value_restriction.creditdebit_restriction")
        if creditdebit_restriction == 'True':
            val["quantity"] = return_lines.get_returned_restricted_quantity(stock_move)
        return val

    def _create_returns(self):
        precision = self.env["decimal.precision"].precision_get(
            "Product Unit of Measure"
        )
        creditdebit_restriction = self.env["ir.config_parameter"].sudo().get_param(
            "loyal_debit_and_credit_value_restriction.creditdebit_restriction")

        if creditdebit_restriction == 'True':
            for return_line in self.product_return_moves:
                quantity = return_line.get_returned_restricted_quantity(return_line.move_id)
                if (
                    float_compare(
                        return_line.quantity, quantity, precision_digits=precision
                    )
                    > 0
                ):
                    raise UserError(
                        _("It is not permitted to return additional quantities.")
                    )
        return super()._create_returns()


class ReturnPickingLine(models.TransientModel):
    _inherit = "stock.return.picking.line"

    @api.onchange("quantity")
    def _onchange_quantity(self):
        creditdebit_restriction = self.env["ir.config_parameter"].sudo().get_param(
            "loyal_debit_and_credit_value_restriction.creditdebit_restriction")

        if creditdebit_restriction == 'True':
            qty = self.get_returned_restricted_quantity(self.move_id)
            if self.quantity > qty:
                raise UserError(_("It is not permitted to return additional quantities."))

    def get_returned_restricted_quantity(self, stock_move):
        """This function is created to know how many products
        have the person who tries to create a return picking
        on his hand."""
        qty = stock_move.product_qty
        for line in stock_move.move_dest_ids.mapped("move_line_ids"):
            if line.state in {"partially_available", "assigned"}:
                qty -= line.product_qty
            elif line.state == "done":
                qty -= line.qty_done
        return max(qty, 0.0)
