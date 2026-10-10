# Module 11: AWS Cloud Deployment and Operations

## 1. Learning Objectives

* Understand common AWS deployment approaches.
* Explain infrastructure as code.
* Identify AWS CloudFormation and AWS Elastic Beanstalk.
* Understand deployment automation and CI/CD fundamentals.
* Recognize blue/green, rolling, and canary deployment strategies.
* Understand operational readiness, change management, and rollback planning.
* Identify common AWS developer and deployment services.

## 2. What Is Cloud Deployment?

Cloud deployment is the process of provisioning cloud resources and releasing applications into an environment.

Deployment may include:

* Creating infrastructure.
* Configuring networks and permissions.
* Deploying application code.
* Applying configuration changes.
* Running tests.
* Monitoring application health.
* Reverting changes if a release fails.

Reliable deployment processes reduce manual errors and help teams deliver changes consistently.

## 3. Infrastructure as Code (IaC)

Infrastructure as Code means defining infrastructure using machine-readable files rather than relying entirely on manual configuration.

IaC can describe resources such as networks, compute instances, databases, permissions, and monitoring configurations.

### Benefits

* Repeatable environments.
* Version-controlled infrastructure changes.
* Easier review and collaboration.
* Reduced configuration drift.
* More consistent deployment processes.

### AWS CloudFormation

AWS CloudFormation provisions and manages supported AWS resources using templates.

Templates describe the intended resources and their configuration.

### Example

A CloudFormation template defines a VPC, subnets, security groups, and application resources. The team can use the template to create a repeatable environment.

Infrastructure as code does not automatically guarantee secure infrastructure. Templates must still be reviewed and tested.

## 4. AWS Elastic Beanstalk

AWS Elastic Beanstalk simplifies deploying and managing supported applications.

It provisions and coordinates underlying resources according to the selected environment and configuration.

### Common Use Cases

* Deploying web applications.
* Managing application environments.
* Integrating deployment with supported compute and load-balancing resources.
* Simplifying routine application operations.

### Example

A developer deploys a supported web application to Elastic Beanstalk instead of manually creating and configuring each underlying resource.

Elastic Beanstalk reduces infrastructure-management effort but does not remove responsibility for application code, access permissions, or appropriate configuration.

## 5. CI/CD Fundamentals

CI/CD refers to practices that automate building, testing, and delivering software changes.

### Continuous Integration (CI)

Developers integrate code changes frequently, and automated workflows build and test those changes.

### Continuous Delivery

Changes are automatically prepared for release, while production deployment may require approval.

### Continuous Deployment

Changes that pass the required automated checks are released to production automatically, according to the pipeline configuration.

### Typical Pipeline

1. Developer commits code.
2. Automated workflow checks out the source.
3. The application is built.
4. Tests and quality checks run.
5. A deployable artifact is produced.
6. The application is deployed to a target environment.
7. Monitoring validates application health.

## 6. AWS Developer and Deployment Services

### AWS CodeBuild

Builds source code, runs tests, and produces build artifacts through configured build projects.

### AWS CodePipeline

Coordinates supported stages in a release pipeline, integrating source, build, test, and deployment activities.

### AWS CodeDeploy

Automates application deployments to supported compute targets and environments.

### AWS CodeCommit

Historically provided managed Git repositories, but it is no longer available to new customers. Do not assume it is an available option for a new AWS account.

Teams can use supported external source-control providers or other appropriate source repositories.

Service availability and recommended developer-tool combinations can change, so consult current AWS documentation.

## 7. Deployment Strategies

### All-at-Once Deployment

Replaces the application version across the target environment in one deployment operation.

**Advantage:** Simple and potentially fast.

**Risk:** Can cause significant disruption if the new version fails.

### Rolling Deployment

Updates a subset of instances at a time until the entire environment runs the new version.

**Advantage:** Can reduce the need to replace everything simultaneously.

**Risk:** Different application versions may run concurrently during deployment.

### Blue/Green Deployment

Maintains two environments:

* Blue: Current production environment.
* Green: New version.

Traffic switches to the new environment after validation.

**Advantage:** Supports testing before switching traffic and can simplify rollback.

**Risk:** Maintaining two environments can increase cost, and data/schema compatibility must be considered.

### Canary Deployment

Releases a new version to a small portion of users or traffic first.

The team evaluates performance and errors before expanding the rollout.

**Advantage:** Limits initial exposure to a potentially faulty release.

**Risk:** Requires suitable traffic control, monitoring, and rollout management.

## 8. Testing and Rollback

A deployment should include appropriate tests and recovery procedures.

Common testing stages include:

* Unit tests.
* Integration tests.
* Security checks.
* Performance tests.
* User acceptance tests.
* Post-deployment health checks.

A rollback plan specifies how to restore a previous working version or recover from a failed change.

