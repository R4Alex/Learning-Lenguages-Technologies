# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from psycopg2 import IntegrityError
from datetime import timedelta

class Course(models.Model):
    _name = 'openacademy.course'
    _description = '''  '''


    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one(
        'res.users', 
        string="Responsible", 
        index=True, 
        ondelete='set null',
        default=lambda self, *a: self.env.uid)
    session_ids = fields.One2many('openacademy.session', 'course_id')
    
    _sql_constraints = [
        ('name_description_check',
         'CHECK( name != description )',
         "The title of the curse should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
    
    
    def copy(self, default=None):
        if default is None:
            default = {}
        
        copied_count = self.search_count([
            ('name', 'ilike', 'Copy of %s%%' % (self.name))])

        if not copied_count:
            new_name = "Copy of %s" % (self.name)
        else:
            new_name = "Copy of %s (%s)" % (self.name, copied_count)
        
        default['name'] = new_name

        return super(Course, self).copy(default)
        
        #try:
        #    return super(Course, self).copy(default)
        #except IntegrityError:
        #    import pdb; pdb.set_trace()

class Session(models.Model):
    _name = 'openacademy.session'
    _description = '''  '''
    
    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string='instructor', domain=['|', ('instructor_id', '=', True), ('category_id.name', 'ilike', 'Teacher')])

    course_id = fields.Many2one(
        'openacademy.course', 
        ondelete="cascade", 
        string="Course", 
        required=True)

    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seats = fields.Float(compute="_taken_seats", store=True);
    active = fields.Boolean(default=True)
    end_date = fields.Date(store=True, compute="_get_end_date", inverse="_set_end_date")
    attendees_count = fields.Integer(compute="_get_attendees_count", store=True)

    # to make a kanbam view 
    color = fields.Float()
    
    # Gantt view
    hours = fields.Float(string="Duration in hours", compute='_get_hours', inverse='_set_hours')
    
    
    
    @api.depends('duration')
    def _get_hours(self):
        for record in self:
            record.hours = record.duration * 24
    
    
    @api.depends('duration')
    def _set_hours(self):
        for record in self:
            record.duration = record.hours / 24

    
    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for record in self:
            record.attendees_count = len(record.attendee_ids)




    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for record in self.filtered('start_date'):
            #start_date = fields.Datetime.from_string(record.start_date) on odoo10 start_date is a unicode on 12 is a date so
            record.end_date = record.start_date + timedelta(days=record.duration, seconds=-1)


    @api.depends('start_date', 'duration')
    def _set_end_date(self):
        for record in self.filtered('start_date'):
            record.duration = (record.end_date - record.start_date).days + 1


    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        #for record in self:
        #for record in self.filtered('seats'):
        for record in self.filtered(lambda r: r.seats):
            if not record.seats:
                record.taken_seats = 0
            else:
                record.taken_seats = 100.0 * len(record.attendee_ids) / record.seats


    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        #if self.seats < 0:
        if self.filtered(lambda r: r.seats < 0):
            self.active = False
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of availible seats may not be negative",
                }
            }

        if self.seats < len(self.attendee_ids):
            self.active = True
            return {
                'warning': {
                    'title': "To many attendees",
                    'message': "Increse seats or remove excess attendees",
                }
            } 

        self.active = True


    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for record in self.filtered('instructor_id'):
            if record.instructor_id in record.attendee_ids:
                raise exceptions.ValidationError(
                        "A session's instructor can't be an attendee")

    