# # -*- coding: utf-8 -*-
from odoo import fields, models, _
from collections import defaultdict



class MailActivity(models.Model):

    _inherit = 'mail.activity'


    priority = fields.Selection([
        ('low','Low'),
        ('medium', 'Medium'),
        ('high','High')
    ])
    is_action = fields.Boolean(string="Is Done")
    status = fields.Selection([('new', 'New'), ('progress', 'Progress'), ('transfer', 'Transferred'), ('done', 'Done')],
                                readonly=True, default='new', tracking=3)

    def action_progress(self):
        return self.write({'status': 'progress'})

    def action_transfer(self):
        return self.write({'status': 'transfer'})

    def action_done(self):
        """ Wrapper without feedback because web button add context as
        parameter, therefore setting context to feedback """
        # messages, next_activities = self._action_done()
        # action_obj = self.env['ir.model.data']
        # action = self.env['ir.actions.act_window']._for_xml_id('schedule_activities.action_window_mail_activities')
        # if self.env.context.get('mail_activity_quick_update') == True:
        #     return action
        # else:
        #     return messages.ids and messages.ids[0] or False
        return self.write({'status': 'done'})


class Meeting(models.Model):

    _name = 'calendar.event'
    _inherit = ['calendar.event', 'mail.activity.mixin', 'utm.mixin']