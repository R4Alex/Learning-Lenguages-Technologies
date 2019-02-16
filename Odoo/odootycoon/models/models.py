# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OdooTycoonGameManager(models.Model):
    _name = "odootycoon.gamemanager"

    name = fields.Char("Game Name", default="New Game")
    day = fields.Integer("Current Day", default=1)
    cash = fields.Float("Cash", default=5000)
    