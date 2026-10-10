# Module 07: AWS Networking and Content Delivery

## 1. Learning Objectives

* Understand Amazon VPC and cloud networking fundamentals.
* Explain subnets, route tables, internet gateways, and NAT gateways.
* Distinguish public and private subnets.
* Understand security groups and network ACLs.
* Identify Elastic Load Balancing, Amazon Route 53, and Amazon CloudFront.
* Understand VPN and AWS Direct Connect.
* Recognize common networking architectures.

## 2. Networking Fundamentals

Cloud networking connects resources and controls how traffic moves between applications, users, and external systems.

Core concepts include:

* IP addresses.
* Subnets.
* Routing.
* Network security.
* DNS.
* Internet connectivity.
* Private connectivity.
* Content delivery.

AWS provides networking services that allow customers to build isolated networks, control traffic, and connect workloads to other environments.

## 3. Amazon VPC

Amazon Virtual Private Cloud (Amazon VPC) lets customers create a logically isolated virtual network within AWS.

A VPC provides control over networking configuration, including IP address ranges, subnets, routing, and connectivity.

### Key VPC Concepts

**CIDR block:** Defines an IP address range, such as `10.0.0.0/16`.

**Subnet:** A range of IP addresses within a VPC associated with a specific Availability Zone.

**Route table:** Contains rules that determine where network traffic is directed.

**Internet gateway:** Enables supported communication between a VPC and the internet when routes and other required configurations are in place.

**NAT gateway:** Allows resources in a private subnet to initiate supported outbound IPv4 connections without accepting unsolicited inbound connections through that NAT gateway.

**Security group:** A stateful virtual firewall associated with supported network resources.

**Network ACL (NACL):** A stateless network access control list applied at the subnet level.

## 4. Public and Private Subnets

### Public Subnet

A subnet is considered public when its associated route table has a route to an internet gateway.

A resource also needs suitable addressing, security rules, and other configuration to communicate directly with the internet.

### Private Subnet

A private subnet does not have a direct route to an internet gateway.

Private resources can use other configured connectivity options, such as a NAT gateway for outbound IPv4 internet access or private network connections.

### Example Architecture

A typical three-tier application may contain:

* Public subnets for internet-facing load balancers.
* Private subnets for application servers.
* Private subnets for databases.

This design helps separate public entry points from application and data layers.

A subnet's route table—not merely the resource's name—determines whether the subnet is public or private.

## 5. Internet Gateway vs. NAT Gateway

### Internet Gateway

An internet gateway provides a target for routes between a VPC and the internet.

Public connectivity also depends on appropriate routing, IP addressing, and security configuration.

### NAT Gateway

A NAT gateway allows eligible resources in private subnets to initiate outbound IPv4 connections, such as downloading software updates.

It does not, by itself, allow unsolicited inbound internet connections to those private resources.

| Feature                                                | Internet Gateway                     | NAT Gateway                                |
| ------------------------------------------------------ | ------------------------------------ | ------------------------------------------ |
| Primary purpose                                        | VPC internet connectivity            | Outbound IPv4 access for private resources |
| Typical placement                                      | Attached to the VPC                  | Deployed in a subnet                       |
| Common scenario                                        | Public-facing resources              | Private servers downloading updates        |
| Direct unsolicited inbound access to private resources | Not provided merely by a NAT gateway | Not allowed through the NAT gateway        |

NAT gateways incur charges. Design their placement and availability according to cost and resilience requirements.

## 6. Security Groups vs. Network ACLs

### Security Groups

Security groups are stateful virtual firewalls.

* Associated with supported resources, such as EC2 instances.
* Control permitted inbound and outbound traffic.
* Return traffic for an allowed connection is automatically permitted, subject to connection tracking and service behavior.
* Support allow rules rather than explicit deny rules.

### Network ACLs

Network ACLs are stateless and operate at the subnet level.

* Support inbound and outbound rules.
* Support both allow and deny rules.
* Return traffic must be permitted by the applicable rules.
* Rules are evaluated according to rule numbers.

### Comparison

