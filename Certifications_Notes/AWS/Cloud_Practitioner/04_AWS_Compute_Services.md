# Module 04: AWS Compute Services

## 1. Learning Objectives

* Understand the purpose of AWS compute services.
* Explain Amazon EC2 and common instance concepts.
* Compare virtual machines, containers, and serverless computing.
* Understand EC2 Auto Scaling and Elastic Load Balancing.
* Identify AWS Lambda, Amazon ECS, Amazon EKS, and AWS Fargate.
* Understand basic compute pricing options and common use cases.

## 2. What Is Cloud Computing Infrastructure?

Compute resources execute application code, process data, and run operating systems and software.

AWS provides several compute approaches, allowing organizations to select the appropriate balance of control, flexibility, operational responsibility, and cost.

Common compute services include:

* Amazon EC2.
* AWS Lambda.
* Amazon ECS.
* Amazon EKS.
* AWS Fargate.
* AWS Elastic Beanstalk.
* Amazon Lightsail.

## 3. Amazon EC2

Amazon Elastic Compute Cloud (Amazon EC2) provides resizable computing capacity through virtual server instances.

Customers can choose operating systems, instance types, storage options, networking configurations, and security settings.

### Common EC2 Use Cases

* Hosting websites and applications.
* Running data-processing workloads.
* Hosting development and testing environments.
* Running enterprise applications.
* Supporting workloads that require operating-system access.

### Key EC2 Concepts

**Instance:** A virtual server running in AWS.

**Amazon Machine Image (AMI):** A template used to launch EC2 instances, containing information needed to configure the operating system and software environment.

**Instance type:** Determines the general hardware characteristics and resource capacity, including CPU, memory, storage, and networking capabilities.

**Key pair:** Credentials used for supported secure instance access methods, such as SSH for Linux.

**Security group:** A virtual firewall controlling permitted inbound and outbound traffic for associated resources.

**Amazon EBS:** Persistent block storage commonly used with EC2 instances.

**Elastic IP address:** A static public IPv4 address designed for use with supported AWS resources.

## 4. EC2 Instance Families

Different instance families are optimized for different workload characteristics.

| Family                | General Purpose                          | Example Workload                                |
| --------------------- | ---------------------------------------- | ----------------------------------------------- |
| General purpose       | Balanced compute, memory, and networking | Web servers and development                     |
| Compute optimized     | High compute capacity relative to memory | Batch processing and CPU-intensive applications |
| Memory optimized      | Large memory capacity                    | In-memory databases and analytics               |
| Storage optimized     | High storage throughput or I/O           | Storage-intensive workloads                     |
| Accelerated computing | Specialized accelerators such as GPUs    | Machine learning and graphics processing        |

Exact capabilities depend on the instance family and generation.

## 5. EC2 Scaling and Load Balancing

### EC2 Auto Scaling

Amazon EC2 Auto Scaling adjusts the number of EC2 instances according to configured policies and conditions.

It can help:

* Add instances when demand increases.
* Remove instances when demand decreases.
* Replace unhealthy instances.
* Maintain a configured minimum or desired capacity.

Auto Scaling does not automatically make an entire application highly available. Other components and dependencies must also be designed for resilience.

### Elastic Load Balancing (ELB)

Elastic Load Balancing distributes incoming traffic across registered targets, such as EC2 instances.

Benefits include:

* Distributing traffic.
* Supporting health checks.
* Improving application availability when combined with resilient architecture.
* Integrating with Auto Scaling.

**Example:** A load balancer sends requests to healthy web servers across two AZs. Auto Scaling adds more instances when traffic increases.

## 6. AWS Lambda: Serverless Computing

AWS Lambda runs supported code in response to events without requiring customers to provision or manage servers directly.

Customers configure functions, permissions, triggers, and other settings. AWS manages the underlying execution infrastructure.

### Common Use Cases

* Processing uploaded files.
* Responding to API requests.
* Automating scheduled or event-driven tasks.
* Processing messages from supported services.
* Performing lightweight data transformations.

### Example

A user uploads an image to an Amazon S3 bucket. An event can trigger a Lambda function to process the image and save the result.

### Benefits

* No need to manage server instances directly.
* Automatic scaling within service limits and configuration.
* Usage-based billing according to the applicable pricing model.
* Integration with many AWS services.

### Important Considerations

* Execution duration and resource limits apply.
* Functions may experience cold starts.
* Permissions must be configured correctly.
* Lambda is not automatically the best choice for every continuously running or long-duration workload.

## 7. Containers: Amazon ECS, Amazon EKS, and AWS Fargate

Containers package application code and its dependencies into a consistent deployment unit.

