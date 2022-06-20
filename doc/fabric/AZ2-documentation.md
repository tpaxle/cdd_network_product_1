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
| l3leaf | BLEAF201 | Ethernet17 | spine | SPINE201 | Ethernet5 |
| l3leaf | BLEAF201 | Ethernet18 | spine | SPINE202 | Ethernet5 |
| l3leaf | BLEAF201 | Ethernet19 | mlag_peer | BLEAF202 | Ethernet19 |
| l3leaf | BLEAF201 | Ethernet20 | mlag_peer | BLEAF202 | Ethernet20 |
| l3leaf | BLEAF202 | Ethernet17 | spine | SPINE201 | Ethernet6 |
| l3leaf | BLEAF202 | Ethernet18 | spine | SPINE202 | Ethernet6 |
| l3leaf | LEAFA201 | Ethernet17 | spine | SPINE201 | Ethernet1 |
| l3leaf | LEAFA201 | Ethernet18 | spine | SPINE202 | Ethernet1 |
| l3leaf | LEAFA201 | Ethernet19 | mlag_peer | LEAFA202 | Ethernet19 |
| l3leaf | LEAFA201 | Ethernet20 | mlag_peer | LEAFA202 | Ethernet20 |
| l3leaf | LEAFA202 | Ethernet17 | spine | SPINE201 | Ethernet2 |
| l3leaf | LEAFA202 | Ethernet18 | spine | SPINE202 | Ethernet2 |
| l3leaf | LEAFB201 | Ethernet17 | spine | SPINE201 | Ethernet3 |
| l3leaf | LEAFB201 | Ethernet18 | spine | SPINE202 | Ethernet3 |
| l3leaf | LEAFB201 | Ethernet19 | mlag_peer | LEAFB202 | Ethernet19 |
| l3leaf | LEAFB201 | Ethernet20 | mlag_peer | LEAFB202 | Ethernet20 |
| l3leaf | LEAFB202 | Ethernet17 | spine | SPINE201 | Ethernet4 |
| l3leaf | LEAFB202 | Ethernet18 | spine | SPINE202 | Ethernet4 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.129.4.0/23 | 512 | 24 | 4.69 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| BLEAF201 | Ethernet17 | 10.129.4.57/31 | SPINE201 | Ethernet5 | 10.129.4.56/31 |
| BLEAF201 | Ethernet18 | 10.129.4.59/31 | SPINE202 | Ethernet5 | 10.129.4.58/31 |
| BLEAF202 | Ethernet17 | 10.129.4.61/31 | SPINE201 | Ethernet6 | 10.129.4.60/31 |
| BLEAF202 | Ethernet18 | 10.129.4.63/31 | SPINE202 | Ethernet6 | 10.129.4.62/31 |
| LEAFA201 | Ethernet17 | 10.129.4.1/31 | SPINE201 | Ethernet1 | 10.129.4.0/31 |
| LEAFA201 | Ethernet18 | 10.129.4.3/31 | SPINE202 | Ethernet1 | 10.129.4.2/31 |
| LEAFA202 | Ethernet17 | 10.129.4.5/31 | SPINE201 | Ethernet2 | 10.129.4.4/31 |
| LEAFA202 | Ethernet18 | 10.129.4.7/31 | SPINE202 | Ethernet2 | 10.129.4.6/31 |
| LEAFB201 | Ethernet17 | 10.129.4.9/31 | SPINE201 | Ethernet3 | 10.129.4.8/31 |
| LEAFB201 | Ethernet18 | 10.129.4.11/31 | SPINE202 | Ethernet3 | 10.129.4.10/31 |
| LEAFB202 | Ethernet17 | 10.129.4.13/31 | SPINE201 | Ethernet4 | 10.129.4.12/31 |
| LEAFB202 | Ethernet18 | 10.129.4.15/31 | SPINE202 | Ethernet4 | 10.129.4.14/31 |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.129.0.0/24 | 256 | 8 | 3.13 % |
| 10.129.0.248/29 | 8 | 2 | 25.0 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| LAB1_AZ2 | BLEAF201 | 10.129.0.15/32 |
| LAB1_AZ2 | BLEAF202 | 10.129.0.16/32 |
| LAB1_AZ2 | LEAFA201 | 10.129.0.1/32 |
| LAB1_AZ2 | LEAFA202 | 10.129.0.2/32 |
| LAB1_AZ2 | LEAFB201 | 10.129.0.3/32 |
| LAB1_AZ2 | LEAFB202 | 10.129.0.4/32 |
| LAB1_AZ2 | SPINE201 | 10.129.0.249/32 |
| LAB1_AZ2 | SPINE202 | 10.129.0.250/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.129.1.0/24 | 256 | 6 | 2.35 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| LAB1_AZ2 | BLEAF201 | 10.129.1.15/32 |
| LAB1_AZ2 | BLEAF202 | 10.129.1.15/32 |
| LAB1_AZ2 | LEAFA201 | 10.129.1.1/32 |
| LAB1_AZ2 | LEAFA202 | 10.129.1.1/32 |
| LAB1_AZ2 | LEAFB201 | 10.129.1.3/32 |
| LAB1_AZ2 | LEAFB202 | 10.129.1.3/32 |
