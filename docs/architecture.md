# Architecture
## Data flow
Jenkins exposes job/build metadata through its REST API. A Python collector retrieves only the fields required for reporting. The metrics engine normalizes results and calculates delivery indicators. A JSON snapshot provides machine-readable output while the HTML renderer produces a management report.
## Security
Use a dedicated read-only Jenkins service account and token. Store secrets in Jenkins Credentials, an OS secret store or CI secret manager. Never commit tokens.
## Extensions
Add build-history API pagination, Prometheus export, trend charts, CSV export, email delivery and scheduled execution.
