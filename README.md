zabbix-scripts
==============

Number of Zabbix scripts and templates for custom monitoring

## PREREQUISITES
1. Python >=2.6
2. Check service-specific requirements in scripts itself 

## INSTALLATION

Please follow the steps below to integrate it with your Zabbix:

1. Import templates into Zabbix
2. Copy scripts into monitored servers (usually at /etc/zabbix/users-scripts)
3. Update zabbix-agent config. Add User Parameters.

__Zookeeper__

```UserParameter=zookeeper[*],/etc/zabbix/user_scripts/check_zookeeper.py -s localhost:2181 -o zabbix -k "$1"
```

__Nginx__

```UserParameter=nginx[*],/etc/zabbix/user_scripts/check_nginx.sh "$1" "$2"
```

__MongoDB__

```UserParameter=mongo[*],/etc/zabbix/user_scripts/check_mongo.py -n locahost -p "$1"
```

4. Restart zabbix agent.
