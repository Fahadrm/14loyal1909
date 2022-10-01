# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    creditdebit_restriction = fields.Boolean(string='Credit Debit Restriction',
                                       help="Restrict credit debit")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            creditdebit_restriction=params.get_param('loyal_debit_and_credit_value_restriction.creditdebit_restriction') or False,
        )
        return res

    def set_values(self):
        self.ensure_one()
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param("loyal_debit_and_credit_value_restriction.creditdebit_restriction", self.creditdebit_restriction)