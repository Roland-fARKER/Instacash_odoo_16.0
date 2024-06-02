from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Empeno(models.Model):
    _name = 'empeno.empeno'
    _description = 'Registro de Empeños'

    cliente_id = fields.Many2one('pic.cliente', string="Cliente", required=True)
    articulo = fields.Selection([
        ('electrodomestico', 'Electrodoméstico'),
        ('herramienta', 'Herramienta'),
        ('vehiculo', 'Vehículo'),
    ], string="Tipo de Artículo", required=True)
    descripcion = fields.Text(string="Descripción del Artículo", required=True)
    monto_prestamo = fields.Float(string="Monto del Préstamo", required=True)
    interes_mensual = fields.Float(string="Interés Mensual (%)", required=True)
    fecha_empeno = fields.Date(string="Fecha de Empeño", default=fields.Date.today, required=True)
    estado = fields.Selection([
        ('activo', 'Activo'),
        ('mora', 'En Mora'),
        ('perdido', 'Perdido'),
        ('liquidacion', 'Liquidación'),
    ], string="Estado", default='activo')

    @api.depends('fecha_empeno')
    def _compute_estado(self):
        for record in self:
            if record.fecha_empeno:
                delta = (fields.Date.today() - record.fecha_empeno).days
                if delta > 40:  # Ejemplo: 30 días del mes + 10 días de gracia
                    record.estado = 'perdido'
                elif delta > 30:
                    record.estado = 'mora'
                else:
                    record.estado = 'activo'

class Abono(models.Model):
    _name = 'empeno.abono'
    _description = 'Registro de Abonos'

    empeno_id = fields.Many2one('empeno.empeno', string="Empeño", required=True)
    monto_abono = fields.Float(string="Monto del Abono", required=True)
    fecha_abono = fields.Date(string="Fecha de Abono", default=fields.Date.today, required=True)
    tipo_abono = fields.Selection([
        ('cancelacion', 'Cancelación'),
        ('interes', 'Pago de Interés'),
    ], string="Tipo de Abono", required=True)

    @api.constrains('monto_abono')
    def _check_monto_abono(self):
        for record in self:
            if record.monto_abono <= 0:
                raise ValidationError("El monto del abono debe ser positivo.")