| Feature        | Security Group                                          | Network ACL                         |
| -------------- | ------------------------------------------------------- | ----------------------------------- |
| Scope          | Resource/network interface level                        | Subnet level                        |
| Stateful       | Yes                                                     | No                                  |
| Allow rules    | Yes                                                     | Yes                                 |
| Deny rules     | No                                                      | Yes                                 |
| Return traffic | Automatically allowed for tracked permitted connections | Must be allowed by applicable rules |

Security groups are commonly used for resource-level access control, while network ACLs provide an additional subnet-level control layer.

## 7. Amazon Route 53

Amazon Route 53 is a scalable DNS service that can route domain queries to appropriate destinations.

DNS translates human-readable domain names into information clients use to locate services.

### Common Capabilities

* Domain registration.
* DNS record management.
* Health checks.
* Routing policies.
* Integration with AWS and external endpoints.

### Example

A user enters `www.example.com`. DNS resolution helps the user's device find the appropriate destination for the website.

Route 53 supports several routing policies, including simple, weighted, latency-based, failover, and geolocation-based routing.

The appropriate policy depends on the application's requirements.

## 8. Amazon CloudFront

Amazon CloudFront is a content delivery network (CDN) that delivers content through a distributed global network of edge locations.

### Common Use Cases

* Static website assets.
* Images and videos.
* Dynamic web content.
* Application acceleration.
* Content delivery integrated with supported security services.

### Benefits

* Reduces latency for many content-delivery workloads.
* Can cache frequently requested content.
* Reduces repeated requests to the origin for cacheable objects.
* Supports integration with AWS security and monitoring capabilities.

CloudFront complements origin services such as Amazon S3 and application servers.

## 9. Elastic Load Balancing

Elastic Load Balancing distributes incoming application traffic across registered targets.

Common load balancer types include:

* **Application Load Balancer (ALB):** Works at the application layer and supports HTTP/HTTPS routing capabilities.
* **Network Load Balancer (NLB):** Handles connection traffic at the transport layer and supports high-performance network workloads.
* **Gateway Load Balancer (GWLB):** Helps deploy and scale virtual network appliances.

The Classic Load Balancer is a legacy option that may appear in older material.

### Example

An ALB routes HTTP requests to healthy application targets across multiple AZs. EC2 Auto Scaling adjusts the number of instances based on configured conditions.

## 10. AWS Site-to-Site VPN and AWS Direct Connect

### AWS Site-to-Site VPN

Provides an encrypted connection between an on-premises network and an Amazon VPC over supported network connectivity, commonly using the public internet.

It can be useful for hybrid networking and secure connectivity without dedicated physical connectivity.

### AWS Direct Connect

Provides dedicated network connectivity between an organization's network and AWS through a Direct Connect location.

Potential benefits include more consistent network performance and access to private connectivity options, depending on the architecture.

Direct Connect is not automatically encrypted at the physical connection layer. Additional encryption may be needed to satisfy security requirements.

### Comparison

| Feature      | Site-to-Site VPN                          | Direct Connect                               |
| ------------ | ----------------------------------------- | -------------------------------------------- |
| Connectivity | Encrypted VPN over supported connectivity | Dedicated network connection                 |
| Typical use  | Hybrid connectivity and quicker setup     | Consistent dedicated connectivity            |
| Encryption   | VPN connection provides encryption        | Encryption must be evaluated separately      |
| Setup        | Usually faster to establish               | Often requires provider and circuit planning |

## 11. VPC Peering and Transit Gateway

### VPC Peering

Connects two VPCs using private IP connectivity, subject to routing and security configuration.

VPC peering does not support transitive routing through a peer connection.

### AWS Transit Gateway

Acts as a central network hub connecting VPCs and supported on-premises networks.

It can simplify network connectivity for organizations operating many VPCs and networks.

### Example

A company has multiple application VPCs and an on-premises network. Transit Gateway can centralize supported routing connections rather than requiring a large mesh of individual peerings.

## 12. Exam-Focused Revision Notes

