# Git Branching Strategy

## Branches

| Branch | Purpose |
|---|---|
| main | Stable production-ready branch |
| develop | Integration branch for validated work |
| feature/adf-feature-flag | Feature branch for ADF feature flag changes |
| feature/databricks-validation | Feature branch for Databricks notebook validation logic |
| release/adm12l01-demo | Release preparation branch |
| hotfix/config-correction | Emergency correction branch |

## Strategy

Developers create feature branches from develop.

Changes are reviewed through pull requests before merging into develop.

Release branches are created from develop when features are ready for controlled release.

Hotfix branches are created from main when urgent production fixes are required.

Feature flags are used to toggle behavior without creating separate long-lived branches.
