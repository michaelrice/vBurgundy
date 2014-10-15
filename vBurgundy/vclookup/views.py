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

from flask import Blueprint, render_template
from flask.ext.login import login_required

blueprint = Blueprint("vclookup", __name__, url_prefix='/vclookup',
                      static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    return render_template("vclookup/vcenter.html")