# Module 02: AWS Global Infrastructure

## 1. Learning Objectives

* Understand AWS Regions and Availability Zones.
* Explain edge locations and Points of Presence.
* Understand how global infrastructure supports availability, resilience, and performance.
* Select appropriate Regions for different workloads.
* Understand data residency, latency, and disaster recovery considerations.

## 2. Overview of AWS Global Infrastructure

AWS operates a global infrastructure that allows customers to deploy applications close to users, distribute workloads across isolated locations, and design resilient architectures.

The main concepts are:

* AWS Regions
* Availability Zones (AZs)
* Data centers
* Edge locations
* Regional and global AWS services

AWS continually expands its infrastructure. Always consult the official infrastructure page for the current Region and Availability Zone list.

Official resource: https://aws.amazon.com/about-aws/global-infrastructure/

## 3. AWS Regions

An AWS Region is a separate geographic area containing multiple Availability Zones.

Each Region is designed to be independent of other Regions, helping customers isolate workloads and plan for regional failures.

### Why Choose a Region?

Consider the following factors:

1. **Latency:** Choose a Region close to users when low response time is important.
2. **Compliance:** Check whether regulations require data to remain in a particular geographic area.
3. **Service availability:** Confirm that the required AWS services and features are available in the selected Region.
4. **Cost:** Pricing can vary by Region.
5. **Disaster recovery:** Consider whether a secondary Region is appropriate for business continuity.

### Example

An Egyptian business serving customers in Europe might evaluate nearby AWS Regions based on application latency, legal requirements, service availability, and cost. Geographic proximity alone does not determine the best Region.

## 4. Availability Zones

An Availability Zone is one or more discrete data centers with redundant power, networking, and connectivity within an AWS Region.

Availability Zones are designed to have independent infrastructure and are connected through high-bandwidth, low-latency networking.

### Why Use Multiple Availability Zones?

A workload deployed across multiple AZs can continue operating when an individual AZ experiences a failure, provided the application and its dependencies are designed appropriately.

**Example:** A web application runs application instances in two Availability Zones behind a load balancer. If one AZ becomes unavailable, traffic can be directed to healthy instances in the other AZ.

Multiple AZs do not automatically make every application highly available. The architecture must account for databases, storage, networking, health checks, and failover.

## 5. Data Centers

Data centers contain the physical infrastructure used to operate cloud services, including servers, networking equipment, power systems, and cooling systems.

Customers generally do not choose or manage the exact physical data center hosting their standard AWS resources. They select the appropriate Region and, where supported, Availability Zone.

## 6. Edge Locations and Points of Presence

AWS uses edge infrastructure to bring certain services closer to end users.

Edge locations are used by services such as Amazon CloudFront to deliver cached content with lower latency.

### Example: Amazon CloudFront

A website stores images and other static assets in an origin location. CloudFront can cache those assets at edge locations closer to viewers.

When a viewer requests cached content, the content can be delivered from the edge rather than repeatedly retrieved from the origin.

Benefits can include:

* Lower content-delivery latency.
* Reduced load on the origin.
* Improved user experience.
* Integration with additional security capabilities.

Edge locations are different from Availability Zones. They serve different architectural purposes.

## 7. Regional Services and Global Services

AWS services do not all operate at the same geographic scope.

### Regional Services

Resources are created or managed within a selected Region.

Examples include:

* Amazon EC2 instances.
* Amazon RDS databases.
* Amazon VPC networks.

Availability and regional behavior vary by service.

### Global or Globally Accessible Services

Some AWS services provide management capabilities across Regions or are designed for global use.

Examples include:

* AWS Identity and Access Management (IAM), whose core resources are managed globally.
* Amazon Route 53, a global DNS service.
* Amazon CloudFront, a global content delivery network.

A global service does not mean every resource or piece of data is automatically replicated worldwide. Always check the service's actual data-location and replication behavior.

## 8. AWS Infrastructure and High Availability

### Single Availability Zone

A workload in one AZ may be affected if that AZ experiences a disruption.

### Multiple Availability Zones

Distributing application components across multiple AZs can reduce the impact of an individual AZ failure.

### Multiple Regions

A multi-Region architecture can support disaster recovery and geographic resilience, but it adds cost and operational complexity.

The appropriate design depends on recovery objectives, business impact, regulatory requirements, and budget.

## 9. Disaster Recovery Concepts

