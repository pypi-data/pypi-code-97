# © 2017 Sergio Teruel <sergio.teruel@tecnativa.com>
# © 2021 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.addons import decimal_precision as dp


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    margin = fields.Monetary(
        string='Margin',
        compute='_compute_margin',
        digits=dp.get_precision('Product Price'),
        store=True,
        currency_field='currency_id',
    )

    margin_signed = fields.Monetary(
        string='Margin Signed',
        compute='_compute_margin',
        digits=dp.get_precision('Product Price'),
        store=True,
        currency_field='currency_id',
    )

    margin_percent = fields.Float(
        string='(%) Margin',
        digits=dp.get_precision('Product Price'),
        compute='_compute_margin',
        store=True,
    )

    @api.multi
    @api.depends(
        'invoice_line_ids.margin',
        'invoice_line_ids.margin_signed',
        'invoice_line_ids.price_subtotal',
    )
    def _compute_margin(self):
        for invoice in self:
            invoice_lines = invoice.invoice_line_ids
            price_subtotal = sum(invoice_lines.mapped('price_subtotal'))
            margin_signed = sum(invoice_lines.mapped('margin_signed'))
            invoice.update({
                'margin': sum(invoice_lines.mapped('margin')),
                'margin_signed': margin_signed,
                'margin_percent': price_subtotal and (
                    margin_signed / price_subtotal * 100) or 0,
            })


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    margin = fields.Float(
        compute='_compute_margin',
        digits=dp.get_precision('Product Price'),
        store=True,
        string='Margin',
    )
    margin_signed = fields.Float(
        compute='_compute_margin',
        digits=dp.get_precision('Product Price'),
        store=True,
        string='Margin Signed',
    )
    margin_percent = fields.Float(
        string='% Margin',
        compute='_compute_margin',
        store=True,
        readonly=True,
    )
    purchase_price = fields.Float(
        digits=dp.get_precision('Product Price'),
        string='Cost',
    )

    @api.multi
    @api.depends('purchase_price', 'price_subtotal')
    def _compute_margin(self):
        applicable = self.filtered(
            lambda x: x.invoice_id and x.invoice_id.type[:2] != 'in'
        )
        for line in applicable:
            tmp_margin = line.price_subtotal - (
                line.purchase_price * line.quantity)
            sign = line.invoice_id.type in [
                'in_refund', 'out_refund'] and -1 or 1
            line.update({
                'margin': tmp_margin,
                'margin_signed': tmp_margin * sign,
                'margin_percent': (tmp_margin / line.price_subtotal * 100.0 if
                                   line.price_subtotal else 0.0),
            })

    @api.onchange('product_id', 'uom_id')
    def _onchange_product_id_account_invoice_margin(self):
        if self.invoice_id.type in ['out_invoice', 'out_refund']:
            purchase_price = self.product_id.standard_price
            if self.uom_id != self.product_id.uom_id:
                purchase_price = self.product_id.uom_id._compute_price(
                    purchase_price, self.uom_id)
            self.purchase_price = purchase_price
