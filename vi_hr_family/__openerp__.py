# -*- coding: utf-8 -*-
##############################################################################
#    
#    @package vi_hr_family HR Family for OpenERP 7.0
#    @copyright Copyright (C) 2013 Leo Tran (leotran.hpvn@gmail.com). All rights reserved.#
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
    'name': 'Vietnam HR Employee Family',
    'version': '1.0',
    'category': 'Human Resources',
    'sequence': 23,
    'summary': 'Employee Family Relationship',
    'description': """
Manage employee family information:
-----------------------------------
* Contact Information
* Relationship
* Dependency
    """,
    'author': 'Leo Tran',
    'website': 'http://openerpdev.com',
    'depends': ['vi_hr_cv'],
    'data': [
        'hr_family_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}