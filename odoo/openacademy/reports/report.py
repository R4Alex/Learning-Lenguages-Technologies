# -*- coding: utf-8 -*-


from odoo import api, models


class ReportSession(models.AbstractModel):
    _name = "report.openacademy.report_session"


    @api.multi
    def render_html(self, data=None):
        report_obj = self.env["report"]
        report = report_obj._get_report_from_name("openacademy.report_session")
        # Argumentos del reporte, aqui se definen variables como docs

        docargs = {
            "doc_ids": self._ids,
            "doc_model": report.model,
            "docs": self,
        }

        return report_obj.render("openacademy.report_session", docargs)