They are often useful for microservices, portable application deployments, and workloads that benefit from consistent runtime environments.

### Amazon ECS

Amazon Elastic Container Service (Amazon ECS) is a managed container orchestration service that runs and manages containerized applications.

### Amazon EKS

Amazon Elastic Kubernetes Service (Amazon EKS) is a managed Kubernetes service for running Kubernetes-based applications.

### AWS Fargate

AWS Fargate is a serverless compute engine for containers that works with supported Amazon ECS and Amazon EKS configurations.

It reduces the need to manage the underlying server infrastructure for supported container workloads.

### Comparison

| Service     | Main Purpose                                                     |
| ----------- | ---------------------------------------------------------------- |
| Amazon ECS  | Orchestrating containerized applications                         |
| Amazon EKS  | Running Kubernetes-based applications                            |
| AWS Fargate | Running supported containers without managing underlying servers |
| AWS Lambda  | Running event-driven functions without managing servers directly |

Fargate and Lambda are both serverless compute options, but they are designed for different execution models.

## 8. AWS Elastic Beanstalk

AWS Elastic Beanstalk helps deploy and manage applications while AWS provisions and coordinates supported underlying resources.

Developers upload application code, select supported configuration options, and use Elastic Beanstalk to manage application environments.

It can handle activities such as environment provisioning, application deployment, health monitoring, and scaling configuration.

**Best suited for:** Developers who want a managed application deployment experience without manually configuring every underlying resource.

Elastic Beanstalk does not eliminate all infrastructure responsibility. Customers still manage application code, configurations, permissions, and relevant environment settings.

## 9. Amazon Lightsail

Amazon Lightsail offers simplified cloud resources with predictable pricing bundles for common workloads.

It can be useful for:

* Small websites.
* Simple development environments.
* Personal projects.
* Basic applications.
* Users who prefer a simplified interface and setup process.

For more complex enterprise architectures, customers may prefer the broader configuration options available across individual AWS services.

## 10. Virtual Machines vs. Containers vs. Serverless

| Characteristic            | Virtual Machines                 | Containers                                   | Serverless Functions                            |
| ------------------------- | -------------------------------- | -------------------------------------------- | ----------------------------------------------- |
| Example                   | Amazon EC2                       | Amazon ECS                                   | AWS Lambda                                      |
| Operating-system control  | Relatively high                  | Depends on platform and configuration        | No direct underlying server management          |
| Deployment unit           | Virtual machine                  | Container image                              | Function code and configuration                 |
| Infrastructure management | Customer manages more            | Depends on orchestration and compute choice  | AWS manages underlying execution infrastructure |
| Typical use               | General-purpose server workloads | Containerized applications and microservices | Event-driven tasks                              |

Containers can run on EC2 or on serverless container infrastructure such as Fargate. The categories are related but not mutually exclusive.

## 11. EC2 Pricing Options

AWS offers different purchasing options for compute workloads. Specific terms and eligibility depend on the service and region.

### On-Demand

Pay for compute capacity without a long-term commitment.

Useful for unpredictable demand, experimentation, and workloads that need flexibility.

### Savings Plans

Offer discounted rates in exchange for a commitment to a specified amount of eligible usage over a defined term.

Useful when an organization has a reasonably predictable level of eligible compute spending.

### Reserved Instances

Provide billing benefits for eligible services and configurations in exchange for a commitment. They are particularly associated with Amazon EC2 and other eligible services.

The precise flexibility and billing benefits depend on the reservation type and service.

### Spot Instances

Use spare EC2 capacity at discounted rates, with the possibility of interruption when AWS needs the capacity back.

Useful for fault-tolerant workloads such as flexible batch jobs.

Not suitable for workloads that cannot tolerate interruptions unless the architecture includes appropriate recovery mechanisms.

## 12. Choosing a Compute Service

### Scenario A: Full Operating-System Control

A company needs a custom operating system configuration and administrative access.

**Likely choice:** Amazon EC2.

### Scenario B: Event-Driven File Processing

A function should execute when a file is uploaded to Amazon S3.

**Likely choice:** AWS Lambda.

### Scenario C: Containerized Application

A company wants to orchestrate containerized microservices.

**Likely choice:** Amazon ECS or Amazon EKS, depending on its requirements.

### Scenario D: Containers Without Managing Servers

A team wants to run supported containers without managing the underlying compute servers.

**Likely choice:** AWS Fargate.

### Scenario E: Simplified Application Deployment

A developer wants help deploying and managing a supported application environment.

**Likely choice:** AWS Elastic Beanstalk.

### Scenario F: Small Website with Simplified Setup

A small business wants a straightforward hosting experience.

