# SPINE102
# Table of Contents

# Management


## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.0.0.12/24 | 10.0.0.1 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   no shutdown
   vrf MGMT
   ip address 10.0.0.12/24
```







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


## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | CVP-ACL | - |

### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
      ip access-group CVP-ACL
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

# Spanning Tree

## Spanning Tree Summary

STP mode: **none**

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 3800 | 4000 |

## Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 3800 4000
```

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



## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_LEAF101_Ethernet18 | routed | - | 10.128.4.2/31 | default | 1500 | false | - | - |
| Ethernet2 | P2P_LINK_TO_LEAF102_Ethernet18 | routed | - | 10.128.4.6/31 | default | 1500 | false | - | - |
| Ethernet3 | P2P_LINK_TO_BLEAF101_Ethernet18 | routed | - | 10.128.4.58/31 | default | 1500 | false | - | - |
| Ethernet4 | P2P_LINK_TO_BLEAF102_Ethernet18 | routed | - | 10.128.4.62/31 | default | 1500 | false | - | - |
| Ethernet5 | P2P_LINK_TO_LEAFB101_Ethernet18 | routed | - | 10.128.4.10/31 | default | 1500 | false | - | - |
| Ethernet6 | P2P_LINK_TO_LEAFB102_Ethernet18 | routed | - | 10.128.4.14/31 | default | 1500 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_LEAF101_Ethernet18
   no shutdown
   mtu 1500
   no switchport
   ip address 10.128.4.2/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet2
   description P2P_LINK_TO_LEAF102_Ethernet18
   no shutdown
   mtu 1500
   no switchport
   ip address 10.128.4.6/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet3
   description P2P_LINK_TO_BLEAF101_Ethernet18
   no shutdown
   mtu 1500
   no switchport
   ip address 10.128.4.58/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet4
   description P2P_LINK_TO_BLEAF102_Ethernet18
   no shutdown
   mtu 1500
   no switchport
   ip address 10.128.4.62/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet5
   description P2P_LINK_TO_LEAFB101_Ethernet18
   no shutdown
   mtu 1500
   no switchport
   ip address 10.128.4.10/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet6
   description P2P_LINK_TO_LEAFB102_Ethernet18
   no shutdown
   mtu 1500
   no switchport
   ip address 10.128.4.14/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
```



## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.128.0.250/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.128.0.250/32
   ip ospf area 0.0.0.0
```




# Routing


## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```



## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| MGMT | false |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
no ip icmp redirect
```

## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| MGMT | false |


## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT | 0.0.0.0/0 | 10.0.0.1 | - | 1 | - | - | - |

### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 10.0.0.1
```


## ARP

Global ARP timeout: 270

## Router OSPF

### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 100 | 10.128.0.250 | enabled | Ethernet1 <br> Ethernet2 <br> Ethernet3 <br> Ethernet4 <br> Ethernet5 <br> Ethernet6 <br> | disabled | 12000 | disabled | disabled | - | - | - | - |

### OSPF Interfaces

| Interface | Area | Cost | Point To Point |
| -------- | -------- | -------- | -------- |
| Ethernet1 | 0.0.0.0 | - | True |
| Ethernet2 | 0.0.0.0 | - | True |
| Ethernet3 | 0.0.0.0 | - | True |
| Ethernet4 | 0.0.0.0 | - | True |
| Ethernet5 | 0.0.0.0 | - | True |
| Ethernet6 | 0.0.0.0 | - | True |
| Loopback0 | 0.0.0.0 | - | - |

### Router OSPF Device Configuration

```eos
!
router ospf 100
   router-id 10.128.0.250
   passive-interface default
   no passive-interface Ethernet1
   no passive-interface Ethernet2
   no passive-interface Ethernet3
   no passive-interface Ethernet4
   no passive-interface Ethernet5
   no passive-interface Ethernet6
   max-lsa 12000
```
# AZ1

# Table of Contents

