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

class hr_dantoc(osv.Model):
    _name = 'vi.hr.dantoc'
    _description = 'HR Dan Toc'

    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'notes': fields.char('Notes', size=128),
    }

class hr_thanhphan_giadinh(osv.Model):
    _name ='vi.hr.thanhphan.giadinh'
    _description = 'HR Thanh Phan Gia Dinh'

    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'notes': fields.char('Notes', size=128),
    }

class hr_thanhphan_banthan(osv.Model):
    _name ='vi.hr.thanhphan.banthan'
    _description = 'HR Thanh Phan Ban Than'

    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'notes': fields.char('Notes', size=128),
    }

class hr_tongiao(osv.Model):
    _name ='vi.hr.tongiao'
    _description = 'HR Ton Giao'

    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'notes': fields.char('Notes', size=128),
    }

class hr_binhchung(osv.Model):
    _name ='vi.hr.binhchung'
    _description = 'HR Binh Chung'

    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'notes': fields.char('Notes', size=128),
    }

class hr_capbac_quannhan(osv.Model):
    _name ='vi.hr.capbac.quannhan'
    _description = 'HR Cap Bac Quan Nhan'

    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'notes': fields.char('Notes', size=128),
    }

class hr_chucvu(osv.Model):
    _name ='vi.hr.chucvu'
    _description = 'HR Chuc Vu'

    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'type': fields.selection([('dang', 'Dang'), ('doan', 'Doan'), ('quannhan', 'Quan nhan')], 'Type'),
        'notes': fields.text('Notes'),
    }

class hr_hangthuongbinh(osv.Model):
    _name = 'vi.hr.hangthuongbinh'
    _description = 'HR Hang Thuong Binh'

    _columns = {
        'name': fields.char('Name', size=32, required=True),
        'notes': fields.char('Notes', size=128),
    }

class hr_quanhegiadinh(osv.Model):
    _name = 'vi.hr.quanhegiadinh'
    _description = 'HR Quan He Gia Dinh'

    _columns = {
        'name': fields.char('Name', size=32, required=True),
        'type': fields.selection([('parent','Parent'),('grandparents','Grandparents'),('spouses','Spouses'),('brotherandsister','Sister/Brother'),('childrent','Children'),('relatives','Relatives'),('other','Other')], 'Type', required=True),
        'notes': fields.text('Notes'),
    }

class hr_trinhdo_daotao(osv.Model):
    _name = 'vi.hr.trinhdo.daotao'
    _description = 'HR Trinh Do Dao Tao'

    _columns = {
        'name': fields.char('Name', size=32, required=True),
        'pass': fields.boolean('Pass'),
        'notes': fields.text('Notes'),
    }

class hr_noi_daotao(osv.Model):
    _name = 'vi.hr.noi.daotao'
    _description = 'HR Noi Dao Tao'

    _columns = {
        'name': fields.char('Name', size=128, required=True),
        'code': fields.char('Code', size=32),
        'notes': fields.text('Notes'),
    }

class hr_khoa_daotao(osv.Model):
    _name = 'vi.hr.khoa.daotao'
    _description = 'HR Khoa Dao Tao'

    _columns = {
        'name': fields.char('Name', size=128, required=True),
        'notes': fields.char('Notes', size=128),
    }

class hr_chuyennganh_daotao(osv.Model):
    _name = 'vi.hr.chuyennganh.daotao'
    _description = 'HR Chuyen Nganh Dao Tao'

    _columns = {
        'name': fields.char('Name', size=128, required=True),
        'notes': fields.char('Notes', size=128),
    }

class hr_xeploai_daotao(osv.Model):
    _name = 'vi.hr.xeploai.daotao'
    _description = 'HR Xep Loai Dao Tao'

    _columns = {
        'name': fields.char('Name', size=32, required=True),
        'notes': fields.char('Notes', size=128),
    }

class hr_nghenghiep(osv.Model):
    _name = 'vi.hr.nghenghiep'
    _description = 'HR Nghe Nghiep'

    _columns = {
        'name': fields.char('Name', size=128, required=True),
        'notes': fields.char('Notes', size=128),
    }