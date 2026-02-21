# from odoo import http


# class CustomTaskManager(http.Controller):
#     @http.route('/custom_task_manager/custom_task_manager', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_task_manager/custom_task_manager/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_task_manager.listing', {
#             'root': '/custom_task_manager/custom_task_manager',
#             'objects': http.request.env['custom_task_manager.custom_task_manager'].search([]),
#         })

#     @http.route('/custom_task_manager/custom_task_manager/objects/<model("custom_task_manager.custom_task_manager"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_task_manager.object', {
#             'object': obj
#         })

