# Module 05: AWS Storage Services

## 1. Learning Objectives

* Understand the main AWS storage services.
* Compare object, block, and file storage.
* Explain Amazon S3, Amazon EBS, and Amazon EFS.
* Understand S3 storage classes and lifecycle management.
* Identify AWS Backup and Amazon S3 Glacier use cases.
* Select suitable storage solutions based on cost, performance, durability, and access requirements.

## 2. Overview of AWS Storage

AWS provides storage services for different types of data and workloads.

The three fundamental storage types are:

* **Object storage:** Stores data as objects with associated metadata.
* **Block storage:** Stores data in addressable blocks, commonly used for disks and databases.
* **File storage:** Stores data in files and directories organized in a hierarchy.

Choosing the correct storage service depends on access patterns, performance, availability, durability, and cost.

## 3. Amazon S3: Object Storage

Amazon Simple Storage Service (Amazon S3) is an object storage service designed to store and retrieve data at scale.

### Key Concepts

**Bucket:** A container for objects.

**Object:** The stored data, its key, and associated metadata.

**Object key:** The name used to identify an object within a bucket.

**Versioning:** Keeps multiple versions of objects, helping recover from accidental overwrites or deletions.

**Lifecycle policies:** Automatically transition or expire objects according to defined rules.

**Access control:** Policies and other supported controls determine who can access stored data.

### Common Use Cases

* Images and videos.
* Backups and archives.
* Data lakes and analytics datasets.
* Static website assets.
* Application files and logs.

### Example

An online store stores product images in an S3 bucket. Its application retrieves the images when customers view products.

### Important Characteristics

* Designed for high durability.
* Scales to large amounts of unstructured data.
* Supports multiple storage classes.
* Integrates with many AWS services.
* Supports encryption and access control.

S3 is object storage, not a traditional block device that an operating system mounts as a disk.

## 4. Amazon S3 Storage Classes

Different S3 storage classes are designed for different access patterns and cost requirements.

| Storage Class                 | Typical Use Case                                                     |
| ----------------------------- | -------------------------------------------------------------------- |
| S3 Standard                   | Frequently accessed data                                             |
| S3 Intelligent-Tiering        | Data with changing or uncertain access patterns                      |
| S3 Standard-IA                | Infrequently accessed data that needs rapid access                   |
| S3 One Zone-IA                | Infrequently accessed data stored in one Availability Zone           |
| S3 Glacier Instant Retrieval  | Archive data requiring millisecond retrieval                         |
| S3 Glacier Flexible Retrieval | Archive data where retrieval may take minutes to hours               |
| S3 Glacier Deep Archive       | Long-term archives with infrequent access and longer retrieval times |

Storage class selection should consider storage price, retrieval costs, minimum storage duration, retrieval time, and resilience requirements.

### S3 Standard

Suitable for frequently accessed data, such as application images or active datasets.

### S3 Intelligent-Tiering

Can automatically move eligible objects between access tiers as access patterns change. Monitoring and automation charges may apply.

### S3 Standard-IA

Designed for infrequently accessed data that still requires rapid retrieval. It has retrieval charges and a minimum storage duration.

### S3 One Zone-IA

Stores data in a single Availability Zone. It can cost less than multi-AZ infrequent-access storage but has different resilience characteristics.

Use it only when the data can tolerate the loss of that AZ or can be recreated from another source.

### S3 Glacier Classes

These classes target archival workloads.

* **Instant Retrieval:** Rapid access for rarely accessed archives.
* **Flexible Retrieval:** Suitable when some retrieval delay is acceptable.
* **Deep Archive:** Intended for long-term data retention with infrequent retrieval.

## 5. Amazon S3 Versioning and Lifecycle Management

### Versioning

Versioning preserves multiple versions of objects in a bucket.

It can help recover from accidental overwrites and deletions, although permissions and version-management practices still matter.

### Lifecycle Management

Lifecycle rules automate actions such as:

