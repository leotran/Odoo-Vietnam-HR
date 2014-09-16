# -*- coding: utf-8 -*-
##############################################################################
#
#    @package vi_hr_cv HR Employee Curriculum Vitae for Odoo 7-saas5
#    @copyright Copyright (C) 2014 Leo Tran (leotran.hpvn@gmail.com). All rights reserved.#
#    @license http://www.gnu.org/licenses GNU Affero General Public License version 3 or later; see LICENSE.txt
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Vietnam HR Employee CV',
    'version': '1.0',
    'category': 'Human Resources',
    'sequence': 22,
    'summary': 'Curriculum Vitae, Politics Information, Medical Information',
    'description': """
Manage employee curriculum vitae:
---------------------------------
* Contact Information
* Family Information
* Politics Information
* Medical Information
* Military Information
    """,
    'author': 'Leo Tran',
    'website': 'http://www.openerpdev.com',
    'depends': ['hr'],
    'data': [
        'views/setting_view.xml',
        'views/hr_cv_view.xml',
        'data/vi.hr.binhchung.csv',
        'data/vi.hr.capbac.quannhan.csv',
        'data/vi.hr.chucvu.csv',
        'data/vi.hr.chuyennganh.daotao.csv',
        'data/vi.hr.dantoc.csv',
        'data/vi.hr.hangthuongbinh.csv',
        'data/vi.hr.khoa.daotao.csv',
        'data/vi.hr.nghenghiep.csv',
        'data/vi.hr.noi.daotao.csv',
        'data/vi.hr.quanhegiadinh.csv',
        'data/vi.hr.thanhphan.banthan.csv',
        'data/vi.hr.thanhphan.giadinh.csv',
        'data/vi.hr.tongiao.csv',
        'data/vi.hr.trinhdo.daotao.csv',
        'data/vi.hr.xeploai.daotao.csv',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}