* Amazon VPC provides a logically isolated virtual network.
* Subnets are associated with individual Availability Zones.
* Route tables determine where traffic is directed.
* A public subnet has a route to an internet gateway.
* Private subnets do not have direct internet-gateway routing.
* NAT gateways support outbound IPv4 connectivity from private subnets.
* Security groups are stateful and support allow rules.
* Network ACLs are stateless and support allow and deny rules.
* Route 53 provides DNS and routing capabilities.
* CloudFront is a content delivery network.
* ALB supports application-layer HTTP/HTTPS routing.
* NLB supports transport-layer network traffic.
* Site-to-Site VPN provides encrypted connectivity.
* Direct Connect provides dedicated network connectivity.
* VPC peering connects VPCs but does not support transitive routing.
* Transit Gateway can act as a central hub for multiple networks.

## 13. Knowledge Check

**Question 1:** Which AWS service provides a logically isolated virtual network?

A. Amazon VPC
B. Amazon S3
C. Amazon Redshift
D. AWS Budgets

**Answer:** A — Amazon VPC provides a logically isolated virtual network.

**Question 2:** Which service allows private subnet resources to initiate outbound IPv4 internet connections without providing unsolicited inbound access through the NAT gateway?

A. NAT gateway
B. Internet gateway only
C. Amazon Route 53
D. AWS CloudTrail

**Answer:** A — A NAT gateway supports outbound IPv4 connectivity for eligible private resources.

**Question 3:** Which control is stateful and commonly associated with an EC2 instance?

A. Network ACL
B. Security group
C. Route table
D. Internet gateway

**Answer:** B — Security groups are stateful virtual firewalls.

**Question 4:** Which AWS service provides DNS management and routing policies?

A. Amazon Route 53
B. Amazon EBS
C. Amazon EFS
D. AWS Backup

**Answer:** A — Route 53 provides DNS capabilities.

**Question 5:** Which service delivers cached content through global edge locations?

A. Amazon CloudFront
B. Amazon RDS
C. Amazon EC2
D. AWS IAM

**Answer:** A — CloudFront is AWS's content delivery network.

**Question 6:** Which service provides dedicated network connectivity to AWS?

A. AWS Site-to-Site VPN
B. AWS Direct Connect
C. Amazon CloudFront
D. Amazon DynamoDB

**Answer:** B — Direct Connect provides dedicated network connectivity.

**Question 7:** Which service can centralize connectivity across multiple VPCs and on-premises networks?

A. AWS Transit Gateway
B. Amazon S3 Versioning
C. AWS Lambda
D. Amazon EBS

**Answer:** A — Transit Gateway acts as a central network hub.

## 14. Practical Exercise

Design a basic three-tier web application network with a public load balancer, private application servers, and a private database.

Identify:

1. Where each component should be placed.
2. Which gateway enables public connectivity.
3. How application servers can download software updates.
4. How access to the database should be restricted.
5. Which service can distribute incoming HTTP traffic.

### Suggested Solution

* Deploy the internet-facing load balancer in public subnets.
* Deploy application servers in private subnets.
* Place the database in private subnets with no direct public access.
* Use an internet gateway for the public entry path.
* Configure a NAT gateway if private servers require outbound IPv4 internet access.
* Use security groups to allow only the required traffic between the load balancer, application tier, and database.
* Use an Application Load Balancer for HTTP/HTTPS traffic distribution.
* Consider multiple AZs for resilience.

## 15. Official Learning Resources

* Amazon VPC: https://aws.amazon.com/vpc/
* Amazon Route 53: https://aws.amazon.com/route53/
* Amazon CloudFront: https://aws.amazon.com/cloudfront/
* Elastic Load Balancing: https://aws.amazon.com/elasticloadbalancing/
* AWS Direct Connect: https://aws.amazon.com/directconnect/
* AWS Transit Gateway: https://aws.amazon.com/transit-gateway/
* VPC Documentation: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html

## 16. Module Completion Checklist

* [ ] Explain VPCs, subnets, and route tables.
* [ ] Distinguish public and private subnets.
* [ ] Compare internet gateways and NAT gateways.
* [ ] Compare security groups and network ACLs.
* [ ] Explain Route 53 and CloudFront.
* [ ] Identify the main load balancer types.
* [ ] Compare VPN and Direct Connect.
* [ ] Explain VPC peering and Transit Gateway.
* [ ] Complete the knowledge check without consulting the answers.
