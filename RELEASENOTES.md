# Unomi Release notes

## actual version: v1.5

### v1.5 (2019-08-06)
* [IMPROVEMENT] more tags added for datadog-agents
    * and add a set_dd_tags.sh for using `/metadata_from_HOST` file for it
* [IMPROVEMENT] unomi logs to Datadog
    * specific jmx conf for datadog-agent are now enabled
        * get log from `/opt/unomi/unomi-1.3.3-jahia/data/log/karaf.log` and `/opt/unomi/unomi-1.3.3-jahia/data/security/audit.log`
        * connect to _JMX_ on `service:jmx:rmi:///jndi/rmi://localhost:1099/karaf-root`
        * autofetch beans from domains `org.apache.karaf`, `com.sun.management` and `java.lang`
* [IMPROVEMENT] set a random password to access unomi
    * by setting a new envvar `UNOMI_ROOT_PASSWORD` on unomi mode (in `unomi.yml`)
    * get this variable and use it in DX's file `org.jahia.modules.marketingfactory.settings-mf.cfg` (in `unomi_update_dx.yml`)


### v1.4 (2019-07-24)
* [IMPROVEMENT] they were no Datadog tags for `envname` and `role`
    * now a tag `envname:${env.envName}` is added to Datadog agent
    * now a tag `role:(unomi|elasticsearch)` is added to Datadog agent

### v1.3 (2019-07-08)
* [NEW] Add _Unomi_ license key as a setting in `unomi_update_dx`
    * this setting is mandatory
    * have to be base64

### v1.2 (2019-06-25)
* [BUG] in `unomi_package_dx.yml`, action `updateDX` was still using old settings `unomidns`
    * add a new action `getUnomiDNS` which set a new global `unomidns`
    * now `updateDX` is using this new global


### v1.1 (2019-06-24)
* revamp the Unomi targetting:
    * rename setting `unommidns` to `unomienv`
    * `unomienv` is now an envlist
    * set `envLink` in Unomi's `cp` node group as a _NodeGroupData_
        * created if not present
        * do nothing if the _DX_ env is already in
        * add the _DX_ env if not in (values are commo separated)
