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
