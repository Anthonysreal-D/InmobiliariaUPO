from odoo import models, fields, api


class persona(models.Model):
    _name = 'inmobiliaria_upo.persona'
    _inherit = 'hr.employee'

    category_ids = fields.Many2many(relation=False)
    name = fields.Char(string="DNI", related='resource_id.name', store=False, readonly=False, tracking=True, size=10)
    phone = fields.Char(related='address_home_id.phone', related_sudo=False, readonly=False, string="Teléfono", groups="hr.group_hr_user")
    work_email = fields.Char(string="Correo Electrónico", compute="_compute_work_contact_details", store=True, inverse='_inverse_work_contact_details')
    
    sNombre = fields.Char(string="Nombre", required=True)
    sApellidoUno = fields.Char(string="Primer apellido", required=True, size=255)
    sApellidoDos = fields.Char(string="Segundo Apellido", size=255)
    iEdad = fields.Integer(string="Edad", size=255)


