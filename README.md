radarr
=========

Installs Radarr.

Requirements
------------

* CentOS
* Internet Connected

Role Variables
--------------

```bash
radarr_release_url: https://api.github.com/repos/Radarr/Radarr/releases.linux.tar.gz # API link for releases
```

Example Playbook
----------------

```plain
- hosts: radarr
  roles:
  - {name: radarr, become: yes}
```

References
----------

* [Radarr](https://github.com/Radarr/Radarr/)
