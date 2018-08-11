# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'India-GST',
    'version' : '11.0.1',
    'summary': 'Generate B2CL,B2CS,HSN Summary,Export',
    'description': "Goods & Service-Tax.",
    'category': 'Accounting',
    'author': 'Merlin Tecsol Pvt. Ltd.',
    'website': 'http://www.merlintecsol.com',
    'license': 'AGPL-3',
    'data': [
        'data/res.country.state.csv',
        'data/fiscal_data.xml',
        'views/gst_code.xml',
        'views/port_code.xml',
        'wizard/b2b_wizard.xml',
        'wizard/b2cl_wizard.xml',
        'wizard/b2cs_wizard.xml',
        'wizard/hsn_wizard.xml',
        'wizard/export_wizard.xml',
        'report/b2b.xml',
        'report/b2cl.xml',
        'report/b2cs.xml',
        'report/hsn.xml',
        'report/export.xml',
        'report/gst_invoice_pdf.xml',
        'report/gst_sales_invoice_pdf.xml',
    ],
    'depends': ['base','report_xlsx','account_invoicing','sale_management'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/banner.png'],
}