# Copyright 2014 Michael Rice <michael@michaelrice.org>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import datetime as dt

from vBurgundy.database import (
    Column,
    db,
    Model,
)


class Vcenter(Model):

    __tablename__ = 'vcenter'
    vcenter_name = Column(db.String(length=120), unique=True, nullable=False)
    vcenter_ip = Column(db.String(15), nullable=True)
    vcenter_user = Column(db.String(120), unique=False, nullable=True)
    vcenter_user_pwd = Column(db.String(240), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, vcname, vcip=None, vcuser=None, vcpwd=None, **kwargs):
        db.Model(vcenter_name=vcname, vcenter_ip=vcip, vcenter_user=vcuser,
                 vcenter_user_pwd=vcpwd, **kwargs)
