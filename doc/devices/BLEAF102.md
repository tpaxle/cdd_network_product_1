# BLEAF102
# Table of Contents

# Management


## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.0.0.22/24 | 10.0.0.1 |

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
   ip address 10.0.0.22/24
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

## Link Tracking

### Link Tracking Groups Summary

| Group Name | Minimum Links | Recovery Delay |
| ---------- | ------------- | -------------- |
| LT_GROUP1 | - | 300 |

### Link Tracking Groups Configuration

```eos
!
link tracking group LT_GROUP1
   recovery delay 300
```

# MLAG

## MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| AZ1_BL25G | Vlan4094 | 10.128.2.28 | Port-Channel19 |

Dual primary detection is disabled.

## MLAG Device Configuration

```eos
!
mlag configuration
   domain-id AZ1_BL25G
   local-interface Vlan4094
   peer-address 10.128.2.28
   peer-link Port-Channel19
   reload-delay mlag 300
   reload-delay non-mlag 330
```

# LACP

## LACP Summary

| Port-id range | Rate-limit default | System-priority |
| ------------- | ------------------ | --------------- |
| 129 - 256 | - | - |

## LACP Device Configuration

```eos
!
lacp port-id range 129 256
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **none**

### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4093-4094**

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
no spanning-tree vlan-id 4093-4094
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

# VLANs

## VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 10 | NONPRO-TIER0-MGMT | - |
| 15 | NONPRO-TIER1-LB | - |
| 16 | NONPRO-TIER2-LB | - |
| 17 | NONPRO-TIER3-FRONT | - |
| 18 | NONPRO-TIER4-BACK | - |
| 19 | NONPRO-TIER5-LB | - |
| 3999 | MLAG_iBGP_VRF-NONPRO | LEAF_PEER_L3 |
| 4093 | LEAF_PEER_L3 | LEAF_PEER_L3 |
| 4094 | MLAG_PEER | MLAG |

## VLANs Device Configuration

```eos
!
vlan 10
   name NONPRO-TIER0-MGMT
!
vlan 15
   name NONPRO-TIER1-LB
!
vlan 16
   name NONPRO-TIER2-LB
!
vlan 17
   name NONPRO-TIER3-FRONT
!
vlan 18
   name NONPRO-TIER4-BACK
!
vlan 19
   name NONPRO-TIER5-LB
!
vlan 3999
   name MLAG_iBGP_VRF-NONPRO
   trunk group LEAF_PEER_L3
!
vlan 4093
   name LEAF_PEER_L3
   trunk group LEAF_PEER_L3
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
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
| Ethernet19 | MLAG_PEER_BLEAF101_Ethernet19 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 19 |
| Ethernet20 | MLAG_PEER_BLEAF101_Ethernet20 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 19 |

*Inherited from Port-Channel Interface

#### Link Tracking Groups

| Interface | Group Name | Direction |
| --------- | ---------- | --------- |
| Ethernet17 | LT_GROUP1 | upstream |
| Ethernet18 | LT_GROUP1 | upstream |

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_BLEAF202_Ethernet1 | routed | - | 10.214.6.4/31 | default | 1500 | false | - | - |
| Ethernet2 | P2P_LINK_TO_BLEAF201_Ethernet2 | routed | - | 10.214.6.6/31 | default | 1500 | false | - | - |
| Ethernet17 | P2P_LINK_TO_SPINE101_Ethernet4 | routed | - | 10.128.4.61/31 | default | 1500 | false | - | - |
| Ethernet18 | P2P_LINK_TO_SPINE102_Ethernet4 | routed | - | 10.128.4.63/31 | default | 1500 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_BLEAF202_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 10.214.6.4/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet2
   description P2P_LINK_TO_BLEAF201_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 10.214.6.6/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet17
   description P2P_LINK_TO_SPINE101_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 10.128.4.61/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
   link tracking group LT_GROUP1 upstream
!
interface Ethernet18
   description P2P_LINK_TO_SPINE102_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 10.128.4.63/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
   link tracking group LT_GROUP1 upstream
