# AZ1

# Table of Contents

<!-- toc -->
<!-- toc -->
# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| LAB1_AZ1 | l3leaf | BLEAF101 | - | - | Provisioned |
| LAB1_AZ1 | l3leaf | BLEAF102 | - | - | Provisioned |
| LAB1_AZ1 | l3leaf | LEAF101 | 10.0.0.31/24 | - | Provisioned |
| LAB1_AZ1 | l3leaf | LEAF102 | - | - | Provisioned |
| LAB1_AZ1 | l3leaf | LEAFB101 | - | - | Provisioned |
| LAB1_AZ1 | l3leaf | LEAFB102 | - | - | Provisioned |
| LAB1_AZ1 | spine | SPINE101 | - | - | Provisioned |
| LAB1_AZ1 | spine | SPINE102 | - | - | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | LEAF101 | Ethernet17 | spine | SPINE101 | Ethernet1 |
| l3leaf | LEAF101 | Ethernet18 | spine | SPINE102 | Ethernet1 |
| l3leaf | LEAF101 | Ethernet19 | mlag_peer | LEAF102 | Ethernet19 |
| l3leaf | LEAF101 | Ethernet20 | mlag_peer | LEAF102 | Ethernet20 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.128.4.0/23 | 512 | 2 | 0.4 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.128.0.0/24 | 256 | 1 | 0.4 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| LAB1_AZ1 | LEAF101 | 10.128.0.1/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.128.1.0/24 | 256 | 1 | 0.4 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| LAB1_AZ1 | LEAF101 | 10.128.1.1/32 |
