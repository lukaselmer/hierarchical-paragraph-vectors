import json
import os
import subprocess

import requests


def api_url(path):
    host = os.environ['API_HOST']
    prefix = 's'
    if host == '127.0.0.1':
        prefix = ''
        host = '127.0.0.1:3000'

    return 'http{0}://{1}{2}'.format(prefix, host, path)


def end_all():
    url = api_url('/runs/end_all')
    params = dict(api_key=os.environ['API_KEY'])
    resp = requests.get(url=url, params=params)
    print(resp)


def schedule_runs(general_params, narrow_params):
    if os.environ.get('END_ALL') == 'end_all':
        end_all()

    url = api_url('/runs/schedule_runs.json')
    params = dict(api_key=os.environ['API_KEY'])
    data = json.dumps(dict(general_params=general_params, narrow_params=narrow_params))
    headers = {'Content-Type': 'application/json'}

    resp = requests.post(url=url, params=params, data=data, headers=headers)
    print(resp)


def get_random_pending_run():
    url = api_url('/runs/start_random_pending_run')

    host_name = _get_host_name()
    params = dict(api_key=os.environ['API_KEY'], host_name=host_name)

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    start = data['result'] == 'start'

    if not start:
        return None

    return dict(id=data['id'], algo_params=data['algo_params'])


def report_results(run_id, output):
    url = api_url('/runs/{0}/report_results'.format(run_id))
    params = {'api_key': os.environ['API_KEY'], 'run[output]': output}

    resp = requests.put(url=url, data=params)
    print(resp)


def _get_host_name():
    if os.path.exists('.host_name'):
        with open('.host_name', 'r') as host_name_file:
            return host_name_file.read().strip()

    return subprocess.check_output('hostname').strip()
