# Jelastic jCustomer Environments

This repository hosts all needed stuff to create a jCustomer environment on Jelastic.

## Infrasctructure overview

A jCustomer environment contains:
- At least one jCustomer node (up to seven)
- Either a single Elasticsearch node or a three/five nodes cluster

Requests on the environment domain name target jCustomer node(s) (load balanced if in cluster mode).

## Docker images

Images used by jCustomer environment nodes:

| Node type     | Docker image              |
| ------------- | ------------------------- |
| jCustomer     | jahia/jahiastic-jcustomer |
| Elasticsearch | jahiadev/elasticsearch    |

## Packages

### unomi.yml

The base JPS, called by Jahia Cloud to create a jCustomer environment.

Takes as parameters:

- name: productVersion
  - jCustomer Version
- name: UnomiMode
  - jCustomer mode
- name: ESMode
  - Number of Elasticsearch nodes
- name: mode
  - Number of jCustomer nodes
- name: ddogApikey
  - Datadog API KEY

### update.yml

This package aims at updating events only, it is used when releasing a new Jahia Cloud version so we can make sure events are up-to-date and synchronized with environment modifications.

### unomi-upgrade.yml

This *upgrade* package aims at upgrading jCustomer version by redeploying jCustomer nodes with the target jCustomer version tag, but since it takes the tag as a parameter, it is also used to do a simple redeploy of jCustomer nodes.

Parameters are:
- name: targetVersion
  caption: Target jCustomer Version, if nothing is specified, it will be a simple redeploy
- name: packageType
  caption: Package Type

### unomi_update_dx.yml

This package aims at linking a jCustomer environment with a Jahia environment.

It is applied on a Jahia environment and take the shortdomain of the jCustomer environment as a parameter.

### utils/

In **utils** folder are stored packages that are called via Jelastic API from Jahia Cloud to do some specific actions related to environment management.

- *set-unomi-root-password.yml*: update jCustomer root password

## Monitoring

Each node is monitored on Datadog thanks to an agent directly installed on containers.

Datadog API key (pointing to a specific organization) is set as an envvar, and a periodic script update Datadog conf in case this envvar or any tag is changed so that the agent is still sending metrics to the right place.