**Possible choice:** Amazon Lightsail.

## 13. Exam-Focused Revision Notes

* Amazon EC2 provides virtual servers.
* An AMI is used as a template to launch EC2 instances.
* Instance types determine available resource characteristics.
* Amazon EBS provides block storage.
* EC2 Auto Scaling adjusts instance capacity according to configured policies.
* Elastic Load Balancing distributes incoming traffic across registered targets.
* AWS Lambda runs event-driven code without requiring customers to manage the underlying servers.
* Amazon ECS orchestrates containers.
* Amazon EKS provides managed Kubernetes.
* AWS Fargate runs supported containers without customers managing the underlying servers.
* AWS Elastic Beanstalk simplifies application deployment and environment management.
* Amazon Lightsail simplifies common cloud hosting tasks.
* On-Demand provides flexibility without a long-term commitment.
* Savings Plans offer discounted rates for committed eligible usage.
* Spot Instances use spare capacity and can be interrupted.
* The right compute service depends on workload requirements, operational control, execution model, and cost.

## 14. Knowledge Check

**Question 1:** Which service provides resizable virtual servers?

A. Amazon Route 53
B. Amazon EC2
C. Amazon CloudFront
D. AWS IAM

**Answer:** B — Amazon EC2 provides virtual server instances.

**Question 2:** Which service can run code in response to an Amazon S3 object-upload event without requiring the customer to manage servers?

A. AWS Lambda
B. Amazon EC2 only
C. Amazon EBS
D. AWS Direct Connect

**Answer:** A — AWS Lambda can be triggered by supported S3 events.

**Question 3:** Which service distributes incoming application traffic across registered targets?

A. AWS Budgets
B. Elastic Load Balancing
C. AWS CloudTrail
D. Amazon S3 Glacier

**Answer:** B — Elastic Load Balancing distributes incoming traffic.

**Question 4:** Which service is designed for managing Kubernetes-based applications?

A. Amazon EKS
B. Amazon Lightsail
C. Amazon Route 53
D. AWS Cost Explorer

**Answer:** A — Amazon EKS is a managed Kubernetes service.

**Question 5:** Which EC2 purchasing option uses spare capacity and may be interrupted?

A. On-Demand Instances
B. Spot Instances
C. Savings Plans
D. Dedicated software licenses

**Answer:** B — Spot Instances use spare EC2 capacity and may be interrupted.

**Question 6:** A company wants to run supported containers without managing the underlying compute servers. Which service should it consider?

A. AWS Fargate
B. Amazon Route 53
C. AWS CloudTrail
D. Amazon EBS

**Answer:** A — Fargate provides serverless compute for supported container workloads.

**Question 7:** What is the purpose of an Amazon Machine Image?

A. To distribute DNS records globally
B. To provide a template for launching EC2 instances
C. To analyze cloud billing
D. To manage IAM users

**Answer:** B — An AMI provides the template information used to launch an instance.

## 15. Practical Exercise

A startup is building an online store. It needs a web application, background image processing, and a way to handle traffic spikes.

Propose an appropriate combination of AWS compute services.

### Suggested Solution

* Use Amazon EC2 or an appropriate container platform for the web application, depending on the required control and application architecture.
* Use AWS Lambda for event-driven image processing when the workload fits Lambda's limits.
* Use Elastic Load Balancing to distribute traffic across application targets.
* Use EC2 Auto Scaling if the application runs on EC2 and requires dynamic instance capacity.
* Monitor application performance and spending.
* Apply appropriate IAM permissions and secure application configuration.

## 16. Official Learning Resources

* Amazon EC2: https://aws.amazon.com/ec2/
* AWS Lambda: https://aws.amazon.com/lambda/
* Amazon ECS: https://aws.amazon.com/ecs/
* Amazon EKS: https://aws.amazon.com/eks/
* AWS Fargate: https://aws.amazon.com/fargate/
* AWS Elastic Beanstalk: https://aws.amazon.com/elasticbeanstalk/
* Amazon Lightsail: https://aws.amazon.com/lightsail/
* AWS Compute Pricing: https://aws.amazon.com/pricing/

## 17. Module Completion Checklist

* [ ] Explain Amazon EC2 and AMIs.
* [ ] Identify common EC2 instance families.
* [ ] Explain Auto Scaling and Elastic Load Balancing.
* [ ] Distinguish Lambda, ECS, EKS, and Fargate.
* [ ] Explain Elastic Beanstalk and Lightsail.
* [ ] Compare On-Demand, Savings Plans, Reserved Instances, and Spot Instances.
* [ ] Choose an appropriate compute service for a given scenario.
* [ ] Complete the knowledge-check questions without consulting the answers.
