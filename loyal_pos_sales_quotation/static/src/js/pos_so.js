odoo.define('loyal_pos_sales_quotation.pos_so', function (require) {
"use strict";

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');
    const { isConnectionError } = require('point_of_sale.utils');

    class SOCreateButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this.onClick);
        }

        async onClick() {
            var order_lines = this.env.pos.get_order().get_orderlines();
            var flag_negative = false;
            for (var line in order_lines){
            if (order_lines[line].quantity < 0){
                    flag_negative = true;
                }
            }
            if(this.env.pos.get_order().get_orderlines().length > 0 && this.env.pos.get_client() && flag_negative == false && this.env.pos.get_order().get_total_with_tax()>0){
                this.showPopup('SOCreatePopup');
            }
            else if(flag_negative == true){
                this.showPopup('ErrorPopup', {
                      title: this.env._t('Alert: Invalid Order'),
                      body: this.env._t('Negative Quantity is Not Allowed'),
                  });
            }
            else if(this.env.pos.get_order().get_orderlines().length == 0 || this.env.pos.get_order().get_total_with_tax() <=0){
                this.showPopup('ErrorPopup',{
                    title: this.env._t('Alert: Invalid Order'),
                    body: this.env._t('Please Add Some Order Lines'),
                });
            }
            else{
                this.showPopup('ErrorPopup',{
                    title: this.env._t('Alert: Invalid Customer'),
                    body: this.env._t('Please Select Customer'),
                });
            }
        }
    }
    SOCreateButton.template = 'SOCreateButton';

    ProductScreen.addControlButton({
        component: SOCreateButton,
        condition: function() {
            return true;
        },
    });

    Registries.Component.add(SOCreateButton);

    return SOCreateButton;

});