* Transitioning objects to another storage class.
* Expiring objects after a defined period.
* Managing older object versions.

**Example:** A company stores recent reports in S3 Standard, transitions older reports to an archival class, and expires temporary files after a retention period.

Lifecycle policies should be tested against the organization's data retention and recovery requirements.

## 6. Amazon EBS: Block Storage

Amazon Elastic Block Store (Amazon EBS) provides persistent block storage volumes for use with Amazon EC2.

An EBS volume behaves like a disk that can be attached to a supported EC2 instance.

### Common Use Cases

* Operating-system disks.
* Application storage.
* Database volumes.
* Workloads requiring block-level access.

### Key Concepts

**Volume:** A block storage device provisioned for use with an instance.

**Snapshot:** A point-in-time backup of an EBS volume, stored using AWS-managed snapshot infrastructure.

**Persistence:** EBS data is designed to persist independently of the life of the EC2 instance, subject to the volume's lifecycle and deletion settings.

### EBS vs. Instance Store

Amazon EBS provides persistent block storage.

EC2 instance store provides temporary block storage tied to the host's lifecycle. Its data may be lost when the instance is stopped, terminated, or otherwise affected by the underlying host lifecycle.

Use instance store only when its ephemeral nature matches the workload requirements.

## 7. Amazon EFS: File Storage

Amazon Elastic File System (Amazon EFS) is a managed, elastic file storage service for supported workloads.

It provides shared file-system access through standard file-system interfaces.

### Common Use Cases

* Shared application files.
* Content management systems.
* Web server fleets.
* Linux-based workloads requiring shared storage.
* Applications where multiple compute instances need access to the same files.

### EFS vs. EBS

| Feature         | Amazon EBS                               | Amazon EFS                             |
| --------------- | ---------------------------------------- | -------------------------------------- |
| Storage type    | Block                                    | File                                   |
| Typical use     | Disk for an EC2 instance                 | Shared file system                     |
| Access pattern  | Attached block volume                    | Network file-system access             |
| Scaling         | Depends on volume configuration and type | Elastic file storage                   |
| Common scenario | Database disk                            | Shared files across multiple instances |

The exact attachment and sharing capabilities depend on the service configuration and supported volume type.

## 8. Amazon FSx

Amazon FSx provides managed file systems designed for particular file-system technologies and workloads.

Examples include:

* Amazon FSx for Windows File Server.
* Amazon FSx for Lustre.
* Amazon FSx for NetApp ONTAP.
* Amazon FSx for OpenZFS.

Use FSx when an application requires particular file-system features, performance characteristics, or compatibility.

For example, FSx for Windows File Server supports Windows-oriented file workloads, while FSx for Lustre is designed for high-performance workloads.

## 9. AWS Backup

AWS Backup is a managed service for centrally configuring and managing backups across supported AWS services.

Key capabilities include:

* Backup plans.
* Backup schedules.
* Retention policies.
* Centralized backup management.
* Backup monitoring and recovery workflows.

**Example:** An organization creates a backup plan for supported databases and storage resources, specifying how frequently backups run and how long they are retained.

Backup policies should align with recovery time objectives, recovery point objectives, compliance requirements, and data retention rules.

## 10. Storage Selection Scenarios

### Scenario A: Product Images

A website needs to store and retrieve images at scale.

**Likely choice:** Amazon S3.

### Scenario B: EC2 Operating-System Disk

An EC2 instance needs a persistent boot volume.

**Likely choice:** Amazon EBS.

### Scenario C: Shared Application Files

Multiple supported compute instances need access to the same file system.

**Likely choice:** Amazon EFS.

### Scenario D: Long-Term Archives

A company needs to retain historical records that are rarely accessed.

**Likely choice:** An appropriate S3 Glacier storage class.

### Scenario E: Centralized Backup Management

An organization needs to manage backup policies across supported AWS services.

**Likely choice:** AWS Backup.

### Scenario F: Windows-Compatible Shared Storage

An application requires a managed Windows file server.

