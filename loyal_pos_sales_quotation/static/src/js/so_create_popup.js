odoo.define('loyal_pos_sales_quotation.SOCreatePopup', function(require) {
    'use strict';

    const { useState, useRef } = owl.hooks;
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');


    class SOCreatePopup extends AbstractAwaitablePopup {
        constructor() {
            super(...arguments);
            this.state = useState({
                dateValue: this.props.startingValue,
            });
            console.log(moment().format('YYYY/MM/DD'));
        }

        async createSaleOrder() {
            var sale_order = {};
            var today = new Date().toJSON().slice(0,10);
            var order = this.env.pos.get_order();
            var order_lines = this.env.pos.get_order().get_orderlines();
            var order_date = this.state.dateValue;
            var valid_date = true;
            var validatePattern = /^(\d{4})([/|-])(\d{1,2})([/|-])(\d{1,2})$/;
            if (order_date){
                var dateValues = order_date.match(validatePattern);
                if (dateValues == null){
                    valid_date = false;
                }
                else{
                    var orderYear = dateValues[1];
                    var orderMonth = dateValues[3];
                    var orderDate =  dateValues[5];
                    if ((orderMonth < 1) || (orderMonth > 12)) {
                        valid_date = false;
                    }
                    else if ((orderDate < 1) || (orderDate> 31)) {
                        valid_date = false;
                    }
                    else if ((orderMonth==4 || orderMonth==6 || orderMonth==9 || orderMonth==11) && orderDate ==31) {
                        valid_date = false;
                    }
                    else if (orderMonth == 2){
                        var isleap = (orderYear % 4 == 0 && (orderYear % 100 != 0 || orderYear % 400 == 0));
                        if (orderDate> 29 || (orderDate ==29 && !isleap)){
                            valid_date = false;
                        }
                    }
                    var dates = [orderYear,orderMonth,orderDate];
                    order_date = dates.join('-');
                }
            }
            sale_order.order_line = [];
            $('.alert_msg').text("");
            if (order_date && order_date < today || valid_date==false){
                $('.alert_msg').text("Please Select Valid Order Date!");
            }
            else{
                $('.alert_msg').text("");
                for (var line in order_lines){
                    if (order_lines[line].quantity>0)
                    {
                        var sale_order_line = [0,false,{product_id:null,product_uom_qty:0,
                        price_unit:0,discount:0}]
                        sale_order_line[2].product_id = order_lines[line].product.id;
                        sale_order_line[2].product_uom_qty = order_lines[line].quantity;
                        sale_order_line[2].price_unit = order_lines[line].price;
                        sale_order_line[2].discount = order_lines[line].discount;
                        sale_order.order_line.push(sale_order_line);
                    }
                }
                sale_order.warehouse_id = this.env.pos.config.warehouse_value[0];
                sale_order.partner_id = this.env.pos.get_client().id;
                if (order_date){
                    sale_order.validity_date = order_date;
                    }
                sale_order.from_pos = true;
                var result = await this.rpc({
                    model: 'sale.order',
                    method: 'create_so_from_pos',
                    args: [[],[sale_order]],
                });
                this.cancel(); // close popup
                if (result) {
                   this.env.pos.get_order().remove_orderline(order_lines);
//                    for (let i = order_lines.length-1; -1<i < order_lines.length; i--) {
//                        this.env.pos.get_order().remove_orderline(order_lines[i]);
//                    }
//                    for (var l in order_lines){
//                        this.env.pos.get_order().remove_orderline(order_lines[l]);
//                    }
                    this.env.pos.get_order().set_client(null);
                    await this.showPopup('PosSoRef', {
                        title: this.env._t('SO Created'),
                        body: this.env._t('Sale Order Ref : ')+ result,
                    });
                }
            }

        }

        dateValidate() {
            var v = this.state.dateValue;
            if (v.match(/^\d{4}$/) !== null) {
                    this.state.dateValue = v + '/';
            }
            else if (v.match(/^\d{4}\/\d{2}$/) !== null) {
                this.state.dateValue = v + '/';
            }
        }
    }

    SOCreatePopup.template = 'SOCreatePopup';
    SOCreatePopup.defaultProps = {
        confirmText: 'Ok',
        cancelText: 'Cancel',
        array: [],
        title: 'Create Sale Order',
        body: '',
        startingValue: moment().format('YYYY/MM/DD'),
        list: [],
    };
    Registries.Component.add(SOCreatePopup);

    return SOCreatePopup;
});
