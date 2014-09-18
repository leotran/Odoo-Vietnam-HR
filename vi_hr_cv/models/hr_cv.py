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

from openerp.osv import fields, osv

class hr_curriculum_vitae(osv.Model):
    _inherit = 'hr.employee'
    
    def _get_year(self, cr, uid, ids, name, arg, context=None):
        values = self.read(cr, uid, ids, ['date_of_graduation'], context)
        res = dict(map(lambda x: (x['id'], x['date_of_graduation'] and x['date_of_graduation'][0:4] or False), values))
    
    _columns = {
        'vi_reference': fields.char('Reference', size=128),
        'vi_address_origin_id': fields.many2one('res.partner', 'Origin Address'),
        'vi_date_allocate_cmnd': fields.date('Date of Allocate'),
        'vi_place_allocate_cmnd': fields.many2one("res.country.state", 'Place of Allocate'),
        'vi_date_allocate_passport': fields.date('Date of Allocate'),
        'vi_place_allocate_passport': fields.many2one("res.country.state", 'Place of Allocate'),
        'vi_date_limit_passport': fields.date('Date of Limit'),
        'vi_family_type': fields.many2one('vi.hr.thanhphan.giadinh','Family Type'),
        'vi_employee_type': fields.many2one('vi.hr.thanhphan.banthan','Employee Type'),
        'vi_nationality': fields.many2one('vi.hr.dantoc','Nationality'),
        'vi_religiousness': fields.many2one('vi.hr.tongiao','Religiousness'),
        'vi_training_level': fields.many2one('vi.hr.trinhdo.daotao','Training Level'),
        'vi_training_place': fields.many2one('vi.hr.noi.daotao','Place of Training'),
        'vi_training_subject': fields.many2one('vi.hr.khoa.daotao','Subject of Training'),
        'vi_training_speciality': fields.many2one('vi.hr.chuyennganh.daotao','Speciality of Training'),
        'vi_date_of_graduation': fields.date('Date of Graduation'),
        'vi_year_of_graduation': fields.function(_get_year, type='char', readonly=True, string='Year'),
        'vi_training_ranking': fields.many2one('vi.hr.xeploai.daotao','Ranking of Training'),
        'vi_occupation': fields.many2one('vi.hr.nghenghiep','Occupation'),
        'vi_personal_email': fields.char('Personal Email', size=32),
        'vi_other_email': fields.char('Other Email', size=32),
        'vi_yahoo': fields.char('Yahoo ID', size=32),
        'vi_skype': fields.char('Skype ID', size=32),
        'vi_msn': fields.char('MSN ID', size=32),
        'vi_gtalk': fields.char('Gtalk ID', size=32),
        'vi_household': fields.many2one('res.partner','Household'),
        'vi_contact_emergency': fields.many2one('res.partner','Contact Emergency'),
        'vi_relation': fields.many2one('vi.hr.quanhegiadinh','Relation'),
        'vi_party_member_ok': fields.boolean('Is Party Member'),
        'vi_date_party_admission': fields.date("Date of Party admission"),
        'vi_duty_party': fields.many2one('vi.hr.chucvu','Duty'),
        'vi_place_party_admission': fields.char('Place of party admission', size=128),
        'vi_union_member_ok': fields.boolean('Is Union Member'),
        'vi_date_union_admission': fields.date("Date of Union Admission"),
        'vi_duty_uinon': fields.many2one('vi.hr.chucvu','Duty'),
        'vi_place_union_admission': fields.char('Place of union admission', size=128),
        'vi_military_ok': fields.boolean('Is Military'),
        'vi_date_military_admission': fields.date('Date of Military admission'),
        'vi_military_organization': fields.char('Military Organization', size=128),
        'vi_duty_military': fields.many2one('vi.hr.chucvu','Duty'),
        'vi_military_level': fields.many2one('vi.hr.capbac.quannhan','Military Level'),
        'vi_army': fields.many2one('vi.hr.binhchung','Army'),
        'vi_date_demobilisation': fields.date('Date of Demobilisation'),
        'vi_reason': fields.text('Reason'),
        'vi_wounded_soldier_ok': fields.boolean('Is wounded soldier'),
        'vi_date_revolution_admission': fields.date('Date of Revolution admission'),
        'vi_wounded_soldier_rate': fields.many2one('vi.hr.hangthuongbinh','Wounded_soldier rate'),
        'vi_declining_labor_rate': fields.float('Declining labor rate'),
        'vi_regimen_ok': fields.boolean('Regimen'),
        'vi_blood_group': fields.selection([('o','O'),('a','A'),('b','B'),('ab','AB')],'Blood group'),
        'vi_height': fields.float('Height'),
        'vi_weight': fields.float('Weight'),
        'vi_health_status': fields.char('Health status', size=64),
        'vi_warning': fields.char('Warning', size=64),
        'vi_disease': fields.char('Disease', size=64),
        'vi_like': fields.text('Like'),
        'vi_strength': fields.text('Strength'),
        'vi_weakness': fields.text('Weakness'),
        'vi_target': fields.text('Target'),
    }