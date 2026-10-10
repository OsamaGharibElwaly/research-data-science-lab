# Module 06: AWS Database Services

## 1. Learning Objectives

* Understand relational and non-relational databases.
* Identify Amazon RDS, Amazon Aurora, Amazon DynamoDB, and Amazon Redshift.
* Explain managed database services.
* Understand database availability, scaling, and backup concepts.
* Identify AWS database services for common business scenarios.
* Distinguish transactional databases from analytical data warehouses.

## 2. Database Fundamentals

A database stores and organizes data so applications can retrieve, modify, and analyze it.

The appropriate database depends on data structure, query patterns, consistency requirements, performance, scale, and operational needs.

Two major database categories are:

### Relational Databases

Store data in structured tables containing rows and columns, often using SQL.

Typical use cases include:

* Financial transactions.
* Customer records.
* Order management.
* Inventory systems.
* Applications requiring relationships between structured records.

### Non-Relational Databases

Often called NoSQL databases, these support data models such as key-value, document, graph, or wide-column structures.

Typical use cases include:

* High-scale applications.
* Flexible data models.
* Low-latency access patterns.
* Event-driven applications.
* Applications with changing data structures.

Neither category is universally better. The right choice depends on application requirements.

## 3. Amazon RDS

Amazon Relational Database Service (Amazon RDS) is a managed service for running supported relational database engines.

Supported engines include options such as MySQL, PostgreSQL, MariaDB, Oracle Database, Microsoft SQL Server, and Amazon Aurora.

### Responsibilities Managed by AWS

Depending on the engine and configuration, AWS manages tasks such as:

* Underlying infrastructure provisioning.
* Routine infrastructure maintenance.
* Supported backup automation.
* Software patching within configured maintenance policies.
* Monitoring integrations.

Customers remain responsible for appropriate database configuration, access control, schema design, query performance, and data protection settings.

### Common Use Cases

* E-commerce databases.
* Business applications.
* Customer management systems.
* Transactional applications.
* Applications that need a managed relational database.

### Example

An online store stores customers, orders, products, and payments in a relational database managed by Amazon RDS.

## 4. Amazon RDS Multi-AZ

Amazon RDS supports Multi-AZ configurations designed to improve database availability.

Depending on the deployment type, AWS can maintain standby infrastructure or distribute database instances across Availability Zones.

### Benefits

* Improved availability.
* Support for failover when eligible failures occur.
* Reduced need to manage underlying database infrastructure manually.

A Multi-AZ standby is generally designed for availability and failover, not as a read-scaling replica.

Read-scaling architectures may instead use supported read replicas or other database-specific approaches.

Multi-AZ configurations do not eliminate every failure scenario and do not replace appropriate backup and recovery practices.

## 5. Amazon RDS Read Replicas

Read replicas provide additional database instances that can serve read queries for supported database engines and configurations.

### Why Use Read Replicas?

* Offload read traffic from the primary database.
* Improve read scalability.
* Support certain reporting or analytics workloads.

Replication behavior, lag, supported configurations, and promotion options depend on the database engine.

### Multi-AZ vs. Read Replicas

| Feature                 | Multi-AZ                                                         | Read Replica                              |
| ----------------------- | ---------------------------------------------------------------- | ----------------------------------------- |
| Primary purpose         | Availability and failover                                        | Read scaling                              |
| Typical use             | Reduce database downtime                                         | Distribute read queries                   |
| Automatic failover      | Supported for appropriate configurations                         | Not the primary purpose                   |
| Read traffic offloading | Depends on architecture; standby is generally not used for reads | Yes, when application queries the replica |

## 6. Amazon Aurora

Amazon Aurora is a relational database service compatible with supported MySQL and PostgreSQL versions.

It is designed for cloud workloads that need relational database capabilities and a distributed storage architecture.

### Key Characteristics

* Managed relational database experience.
* Compatibility with supported MySQL and PostgreSQL applications.
* Distributed storage architecture.
* Availability and scaling options depending on configuration.
* Integration with AWS database management capabilities.