**Likely choice:** Amazon FSx for Windows File Server.

## 11. Exam-Focused Revision Notes

* Amazon S3 is object storage.
* Amazon EBS provides block storage for EC2 workloads.
* Amazon EFS provides managed file storage.
* Amazon FSx offers managed file systems for specialized workloads.
* S3 Standard suits frequently accessed data.
* S3 Intelligent-Tiering is useful when access patterns change or are uncertain.
* S3 Standard-IA suits infrequently accessed data that needs rapid retrieval.
* S3 One Zone-IA stores data in one Availability Zone.
* S3 Glacier classes are designed for different archival access requirements.
* S3 Versioning can help recover earlier object versions.
* S3 Lifecycle policies automate transitions and expiration.
* EBS snapshots support point-in-time volume backup and recovery.
* Instance store is ephemeral.
* AWS Backup centrally manages backup policies for supported services.
* Storage choices must account for retrieval costs, performance, durability, availability, and retention requirements.

## 12. Knowledge Check

**Question 1:** Which AWS service is designed for object storage?

A. Amazon EBS
B. Amazon S3
C. Amazon EFS
D. Amazon EC2

**Answer:** B — Amazon S3 provides object storage.

**Question 2:** Which service provides persistent block storage for EC2 instances?

A. Amazon EBS
B. Amazon CloudFront
C. Amazon Route 53
D. AWS IAM

**Answer:** A — Amazon EBS provides block storage volumes.

**Question 3:** Which service is appropriate when multiple supported compute instances need shared file storage?

A. Amazon EFS
B. Amazon EBS only
C. AWS CloudTrail
D. AWS Budgets

**Answer:** A — Amazon EFS provides managed shared file storage.

**Question 4:** Which S3 storage class is intended for long-term archival data with infrequent access and longer retrieval times?

A. S3 Standard
B. S3 Glacier Deep Archive
C. S3 Intelligent-Tiering only
D. S3 Standard-IA only

**Answer:** B — S3 Glacier Deep Archive is designed for long-term archival workloads.

**Question 5:** What is the purpose of S3 Versioning?

A. To increase an EC2 instance's CPU capacity
B. To preserve multiple versions of objects
C. To create VPC subnets
D. To manage DNS records

**Answer:** B — Versioning preserves object versions and can help with recovery.

**Question 6:** Which service provides centralized backup management for supported AWS resources?

A. AWS Backup
B. Amazon Route 53
C. AWS Lambda only
D. Amazon CloudFront

**Answer:** A — AWS Backup centralizes backup management.

## 13. Practical Exercise

A business needs to store product images, database files on EC2, shared application files, and five-year historical archives.

Choose a suitable AWS storage approach for each requirement.

### Suggested Solution

* Product images: Amazon S3.
* Database files on EC2: Amazon EBS, if the database architecture and storage requirements are suitable.
* Shared application files: Amazon EFS or an appropriate Amazon FSx file system, depending on requirements.
* Historical archives: An appropriate S3 Glacier storage class based on retrieval needs and retention requirements.
* Backups: AWS Backup or service-specific backup capabilities, depending on the resource and recovery requirements.

## 14. Official Learning Resources

* Amazon S3: https://aws.amazon.com/s3/
* Amazon EBS: https://aws.amazon.com/ebs/
* Amazon EFS: https://aws.amazon.com/efs/
* Amazon FSx: https://aws.amazon.com/fsx/
* AWS Backup: https://aws.amazon.com/backup/
* S3 Storage Classes: https://aws.amazon.com/s3/storage-classes/

## 15. Module Completion Checklist

* [ ] Compare object, block, and file storage.
* [ ] Explain S3 buckets, objects, versioning, and lifecycle rules.
* [ ] Identify the main S3 storage classes.
* [ ] Compare EBS and EFS.
* [ ] Explain the purpose of Amazon FSx.
* [ ] Understand EBS snapshots and instance store.
* [ ] Explain AWS Backup.
* [ ] Choose storage services for common exam scenarios.
