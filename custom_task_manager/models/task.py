from odoo import models, fields, api


class TaskCategory(models.Model):
    _name = 'task.category'
    _description = 'Task Category'

    name = fields.Char(string='Name', required=True)
    task_count = fields.Integer(string='Task Count')


class Task(models.Model):
    _name = 'task.task'
    _description = 'Custom Task'

    name = fields.Char(string='Name', required=True)
    user_id = fields.Many2one(comodel_name='res.users', string='User', default=lambda self: self.env.user)
    deadline = fields.Date(string='Deadline', default=fields.Datetime.now())
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('new', 'New Task'),
        ('in_progress', 'In Progress'),
        ('qa', 'QA'),
        ('failed', 'QA Failed'),
        ('done', 'Done')
    ], default='new', string='Task Status') # tracking=True, copy=False, index=True
    is_overdue = fields.Boolean(string='Is Overdue', compute='_compute_is_overdue', store=True)
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner')

    @api.depends('deadline')
    def _compute_is_overdue(self):
        for task in self:
            task.is_overdue = task.deadline and task.deadline < fields.Date.today() and task.state != 'done'
        # self.is_overdue = self.deadline and self.deadline < fields.Date.today() and self.state != 'done'

    def sent_to_in_progress(self):
        self.state = 'in_progress'

    def sent_to_in_qa(self):
        self.state = 'qa'

    def sent_to_done(self):
        try:
            self.state = 'done'
            product = self.env['product.template'].browse(45)
            sale_order = self.env['sale.order'].create({
                'partner_id': self.partner_id.id,
                'task_id': self.id,
                'order_line': [
                    fields.Command.create({
                        'product_template_id': product.id,
                        'name': product.name,
                        'product_uom_qty': 1.0,
                        'price_unit': 150,
                    }),
                ],
            })
            self.state = 'done'
        except Exception as e:
            raise e

