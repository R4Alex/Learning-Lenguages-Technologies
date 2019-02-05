# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OdooTycoonGameManager(models.Model):
    _name = "odootycoon.gamemanager"

    name = fields.Char("Game Name")
    day = fields.Integer("Current Day")
    cash = fields.Float("Cash")
    