### Common Use Cases

* Enterprise applications.
* High-demand transactional systems.
* Applications requiring MySQL or PostgreSQL compatibility.
* Cloud-native applications with demanding database requirements.

Aurora is not identical to standard Amazon RDS deployments. The available capabilities and pricing differ by engine, configuration, and Region.

## 7. Amazon DynamoDB

Amazon DynamoDB is a fully managed NoSQL database service supporting key-value and document data models.

It is designed for applications that need predictable, low-latency access patterns and scalable managed database infrastructure.

### Key Concepts

**Table:** A collection of items.

**Item:** A record in a table.

**Attribute:** A data element associated with an item.

**Partition key:** An attribute used to determine data distribution and access patterns.

**Sort key:** An optional key attribute that can organize and query related items within a partition-key grouping.

### Common Use Cases

* Shopping carts.
* User session data.
* Gaming applications.
* Device and event metadata.
* High-scale application backends.

### Example

An application stores user session information in DynamoDB, using a user identifier as a partition key.

DynamoDB is not a direct replacement for every relational database. Its data model and access patterns should be designed around the application's queries.

## 8. Amazon Redshift

Amazon Redshift is a cloud data warehousing service designed for analytical workloads.

It supports querying and analyzing large datasets to support reporting, business intelligence, and decision-making.

### Common Use Cases

* Business intelligence.
* Enterprise reporting.
* Aggregation of data from multiple systems.
* Analytical SQL queries.
* Data warehouse workloads.

### OLTP vs. OLAP

**Online Transaction Processing (OLTP):** Handles operational transactions such as creating an order or updating a customer record.

**Online Analytical Processing (OLAP):** Supports complex analysis, aggregation, and reporting across large datasets.

| Characteristic      | OLTP                           | OLAP                               |
| ------------------- | ------------------------------ | ---------------------------------- |
| Typical task        | Insert or update a transaction | Analyze historical sales           |
| Workload            | Frequent operational queries   | Analytical and aggregation queries |
| Example AWS service | Amazon RDS                     | Amazon Redshift                    |

The distinction is conceptual; actual architecture choices depend on the workload.

## 9. Other AWS Database Services

### Amazon ElastiCache

Provides managed in-memory caching using supported engines such as Valkey and Redis OSS, subject to current service offerings.

Use cases include caching frequently requested data and reducing database load.

### Amazon DocumentDB

A managed document database service with MongoDB compatibility for supported features and versions.

Useful for document-oriented application workloads that need the supported compatibility model.

### Amazon Neptune

A managed graph database service designed for applications that model relationships between entities.

Examples include relationship analysis and knowledge graphs.

### Amazon MemoryDB

A durable in-memory database service designed for use cases requiring very low latency and high throughput.

Service capabilities and suitability depend on the application requirements.

## 10. Choosing an AWS Database Service

### Scenario A: Traditional Transactional Application

A company needs a relational database for customers and orders.

**Likely choice:** Amazon RDS or Amazon Aurora.

### Scenario B: High-Scale Key-Value Access

A shopping application needs low-latency access to shopping-cart records.

**Likely choice:** Amazon DynamoDB, if its data model and access patterns fit.

### Scenario C: Large-Scale Analytical Reporting

An enterprise needs analytical queries over large datasets.

**Likely choice:** Amazon Redshift.

### Scenario D: Reduce Repeated Database Queries

An application repeatedly requests the same data.

**Possible choice:** Amazon ElastiCache.

### Scenario E: Model Complex Relationships

A workload requires graph-oriented queries.

**Possible choice:** Amazon Neptune.

## 11. Database Availability, Backups, and Security

### Backups

Backups help restore data following accidental deletion, corruption, or other incidents.

Customers should verify retention policies, recovery options, and restoration procedures.

### Encryption

AWS database services support various encryption capabilities. Appropriate encryption configuration and key management are important for protecting data.

### Access Control

Use appropriate identity permissions, database authentication, network controls, and least-privilege access.

### Monitoring

Monitor database performance, resource utilization, connections, and relevant application metrics.