Not every change can be reversed by simply redeploying old code. Database migrations and data changes may require forward fixes or a dedicated recovery plan.

## 9. AWS Systems Manager for Operations

AWS Systems Manager provides capabilities that support managing and operating AWS and hybrid resources.

Depending on the feature and resource, it can support:

* Running operational commands.
* Automating maintenance.
* Managing parameters.
* Patch workflows.
* Inventory collection.
* Executing predefined runbooks.

Use controlled permissions and change-management procedures when automating production operations.

## 10. Deployment and Operational Best Practices

* Keep infrastructure definitions in version control.
* Test changes in non-production environments.
* Apply least-privilege deployment permissions.
* Automate repeatable steps.
* Use health checks and monitoring.
* Keep secrets out of source code.
* Plan for rollback and recovery.
* Review changes before production release.
* Track deployment outcomes and incidents.
* Maintain clear operational documentation.

## 11. Exam-Focused Revision Notes

* CloudFormation provides infrastructure as code for AWS resources.
* Elastic Beanstalk simplifies supported application deployment.
* CodeBuild builds and tests code.
* CodePipeline orchestrates release pipeline stages.
* CodeDeploy automates supported application deployments.
* CI involves integrating and testing changes.
* Continuous delivery prepares releases for deployment.
* Continuous deployment automatically releases qualifying changes according to pipeline rules.
* Blue/green uses two environments and switches traffic.
* Rolling deployment updates resources in stages.
* Canary deployment starts with a small portion of traffic or users.
* Rollback plans reduce the impact of failed deployments.
* Infrastructure automation improves repeatability but still requires security review.
* CodeCommit is no longer available to new AWS customers.

## 12. Knowledge Check

**Question 1:** Which AWS service provisions resources using infrastructure-as-code templates?

A. AWS CloudFormation
B. Amazon CloudFront
C. Amazon Route 53
D. Amazon EBS

**Answer:** A — CloudFormation uses templates to provision AWS resources.

**Question 2:** Which deployment strategy uses separate current and new environments before switching traffic?

A. Blue/green deployment
B. All-at-once deployment only
C. Manual patching
D. DNS registration

**Answer:** A — Blue/green deployment maintains separate environments for the current and new versions.

**Question 3:** Which AWS service is designed to build code and run configured build tests?

A. AWS CodeBuild
B. AWS CloudTrail
C. Amazon EFS
D. AWS Config

**Answer:** A — CodeBuild performs configured build and test operations.

**Question 4:** Which deployment strategy initially releases a new version to a small percentage of traffic?

A. Canary deployment
B. Full replacement without testing
C. Database snapshotting
D. Infrastructure discovery

**Answer:** A — Canary deployment limits initial exposure.

**Question 5:** What is the main purpose of a rollback plan?

A. To disable monitoring
B. To provide a recovery path when a deployment fails
C. To make all resources public
D. To remove access control

**Answer:** B — Rollback planning supports recovery from unsuccessful releases.

**Question 6:** Which service can coordinate supported stages of a CI/CD pipeline?

A. AWS CodePipeline
B. Amazon S3 Glacier Deep Archive
C. Amazon VPC
D. AWS KMS

**Answer:** A — CodePipeline orchestrates release pipeline stages.

## 13. Practical Exercise

A company deploys its web application manually and has experienced production failures after releases.

Recommend improvements to its deployment process.

### Suggested Solution

* Define infrastructure using CloudFormation or another appropriate IaC approach.
* Store application code and infrastructure definitions in version control.
* Automate builds and tests using suitable CI/CD tools.
* Deploy first to a test environment.
* Consider a rolling, blue/green, or canary deployment strategy.
* Use monitoring and health checks to validate releases.
* Maintain rollback and database recovery plans.
* Restrict deployment permissions and protect secrets.

## 14. Official Learning Resources

* AWS CloudFormation: https://aws.amazon.com/cloudformation/
* AWS Elastic Beanstalk: https://aws.amazon.com/elasticbeanstalk/
* AWS CodeBuild: https://aws.amazon.com/codebuild/
* AWS CodePipeline: https://aws.amazon.com/codepipeline/
* AWS CodeDeploy: https://aws.amazon.com/codedeploy/
* AWS Systems Manager: https://aws.amazon.com/systems-manager/
* AWS Developer Tools: https://aws.amazon.com/developer/tools/

## 15. Module Completion Checklist

* [ ] Explain infrastructure as code.
* [ ] Identify CloudFormation and Elastic Beanstalk use cases.
* [ ] Explain CI, continuous delivery, and continuous deployment.
* [ ] Distinguish CodeBuild, CodePipeline, and CodeDeploy.
* [ ] Compare all-at-once, rolling, blue/green, and canary deployment strategies.
* [ ] Explain testing and rollback planning.
* [ ] Identify relevant Systems Manager operational capabilities.
* [ ] Complete the knowledge check without consulting the answers.
