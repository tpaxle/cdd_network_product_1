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
