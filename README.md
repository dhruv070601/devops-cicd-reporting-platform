# DevOps CI/CD Reporting Platform
A Python reporting platform that turns Jenkins API data into operational metrics and management-ready HTML reports.
## Flow
Jenkins API -> Python Collector -> Metrics Engine -> JSON Snapshot -> HTML Dashboard
## Metrics
- Pipeline runs, success/failure rate and duration
- Deployment frequency and environment distribution
- Top failing jobs and recent failures
- Trend summaries and SLA-style health indicators
- Report timestamp and data freshness
## Run
Set JENKINS_URL, JENKINS_USER and JENKINS_TOKEN in the environment. Run python src/report.py.
For offline demonstration, run python src/report.py --sample.
