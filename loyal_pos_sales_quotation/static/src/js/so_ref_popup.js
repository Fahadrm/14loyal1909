odoo.define('loyal_pos_sales_quotation.SORefPopup', function(require) {
    'use strict';

    const { useState, useRef } = owl.hooks;
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
//    const { _lt } = require('@web/core/l10n/translation');

    // formerly SORefPopupWidget
    class PosSoRef extends AbstractAwaitablePopup {
        constructor() {
            super(...arguments);
        }
        so_created() {
            this.cancel();
        }
    }
    PosSoRef.template = 'PosSoRef';
    PosSoRef.defaultProps = {
        confirmText: 'Ok',
        cancelText: 'Cancel',
        title: 'SO Created',
        body: '',
    };

    Registries.Component.add(PosSoRef);

    return PosSoRef;

});