### Disaster Recovery

Select backup, replication, and recovery approaches based on the required RTO and RPO.

A highly available database is not automatically protected from accidental deletion or every form of data corruption.

## 12. Exam-Focused Revision Notes

* Amazon RDS is a managed relational database service.
* Amazon Aurora is a relational database compatible with supported MySQL and PostgreSQL versions.
* RDS Multi-AZ supports availability and failover.
* Read replicas primarily support read scaling.
* Amazon DynamoDB is a managed NoSQL key-value and document database.
* Amazon Redshift is designed for analytical data warehousing.
* Amazon ElastiCache supports in-memory caching.
* Amazon DocumentDB supports document database workloads.
* Amazon Neptune is a graph database service.
* OLTP focuses on operational transactions.
* OLAP focuses on analytical processing.
* Managed databases reduce infrastructure management but do not remove all customer responsibilities.
* Backup, availability, encryption, and access control solve different problems and should be considered together.

## 13. Knowledge Check

**Question 1:** Which AWS service provides a managed relational database?

A. Amazon RDS
B. Amazon CloudFront
C. Amazon Route 53
D. AWS IAM

**Answer:** A — Amazon RDS manages supported relational database engines.

**Question 2:** Which service is a managed NoSQL key-value and document database?

A. Amazon Redshift
B. Amazon DynamoDB
C. Amazon EBS
D. Amazon VPC

**Answer:** B — DynamoDB supports key-value and document data models.

**Question 3:** Which service is designed primarily for cloud data warehousing and analytical queries?

A. Amazon Redshift
B. Amazon EC2 Auto Scaling
C. Amazon Route 53
D. Amazon EFS

**Answer:** A — Redshift supports analytical data warehousing.

**Question 4:** What is the main purpose of an RDS read replica?

A. To replace IAM
B. To support read scaling
C. To provide object storage
D. To distribute DNS records

**Answer:** B — Read replicas can offload read traffic from the primary database.

**Question 5:** Which service is most directly associated with managed in-memory caching?

A. Amazon ElastiCache
B. Amazon S3 Glacier Deep Archive
C. AWS CloudTrail
D. Amazon EBS

**Answer:** A — ElastiCache provides managed in-memory caching.

**Question 6:** Which statement best describes OLTP?

A. Long-term archival storage
B. Operational transactions such as inserting orders
C. Global content delivery
D. Network address translation

**Answer:** B — OLTP supports operational transactions.

## 14. Practical Exercise

An online retailer has customer accounts, orders, shopping-cart sessions, and historical sales reports.

Select a potential AWS service for each requirement.

### Suggested Solution

* Customer accounts and orders: Amazon RDS or Aurora if relational transactions are required.
* Shopping-cart sessions: DynamoDB or an appropriate caching architecture, depending on consistency and access requirements.
* Historical sales reporting: Amazon Redshift if a dedicated analytical warehouse is justified.
* Frequently requested cached data: Amazon ElastiCache where appropriate.
* Data protection: Configure backups, access controls, encryption, monitoring, and recovery testing.

## 15. Official Learning Resources

* Amazon RDS: https://aws.amazon.com/rds/
* Amazon Aurora: https://aws.amazon.com/rds/aurora/
* Amazon DynamoDB: https://aws.amazon.com/dynamodb/
* Amazon Redshift: https://aws.amazon.com/redshift/
* Amazon ElastiCache: https://aws.amazon.com/elasticache/
* Amazon Neptune: https://aws.amazon.com/neptune/
* AWS Database Services: https://aws.amazon.com/products/databases/

## 16. Module Completion Checklist

* [ ] Distinguish relational and non-relational databases.
* [ ] Explain Amazon RDS and Aurora.
* [ ] Compare Multi-AZ and read replicas.
* [ ] Explain DynamoDB tables, items, and keys.
* [ ] Identify Redshift's analytical use cases.
* [ ] Recognize ElastiCache, DocumentDB, and Neptune.
* [ ] Match database services to common business requirements.
* [ ] Explain database backups, security, and recovery.
