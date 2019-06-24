# Release note

## actual version: v1.1

### v1.1 (2019-06-24)
* revamp the Unomi targetting:
    * rename setting `unommidns` to `unomienv`
    * `unomienv` is now an envlist
    * set `envLink` in Unomi's `cp` node group as a _NodeGroupData_
        * created if not present
        * do nothing if the _DX_ env is already in
        * add the _DX_ env if not in (values are commo separated)
