import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_service_is_running_and_enabled(host):
    kibana = host.service("kibana")

    assert kibana.is_running
    assert kibana.is_enabled


def test_package_is_installed(host):
    kibana = host.package('kibana')

    assert kibana.is_installed
    assert kibana.version.startswith('7')
