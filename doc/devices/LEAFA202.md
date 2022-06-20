# LEAFA202
# Table of Contents

# Management








## NTP

### NTP Summary

#### NTP Local Interface

| Interface | VRF |
| --------- | --- |
| Management1 | MGMT |

#### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| 10.0.0.1 | MGMT | True | - | - | - | - | - | - | - |

### NTP Device Configuration

```eos
!
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 10.0.0.1 prefer
```




## Management SSH

### IPv4 ACL

| IPv4 ACL | VRF |
| -------- | --- |
| MGMT-ACL | MGMT |

 ### SSH timeout and management

| Idle Timeout | SSH Management |
| ------------ | -------------- |
| 5 | Enabled |

### Max number of SSH sessions limit and per-host limit

| Connection Limit | Max from a single Host |
| ---------------- | ---------------------- |
| - | - |

### Ciphers and algorithms

| Ciphers | Key-exchange methods | MAC algorithms | Hostkey server algorithms |
|---------|----------------------|----------------|---------------------------|
| default | default | default | default |

### VRFs

| VRF | Status |
| --- | ------ |
| MGMT | Enabled |

### Management SSH Configuration

```eos
!
management ssh
   ip access-group MGMT-ACL vrf MGMT in
   idle-timeout 5
   no shutdown
   vrf MGMT
      no shutdown
```




## Management Console

### Management Console Timeout

Management Console Timeout is set to **15** minutes.

### Management Console Configuration

```eos
!
management console
   idle-timeout 15
```



# Authentication

## Local Users

### Local Users Summary

| User | Privilege | Role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |
| admin3 | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 $6$h3fKZwL2dRkIh1/E$lH8WzalZU0SWcd43poT4JUjrHb3n/2o7WMV0Brw3SlpYfDN8SlGDWIYJ6t0KWtZzHa2.hSzvP2uMGIEZoDfts/
username admin3 privilege 15 role network-admin secret sha512 $6$h3fKZwL2dRkIh1/E$lH8WzalZU0SWcd43poT4JUjrHb3n/2o7WMV0Brw3SlpYfDN8SlGDWIYJ6t0KWtZzHa2.hSzvP2uMGIEZoDfts/
```

## Enable Password

sha512 encrypted enable password is configured
### Enable password configuration

```eos
enable password sha512 $6$h3fKZwL2dRkIh1/E$lH8WzalZU0SWcd43poT4JUjrHb3n/2o7WMV0Brw3SlpYfDN8SlGDWIYJ6t0KWtZzHa2.hSzvP2uMGIEZoDfts/
!
```

## IP TACACS Source Interfaces

### IP TACACS Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| MGMT | Management1 |

### IP TACACS Source Interfaces Device Configuration

```eos
!
ip tacacs vrf MGMT source-interface Management1
```

## AAA Authentication

### AAA Authentication Summary

| Type | Sub-type | User Stores |
| ---- | -------- | ---------- |
| Login | default | local |
| Login | console | local |

AAA Authentication on-failure log has been enabled

AAA Authentication on-success log has been enabled

### AAA Authentication Device Configuration

```eos
!
aaa authentication login default local
aaa authentication login console local
aaa authentication policy on-failure log
aaa authentication policy on-success log
!
```

## AAA Authorization

### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |
| Exec | local |

Authorization for configuration commands is disabled.

### AAA Authorization Privilege Levels Summary

| Privilege Level | User Stores |
| --------------- | ----------- |
| 15 | local |

### AAA Authorization Device Configuration

```eos
!
aaa authorization exec default local
!
```

# Management Security

## Management Security Summary

| Settings | Value |
| -------- | ----- |
| Common password encryption key | True |

## Management Security Configuration

```eos
!
management security
   password encryption-key common
