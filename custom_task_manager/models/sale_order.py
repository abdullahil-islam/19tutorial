from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    task_id = fields.Many2one(
        'task.task',
        string='Task', readonly=True,
        copy=False,
    )
