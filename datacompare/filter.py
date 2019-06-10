from PyQt5 import QtCore

class BaseFilter(object):
    def __init__(self):
        self.dvs_id = QtCore.Qt.Unchecked
        self.dgr_id = QtCore.Qt.Unchecked
        self.unt_id = QtCore.Qt.Unchecked
        self.cls_id = QtCore.Qt.Unchecked
        self.yms_year = QtCore.Qt.Unchecked
        self.yms_sms = QtCore.Qt.Unchecked
        self.cls_id = QtCore.Qt.Unchecked
        self.cls_name_abr = QtCore.Qt.Unchecked
        self.std_id = QtCore.Qt.Unchecked
        self.std_name = QtCore.Qt.Unchecked
        self.std_idno = QtCore.Qt.Unchecked
        self.src_status = QtCore.Qt.Unchecked
        self.kind_id = QtCore.Qt.Unchecked
        self.kind_name = QtCore.Qt.Unchecked
        self.std_key = QtCore.Qt.Unchecked
        self.src_flag = QtCore.Qt.Unchecked
        self.m1 = QtCore.Qt.Unchecked
        self.m2 = QtCore.Qt.Unchecked
        self.m3 = QtCore.Qt.Unchecked
        self.s1 = QtCore.Qt.Unchecked
        self.s2 = QtCore.Qt.Unchecked
        self.s3 = QtCore.Qt.Unchecked
        self.status1 = QtCore.Qt.Unchecked
        self.status2 = QtCore.Qt.Unchecked
        self.pass_yn = QtCore.Qt.Unchecked
        self.src_kind = QtCore.Qt.Unchecked
        self.s4 = QtCore.Qt.Unchecked
        self.std_sex = QtCore.Qt.Unchecked
        self.std_mobile = QtCore.Qt.Unchecked
        self.std_tel = QtCore.Qt.Unchecked

    def set_dvs_id(self, state):
        if state == QtCore.Qt.Checked:
            self.dvs_id = QtCore.Qt.Checked
        else:
            self.dvs_id = QtCore.Qt.Unchecked
            
    def set_dgr_id(self, state):
        if state == QtCore.Qt.Checked:
            self.dgr_id = QtCore.Qt.Checked
        else:
            self.dgr_id = QtCore.Qt.Unchecked
            
    def set_unt_id(self, state):
        if state == QtCore.Qt.Checked:
            self.unt_id = QtCore.Qt.Checked
        else:
            self.unt_id = QtCore.Qt.Unchecked

    def set_cls_id(self, state):
        if state == QtCore.Qt.Checked:
            self.cls_id = QtCore.Qt.Checked
        else:
            self.cls_id = QtCore.Qt.Unchecked
            
    def set_yms_year(self, state):
        if state == QtCore.Qt.Checked:
            self.yms_year = QtCore.Qt.Checked
        else:
            self.yms_year = QtCore.Qt.Unchecked

    def set_yms_sms(self, state):
        if state == QtCore.Qt.Checked:
            self.yms_sms = QtCore.Qt.Checked
        else:
            self.yms_sms = QtCore.Qt.Unchecked
            
    def set_cls_name_abr(self, state):
        if state == QtCore.Qt.Checked:
            self.cls_name_abr = QtCore.Qt.Checked
        else:
            self.cls_name_abr = QtCore.Qt.Unchecked

    def set_std_id(self, state):
        if state == QtCore.Qt.Checked:
            self.std_id = QtCore.Qt.Checked
        else:
            self.std_id = QtCore.Qt.Unchecked
   
    def set_src_status(self, state):
        if state == QtCore.Qt.Checked:
            self.src_status = QtCore.Qt.Checked
        else:
            self.src_status = QtCore.Qt.Unchecked

    def set_kind_id(self, state):
        if state == QtCore.Qt.Checked:
            self.kind_id = QtCore.Qt.Checked
        else:
            self.kind_id = QtCore.Qt.Unchecked

    def set_kind_name(self, state):
        if state == QtCore.Qt.Checked:
            self.kind_name = QtCore.Qt.Checked
        else:
            self.kind_name = QtCore.Qt.Unchecked

    def set_std_key(self, state):
        if state == QtCore.Qt.Checked:
            self.std_key = QtCore.Qt.Checked
        else:
            self.std_key = QtCore.Qt.Unchecked

    def set_src_flag(self, state):
        if state == QtCore.Qt.Checked:
            self.src_flag = QtCore.Qt.Checked
        else:
            self.src_flag = QtCore.Qt.Unchecked

    def set_m1(self, state):
        if state == QtCore.Qt.Checked:
            self.m1 = QtCore.Qt.Checked
        else:
            self.m1 = QtCore.Qt.Unchecked
            
    def set_m2(self, state):
        if state == QtCore.Qt.Checked:
            self.m2 = QtCore.Qt.Checked
        else:
            self.m2 = QtCore.Qt.Unchecked
            
    def set_m3(self, state):
        if state == QtCore.Qt.Checked:
            self.m3 = QtCore.Qt.Checked
        else:
            self.m3 = QtCore.Qt.Unchecked
            
    def set_s1(self, state):
        if state == QtCore.Qt.Checked:
            self.s1 = QtCore.Qt.Checked
        else:
            self.s1 = QtCore.Qt.Unchecked
            
    def set_s2(self, state):
        if state == QtCore.Qt.Checked:
            self.s2 = QtCore.Qt.Checked
        else:
            self.s2 = QtCore.Qt.Unchecked
            
    def set_s3(self, state):
        if state == QtCore.Qt.Checked:
            self.s3 = QtCore.Qt.Checked
        else:
            self.s3 = QtCore.Qt.Unchecked
            
    def set_s4(self, state):
        if state == QtCore.Qt.Checked:
            self.s4 = QtCore.Qt.Checked
        else:
            self.s4 = QtCore.Qt.Unchecked

    def set_status1(self, state):
        if state == QtCore.Qt.Checked:
            self.status1 = QtCore.Qt.Checked
        else:
            self.status1 = QtCore.Qt.Unchecked
            
    def set_status2(self, state):
        if state == QtCore.Qt.Checked:
            self.status2 = QtCore.Qt.Checked
        else:
            self.status2 = QtCore.Qt.Unchecked
            
    def set_std_idno(self, state):
        if state == QtCore.Qt.Checked:
            self.std_idno = QtCore.Qt.Checked
        else:
            self.std_idno = QtCore.Qt.Unchecked
            
    def set_std_name(self, state):
        if state == QtCore.Qt.Checked:
            self.std_name = QtCore.Qt.Checked
        else:
            self.std_name = QtCore.Qt.Unchecked

    def set_pass_yn(self, state):
        if state == QtCore.Qt.Checked:
            self.pass_yn = QtCore.Qt.Checked
        else:
            self.pass_yn = QtCore.Qt.Unchecked

    def set_src_kind(self, state):
        if state == QtCore.Qt.Checked:
            self.src_kind = QtCore.Qt.Checked
        else:
            self.src_kind = QtCore.Qt.Unchecked

    def set_std_sex(self, state):
        if state == QtCore.Qt.Checked:
            self.std_sex = QtCore.Qt.Checked
        else:
            self.std_sex = QtCore.Qt.Unchecked

    def set_std_mobile(self, state):
        if state == QtCore.Qt.Checked:
            self.std_mobile = QtCore.Qt.Checked
        else:
            self.std_mobile = QtCore.Qt.Unchecked

    def set_std_tel(self, state):
        if state == QtCore.Qt.Checked:
            self.std_tel = QtCore.Qt.Checked
        else:
            self.std_tel = QtCore.Qt.Unchecked


class ResultFilter(BaseFilter):
    def __init__(self):
        super(ResultFilter, self).__init__()
        self.std_name = QtCore.Qt.Checked
        self.std_idno = QtCore.Qt.Checked
        self.std_id = QtCore.Qt.Checked
        self.std_mobile = QtCore.Qt.Checked
        self.std_tel = QtCore.Qt.Checked
        self.kind_name = QtCore.Qt.Checked

    @property
    def filter_list(self):
        filter_list = []
        for key, value in self.__dict__.items():
            if value == QtCore.Qt.Checked:
                filter_list.append(key)
        return filter_list
