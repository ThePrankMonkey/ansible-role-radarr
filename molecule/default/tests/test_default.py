import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_radarr_service(host):
    host.service('radarr').is_running


def test_radarr_page(host):
    cmd = host.run("curl 127.0.0.1:7878")
    cmd.rc == 0
    "Radarr" in cmd.stdout