### Recovery Time Objective (RTO)

The maximum targeted duration of service disruption before the service must be restored.

### Recovery Point Objective (RPO)

The maximum targeted amount of data loss measured in time.

**Example:** If an application has an RPO of 15 minutes, its disaster recovery design aims to limit data loss to approximately 15 minutes of updates or less.

Common disaster recovery approaches include:

* Backup and restore.
* Pilot light.
* Warm standby.
* Multi-site active/active.

These strategies generally differ in cost, recovery speed, and operational complexity.

## 10. Choosing a Region: Practical Scenario

A company wants to host a customer portal for users in several countries.

Its team should:

1. Identify where most customers are located.
2. Evaluate latency from candidate Regions.
3. Confirm required AWS services are available.
4. Review data residency and regulatory obligations.
5. Compare service costs.
6. Select an availability architecture.
7. Evaluate whether a second Region is needed for disaster recovery.

The closest Region is not necessarily the best if it lacks a required service or fails to meet compliance requirements.

## 11. Exam-Focused Revision Notes

* A Region is a separate geographic area.
* An Availability Zone consists of one or more discrete data centers.
* AZs within a Region are connected using high-bandwidth, low-latency networking.
* Multiple AZs can improve resilience against an AZ-level failure.
* Edge locations support services such as CloudFront for low-latency content delivery.
* Route 53 provides DNS services.
* IAM is a global service for core identity and access management resources.
* Many AWS resources are Region-specific.
* A multi-Region architecture can support disaster recovery but typically increases complexity and cost.
* RTO concerns recovery time; RPO concerns acceptable data loss.
* AWS global infrastructure does not mean all data is automatically copied across every Region.

## 12. Knowledge Check

**Question 1:** Which AWS infrastructure component represents a separate geographic area?

A. Edge location
B. Availability Zone
C. Region
D. EC2 instance

**Answer:** C — A Region is a separate geographic area.

**Question 2:** A company wants to improve application resilience against a failure affecting one Availability Zone. What should it consider?

A. Deploying redundant application components across multiple AZs
B. Using a larger monitor
C. Moving all resources into a single AZ
D. Disabling health checks

**Answer:** A — Multi-AZ architecture can reduce the impact of an AZ-level failure.

**Question 3:** Which service uses edge locations to help deliver cached content globally?

A. Amazon RDS
B. Amazon CloudFront
C. Amazon EBS
D. AWS IAM

**Answer:** B — CloudFront is a content delivery network.

**Question 4:** Which factor is important when selecting an AWS Region?

A. Only the color of the AWS console
B. Latency, compliance, cost, and service availability
C. The number of developers using Windows
D. Whether the customer owns a physical server

**Answer:** B — Region selection involves several business and technical considerations.

**Question 5:** What does RPO measure?

A. Target recovery time
B. Acceptable data loss measured in time
C. Number of Availability Zones
D. Network bandwidth

**Answer:** B — RPO defines the targeted limit on data loss.

## 13. Practical Exercise

Design a high-level architecture for a website used by customers in two countries.

Answer the following:

1. What factors would determine the primary Region?
2. Why might multiple Availability Zones be appropriate?
3. How could CloudFront improve delivery of static assets?
4. When would a secondary Region be justified?
5. How would you explain the trade-off between resilience and cost?

### Suggested Solution

Select the primary Region based on latency, compliance, service availability, and cost. Deploy application components across multiple AZs where appropriate, and use CloudFront for caching and content delivery. Consider a secondary Region when recovery requirements justify the extra cost and operational complexity. Define RTO and RPO before choosing the disaster recovery strategy.

## 14. Official Learning Resources

* AWS Global Infrastructure: https://aws.amazon.com/about-aws/global-infrastructure/
* AWS Regions and Availability Zones: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html
* Amazon CloudFront: https://aws.amazon.com/cloudfront/
* Amazon Route 53: https://aws.amazon.com/route53/
* AWS Disaster Recovery: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html

## 15. Module Completion Checklist

* [ ] Explain Regions, AZs, data centers, and edge locations.
* [ ] Identify the main Region selection factors.
* [ ] Explain how multi-AZ deployment improves resilience.
* [ ] Distinguish regional services from global services.
* [ ] Define RTO and RPO.
* [ ] Explain the role of CloudFront.
* [ ] Complete the knowledge check without consulting the answers.