<!-- toc -->
<!-- toc -->
# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| LAB1_AZ1 | l3leaf | BLEAF101 | 10.0.0.21/24 | VEOS-LAB | Provisioned |
| LAB1_AZ1 | l3leaf | BLEAF102 | 10.0.0.22/24 | VEOS-LAB | Provisioned |
| LAB1_AZ1 | l3leaf | LEAF101 | 10.0.0.31/24 | - | Provisioned |
| LAB1_AZ1 | l3leaf | LEAF102 | 10.0.0.32/24 | - | Provisioned |
| LAB1_AZ1 | l3leaf | LEAFB101 | 10.0.0.33/24 | - | Provisioned |
| LAB1_AZ1 | l3leaf | LEAFB102 | 10.0.0.34/24 | - | Provisioned |
| LAB1_AZ1 | spine | SPINE101 | 10.0.0.11/24 | - | Provisioned |
| LAB1_AZ1 | spine | SPINE102 | 10.0.0.12/24 | - | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | BLEAF101 | Ethernet17 | spine | SPINE101 | Ethernet3 |
| l3leaf | BLEAF101 | Ethernet18 | spine | SPINE102 | Ethernet3 |
| l3leaf | BLEAF101 | Ethernet19 | mlag_peer | BLEAF102 | Ethernet19 |
| l3leaf | BLEAF101 | Ethernet20 | mlag_peer | BLEAF102 | Ethernet20 |
| l3leaf | BLEAF102 | Ethernet17 | spine | SPINE101 | Ethernet4 |
| l3leaf | BLEAF102 | Ethernet18 | spine | SPINE102 | Ethernet4 |
| l3leaf | LEAF101 | Ethernet19 | mlag_peer | LEAF102 | Ethernet19 |
| l3leaf | LEAF101 | Ethernet20 | mlag_peer | LEAF102 | Ethernet20 |
| l3leaf | LEAF102 | Ethernet17 | spine | SPINE101 | Ethernet2 |
| l3leaf | LEAF102 | Ethernet18 | spine | SPINE102 | Ethernet2 |
| l3leaf | LEAFB101 | Ethernet17 | spine | SPINE101 | Ethernet5 |
| l3leaf | LEAFB101 | Ethernet18 | spine | SPINE102 | Ethernet5 |
| l3leaf | LEAFB101 | Ethernet19 | mlag_peer | LEAFB102 | Ethernet19 |
| l3leaf | LEAFB101 | Ethernet20 | mlag_peer | LEAFB102 | Ethernet20 |
| l3leaf | LEAFB102 | Ethernet17 | spine | SPINE101 | Ethernet6 |
| l3leaf | LEAFB102 | Ethernet18 | spine | SPINE102 | Ethernet6 |
| spine | SPINE101 | Ethernet1 | l3leaf | LEAF101 | Ethernet17 |
| spine | SPINE102 | Ethernet1 | l3leaf | LEAF101 | Ethernet18 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.128.4.0/23 | 512 | 22 | 4.3 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| BLEAF101 | Ethernet17 | 10.128.4.57/31 | SPINE101 | Ethernet3 | 10.128.4.56/31 |
| BLEAF101 | Ethernet18 | 10.128.4.59/31 | SPINE102 | Ethernet3 | 10.128.4.58/31 |
| BLEAF102 | Ethernet17 | 10.128.4.61/31 | SPINE101 | Ethernet4 | 10.128.4.60/31 |
| BLEAF102 | Ethernet18 | 10.128.4.63/31 | SPINE102 | Ethernet4 | 10.128.4.62/31 |
| LEAF102 | Ethernet17 | 10.128.4.5/31 | SPINE101 | Ethernet2 | 10.128.4.4/31 |
| LEAF102 | Ethernet18 | 10.128.4.7/31 | SPINE102 | Ethernet2 | 10.128.4.6/31 |
| LEAFB101 | Ethernet17 | 10.128.4.9/31 | SPINE101 | Ethernet5 | 10.128.4.8/31 |
| LEAFB101 | Ethernet18 | 10.128.4.11/31 | SPINE102 | Ethernet5 | 10.128.4.10/31 |
| LEAFB102 | Ethernet17 | 10.128.4.13/31 | SPINE101 | Ethernet6 | 10.128.4.12/31 |
| LEAFB102 | Ethernet18 | 10.128.4.15/31 | SPINE102 | Ethernet6 | 10.128.4.14/31 |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.128.0.0/24 | 256 | 8 | 3.13 % |
| 10.128.0.248/29 | 8 | 2 | 25.0 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| LAB1_AZ1 | BLEAF101 | 10.128.0.15/32 |
| LAB1_AZ1 | BLEAF102 | 10.128.0.16/32 |
| LAB1_AZ1 | LEAF101 | 10.128.0.1/32 |
| LAB1_AZ1 | LEAF102 | 10.128.0.2/32 |
| LAB1_AZ1 | LEAFB101 | 10.128.0.3/32 |
| LAB1_AZ1 | LEAFB102 | 10.128.0.4/32 |
| LAB1_AZ1 | SPINE101 | 10.128.0.249/32 |
| LAB1_AZ1 | SPINE102 | 10.128.0.250/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.128.1.0/24 | 256 | 6 | 2.35 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| LAB1_AZ1 | BLEAF101 | 10.128.1.15/32 |
| LAB1_AZ1 | BLEAF102 | 10.128.1.15/32 |
| LAB1_AZ1 | LEAF101 | 10.128.1.1/32 |
| LAB1_AZ1 | LEAF102 | 10.128.1.1/32 |
| LAB1_AZ1 | LEAFB101 | 10.128.1.3/32 |
| LAB1_AZ1 | LEAFB102 | 10.128.1.3/32 |

# BFD

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
```

# Multicast

# Filters

## Route-maps

### Route-maps Summary

#### RM_AS_PATH_PREP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match extcommunity NO_PREPENDING |
| 20 | permit | match origin-as 64505 |
| 20 | permit | set as-path prepend auto |
| 30 | permit | match origin-as 64506 |
| 30 | permit | set as-path prepend auto |
| 40 | permit | match origin-as 64507 |
| 40 | permit | set as-path prepend auto |

### Route-maps Device Configuration

```eos
!
route-map RM_AS_PATH_PREP permit 10
   match extcommunity NO_PREPENDING
!
route-map RM_AS_PATH_PREP permit 20
   match origin-as 64505
   set as-path prepend auto
!
route-map RM_AS_PATH_PREP permit 30
   match origin-as 64506
   set as-path prepend auto
!
route-map RM_AS_PATH_PREP permit 40
   match origin-as 64507
   set as-path prepend auto
!
route-map RM_AS_PATH_PREP permit 50
```


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

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |

## VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```

# Errdisable



```eos
!
errdisable recovery interval 30
```

# Quality Of Service