!
interface Ethernet19
   description MLAG_PEER_BLEAF101_Ethernet19
   no shutdown
   channel-group 19 mode active
!
interface Ethernet20
   description MLAG_PEER_BLEAF101_Ethernet20
   no shutdown
   channel-group 19 mode active
```


## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel19 | MLAG_PEER_BLEAF101_Po19 | switched | trunk | 2-4094 | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel19
   description MLAG_PEER_BLEAF101_Po19
   no shutdown
   switchport
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
```


## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.128.0.16/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 10.128.1.15/32 |
| Loopback2 | VRF-NONPRO_VTEP_DIAGNOSTICS | VRF-NONPRO | 192.168.7.16/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback2 | VRF-NONPRO_VTEP_DIAGNOSTICS | VRF-NONPRO | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.128.0.16/32
   ip ospf area 0.0.0.0
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 10.128.1.15/32
   ip ospf area 0.0.0.0
!
interface Loopback2
   description VRF-NONPRO_VTEP_DIAGNOSTICS
   no shutdown
   vrf VRF-NONPRO
   ip address 192.168.7.16/32
```


## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan10 | NONPRO-TIER0-MGMT | VRF-NONPRO | - | false |
| Vlan15 | NONPRO-TIER1-LB | VRF-NONPRO | - | false |
| Vlan16 | NONPRO-TIER2-LB | VRF-NONPRO | - | false |
| Vlan17 | NONPRO-TIER3-FRONT | VRF-NONPRO | - | false |
| Vlan18 | NONPRO-TIER4-BACK | VRF-NONPRO | - | false |
| Vlan19 | NONPRO-TIER5-LB | VRF-NONPRO | - | false |
| Vlan3999 | MLAG_PEER_L3_iBGP: vrf VRF-NONPRO | VRF-NONPRO | 1500 | false |
| Vlan4093 | MLAG_PEER_L3_PEERING | default | 1500 | false |
| Vlan4094 | MLAG_PEER | default | 1500 | false |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan10 |  VRF-NONPRO  |  -  |  192.168.10.1/25  |  -  |  -  |  -  |  -  |
| Vlan15 |  VRF-NONPRO  |  -  |  192.168.15.1/25  |  -  |  -  |  -  |  -  |
| Vlan16 |  VRF-NONPRO  |  -  |  192.168.16.1/25  |  -  |  -  |  -  |  -  |
| Vlan17 |  VRF-NONPRO  |  -  |  192.168.17.1/25  |  -  |  -  |  -  |  -  |
| Vlan18 |  VRF-NONPRO  |  -  |  192.168.18.1/25  |  -  |  -  |  -  |  -  |
| Vlan19 |  VRF-NONPRO  |  -  |  192.168.19.1/25  |  -  |  -  |  -  |  -  |
| Vlan3999 |  VRF-NONPRO  |  10.128.3.29/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4093 |  default  |  10.128.3.29/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  10.128.2.29/31  |  -  |  -  |  -  |  -  |  -  |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan10
   description NONPRO-TIER0-MGMT
   no shutdown
   vrf VRF-NONPRO
   ip address virtual 192.168.10.1/25
!
interface Vlan15
   description NONPRO-TIER1-LB
   no shutdown
   vrf VRF-NONPRO
   ip address virtual 192.168.15.1/25
!
interface Vlan16
   description NONPRO-TIER2-LB
   no shutdown
   vrf VRF-NONPRO
   ip address virtual 192.168.16.1/25
!
interface Vlan17
   description NONPRO-TIER3-FRONT
   no shutdown
   vrf VRF-NONPRO
   ip address virtual 192.168.17.1/25
!
interface Vlan18
   description NONPRO-TIER4-BACK
   no shutdown
   vrf VRF-NONPRO
   ip address virtual 192.168.18.1/25
!
interface Vlan19
   description NONPRO-TIER5-LB
   no shutdown
   vrf VRF-NONPRO
   ip address virtual 192.168.19.1/25
!
interface Vlan3999
   description MLAG_PEER_L3_iBGP: vrf VRF-NONPRO
   no shutdown
   mtu 1500
   vrf VRF-NONPRO
   ip address 10.128.3.29/31
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   no shutdown
   mtu 1500
   ip address 10.128.3.29/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 1500
   no autostate
   ip address 10.128.2.29/31
```


