# -*- coding: utf-8 -*-
from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError
class pic(models.Model):
    _name = 'pic.cliente'
    _description = 'cliente'

    nombre = fields.Char(string="Nombre", help="Ejemplo Juan Perez")
    phone = fields.Char(string="Teléfono", help="ejemplo 23238989")
    email = fields.Char(string="Correo", help="ejemplo cliente@correo.com")
    direccion = fields.Char(string="Dirección")
    identification = fields.Char(string="Identificación", help=" Ejemplo XXX-XXXXXX-XXXXX" )
    
    _sql_constraints = [
        ('identificacion_unique', 'unique(identificacion)', 'La identificación debe ser única.')
    ]
    @api.constrains('phone')
    def _check_phone(self):
        phone_pattern = re.compile(r'^\+?1?\d{8,15}$')
        for record in self:
            if record.phone and not phone_pattern.match(record.phone):
                raise ValidationError("El número de teléfono no es válido. Debe tener entre 8 y 15 dígitos y puede comenzar con +.")

    @api.constrains('email')
    def _check_email(self):
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        for record in self:
            if record.email and not email_pattern.match(record.email):
                raise ValidationError("La direción de correo no es valida.")
    
    @api.constrains('identification')
    def _check_identification_format(self):
        for record in self:
            if record.identification:
                # Comprobamos que el campo tenga el formato correcto
                if not re.match(r'^\d{3}-\d{6}-\d{4}[A-Z]$', record.identification):
                    raise ValidationError("La identificación debe tener un formato: XXX-XXXXXX-XXXXX.")