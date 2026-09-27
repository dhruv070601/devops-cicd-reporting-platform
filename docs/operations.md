# Operations
## Daily execution
Run the report from a scheduler or Jenkins job, archive output/metrics.json and publish output/index.html.
## Troubleshooting
- 401/403: verify service-account permissions and token.
- Timeout: verify Jenkins reachability and API load.
- Empty data: verify job visibility and API query fields.
## Governance
Keep report snapshots immutable, record generation time, and restrict access to operational data.
