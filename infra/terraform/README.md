# Terraform

- `modules/network`: VPC, subnets, NAT, routes (Week 5)
- `modules/compute`: ALB, ASG, Route 53, ACM, IAM (Week 6)
- `envs/dev`, `envs/prod`: root modules with separate remote state keys (Week 6)

State lives in S3 with locking. Never commit `*.tfstate`.
