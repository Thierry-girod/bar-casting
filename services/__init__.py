import sys

import requests

def get_param(request, param_name, mandatory=False):
    param = request.args.get(param_name)
    if mandatory and not param:
        raise BadRequest("{} parameter is mandatory".format(param_name))
    return param


def get_form_param(request, param_name, mandatory=False):
    param = request.form.get(param_name)
    if mandatory and not param:
        raise BadRequest("{} parameter is mandatory".format(param_name))
    return param


def get_json_value(request, value_name, mandatory=False, default=None):
    data = request.get_json(silent=True, cache=False)
    if not data:
        if mandatory:
            raise BadRequest("Invalid JSON request")
        return None
    if mandatory and data.get(value_name) is None:
        raise BadRequest("{} parameter is mandatory".format(value_name))
    return data.get(value_name, default)
