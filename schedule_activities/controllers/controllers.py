# -*- coding: utf-8 -*-
# from odoo import http


# class ScheduleActivities(http.Controller):
#     @http.route('/schedule_activities/schedule_activities', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/schedule_activities/schedule_activities/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('schedule_activities.listing', {
#             'root': '/schedule_activities/schedule_activities',
#             'objects': http.request.env['schedule_activities.schedule_activities'].search([]),
#         })

#     @http.route('/schedule_activities/schedule_activities/objects/<model("schedule_activities.schedule_activities"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('schedule_activities.object', {
#             'object': obj
#         })