```

# Monitoring

## TerminAttr Daemon

### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 192.168.100.131:9910,192.168.100.132:9910,192.168.100.133:9910 | MGMT | token,/tmp/token | - | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.168.100.131:9910,192.168.100.132:9910,192.168.100.133:9910 -cvauth=token,/tmp/token -cvvrf=MGMT -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

## Logging

### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |
| Console | notifications |
| Monitor | debugging |
| Buffer | notifications |
| Trap | debugging |

| Format Type | Setting |
| ----------- | ------- |
| Timestamp | high-resolution |
| Hostname | hostname |
| Sequence-numbers | false |

| VRF | Source Interface |
| --- | ---------------- |
| - | Management1 |
| MGMT | Management1 |

| VRF | Hosts | Ports | Protocol |
| --- | ----- | ----- | -------- |
| MGMT | 10.0.0.1 | Default | UDP |

### Logging Servers and Features Device Configuration

```eos
!
logging console notifications
logging monitor debugging
logging buffered 8000 notifications
logging trap debugging
logging format timestamp high-resolution
logging source-interface Management1
logging vrf MGMT source-interface Management1
logging vrf MGMT host 10.0.0.1
```

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | - | All | Enabled |
| - | - |  | Enabled |
| - | - | bridge arista-mac-age, bridge arista-mac-learn, bridge arista-mac-move | Disabled |

### SNMP Local Interfaces

| Local Interface | VRF |
| --------------- | --- |
| Management1 | MGMT |

### SNMP VRF Status

| VRF | Status |
| --- | ------ |
| MGMT | Enabled |

### SNMP Hosts Configuration

| Host | VRF | Community | Username | Authentication level | SNMP Version |
| ---- |---- | --------- | -------- | -------------------- | ------------ |
| 172.29.194.41 | MGMT | - | user1 | priv | 3 |

### SNMP Communities

| Community | Access | Access List IPv4 | Access List IPv6 | View |
| --------- | ------ | ---------------- | ---------------- | ---- |
| snmp_community1 | rw | - | - | - |

### SNMP Groups Configuration

| Group | SNMP Version | Authentication | Read | Write | Notify |
| ----- | ------------ | -------------- | ---- | ----- | ------ |
| Group1 | v3 | priv | - | - | - |

### SNMP Users Configuration

| User | Group | Version | Authentication | Privacy | Remote Address | Remote Port | Engine ID |
| ---- | ----- | ------- | -------------- | ------- | -------------- | ----------- | --------- |
| user1 | Group1 | v3 | sha | aes | - | - | - |

### SNMP Device Configuration

```eos
!
snmp-server vrf MGMT local-interface Management1
snmp-server community snmp_community1 rw
snmp-server group Group1 v3 priv
snmp-server user user1 Group1 v3 auth sha test priv aes test
snmp-server host 172.29.194.41 vrf MGMT version 3 priv user1
snmp-server enable traps
no snmp-server enable traps bridge arista-mac-age
no snmp-server enable traps bridge arista-mac-learn
no snmp-server enable traps bridge arista-mac-move
snmp-server vrf MGMT
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

**Default Allocation Policy**

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 4094 |

# Interfaces

## Switchport Default

### Switchport Defaults Summary

- Default Switchport Mode: routed

### Switchport Default Configuration

```eos
!
switchport default mode routed
```


## Interface Defaults

### Interface Defaults Summary

- Default Ethernet Interface Shutdown: True

- Default Routed Interface MTU: 1500

### Interface Defaults Configuration

```eos
!
interface defaults
   ethernet
      shutdown
   mtu 1500
```








# Routing





## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |

### IP Routing Device Configuration

```eos
no ip icmp redirect
```

## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |



## ARP

Global ARP timeout: 270
# AZ2

# Table of Contents

<!-- toc -->
<!-- toc -->
# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| LAB1_AZ2 | l3leaf | BLEAF201 | 10.0.0.121/24 | VEOS-LAB | Provisioned |
| LAB1_AZ2 | l3leaf | BLEAF202 | 10.0.0.122/24 | VEOS-LAB | Provisioned |
| LAB1_AZ2 | l3leaf | LEAFA201 | 10.0.0.131/24 | - | Provisioned |
| LAB1_AZ2 | l3leaf | LEAFA202 | 10.0.0.132/24 | - | Provisioned |
| LAB1_AZ2 | l3leaf | LEAFB201 | 10.0.0.133/24 | - | Provisioned |
| LAB1_AZ2 | l3leaf | LEAFB202 | 10.0.0.134/24 | - | Provisioned |
| LAB1_AZ2 | spine | SPINE201 | 10.0.0.111/24 | - | Provisioned |
| LAB1_AZ2 | spine | SPINE202 | 10.0.0.112/24 | - | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.129.4.0/23 | 512 | 0 | 0.0 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.129.0.0/24 | 256 | 0 | 0.0 % |
| 10.129.0.248/29 | 8 | 0 | 0.0 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.129.1.0/24 | 256 | 0 | 0.0 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |

# Multicast

# Filters


# ACL

## Standard Access-lists

### Standard Access-lists Summary

#### CVP-ACL

| Sequence | Action |
| -------- | ------ |
| 10 | permit 0.0.0.0/0 |

#### MGMT-ACL

| Sequence | Action |
| -------- | ------ |
| 10 | permit 0.0.0.0/0 |

### Standard Access-lists Device Configuration

```eos
!
ip access-list standard CVP-ACL
   10 permit 0.0.0.0/0
!
ip access-list standard MGMT-ACL
   10 permit 0.0.0.0/0
```

# Errdisable



```eos
!
errdisable recovery interval 30
```

# Quality Of Service