## VXLAN Interface

### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |

#### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 10 | 10010 | - | - |
| 15 | 10015 | - | - |
| 16 | 10016 | - | - |
| 17 | 10017 | - | - |
| 18 | 10018 | - | - |
| 19 | 10019 | - | - |

#### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| VRF-NONPRO | 1000 | - |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description BLEAF102_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 10 vni 10010
   vxlan vlan 15 vni 10015
   vxlan vlan 16 vni 10016
   vxlan vlan 17 vni 10017
   vxlan vlan 18 vni 10018
   vxlan vlan 19 vni 10019
   vxlan vrf VRF-NONPRO vni 1000
```


# Routing


## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```


## Virtual Router MAC Address

### Virtual Router MAC Address Summary

#### Virtual Router MAC Address: 00:1c:73:00:dc:01

### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:dc:01
```


## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| MGMT | false |
| VRF-NONPRO | true |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf VRF-NONPRO
no ip icmp redirect
```

## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| MGMT | false |
| VRF-NONPRO | false |


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
| 100 | 10.128.0.16 | enabled | Ethernet17 <br> Ethernet18 <br> Vlan4093 <br> Ethernet1 <br> Ethernet2 <br> | disabled | 12000 | disabled | disabled | - | - | - | - |

### OSPF Interfaces

| Interface | Area | Cost | Point To Point |
| -------- | -------- | -------- | -------- |
| Ethernet1 | 0.0.0.0 | - | True |
| Ethernet2 | 0.0.0.0 | - | True |
| Ethernet17 | 0.0.0.0 | - | True |
| Ethernet18 | 0.0.0.0 | - | True |
| Vlan4093 | 0.0.0.0 | - | True |
| Loopback0 | 0.0.0.0 | - | - |
| Loopback1 | 0.0.0.0 | - | - |

### Router OSPF Device Configuration

```eos
!
router ospf 100
   router-id 10.128.0.16
   passive-interface default
   no passive-interface Ethernet17
   no passive-interface Ethernet18
   no passive-interface Vlan4093
   no passive-interface Ethernet1
   no passive-interface Ethernet2
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
| l3leaf | LEAF101 | Ethernet17 | spine | SPINE101 | Ethernet1 |
| l3leaf | LEAF101 | Ethernet18 | spine | SPINE102 | Ethernet1 |
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

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.128.4.0/23 | 512 | 24 | 4.69 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| BLEAF101 | Ethernet17 | 10.128.4.57/31 | SPINE101 | Ethernet3 | 10.128.4.56/31 |
| BLEAF101 | Ethernet18 | 10.128.4.59/31 | SPINE102 | Ethernet3 | 10.128.4.58/31 |
| BLEAF102 | Ethernet17 | 10.128.4.61/31 | SPINE101 | Ethernet4 | 10.128.4.60/31 |
| BLEAF102 | Ethernet18 | 10.128.4.63/31 | SPINE102 | Ethernet4 | 10.128.4.62/31 |
| LEAF101 | Ethernet17 | 10.128.4.1/31 | SPINE101 | Ethernet1 | 10.128.4.0/31 |
| LEAF101 | Ethernet18 | 10.128.4.3/31 | SPINE102 | Ethernet1 | 10.128.4.2/31 |
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

## IP IGMP Snooping

### IP IGMP Snooping Summary

IGMP snooping is globally disabled

### IP IGMP Snooping Device Configuration

```eos
!
no ip igmp snooping
```

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

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| VRF-NONPRO | enabled |

## VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance VRF-NONPRO
```

# Virtual Source NAT

## Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| VRF-NONPRO | 192.168.7.16 |

## Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf VRF-NONPRO address 192.168.7.16
```

# Errdisable



```eos
!
errdisable recovery interval 30
```

# Quality Of Service
