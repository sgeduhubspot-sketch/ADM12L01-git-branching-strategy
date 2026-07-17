# Module 12 Lab 1 - Git Branching Strategy Setup Evidence

## Lab Name

Git Branching Strategy Setup

## Lab Objective

Configure a Git-based branching workflow for data engineering artifacts using GitHub, Azure Data Factory Git integration, branch protection, required PR reviews, linked issue tracking, and feature flags.

## Repository

Repository: ADM12L01-git-branching-strategy  
Owner: sgeduhubspot-sketch  

## Branching Model

| Branch | Purpose |
|---|---|
| main | Stable production-ready branch |
| develop | Collaboration and integration branch |
| feature/adf-feature-flag | Feature branch for ADF feature flag change |
| feature/databricks-validation | Feature branch for Databricks notebook validation logic |
| release/adm12l01-demo | Release preparation branch |
| hotfix/config-correction | Emergency correction branch |

## Branch Protection

Branch rulesets were configured for main and develop.

| Branch | Protection Applied |
|---|---|
| main | Pull request required, one approval required, stale approvals dismissed, force push blocked, deletion blocked |
| develop | Pull request required, one approval required, stale approvals dismissed, force push blocked |

## Linked Issue Tracking

Issue ADM12L01-001 was created to track the feature flag requirement.

## Pull Request Evidence

A pull request was created from feature/adf-feature-flag into develop.

The PR referenced the linked issue using Refs #1.

The merge was blocked because at least one approving reviewer was required. This confirms that branch protection and reviewer enforcement worked correctly.

## Feature Flag Pattern

A feature flag configuration file was created at:

config/feature_flags.json

The enableStrictValidation flag was changed from false to true in the feature branch.

This demonstrates how pipeline behavior can be toggled through configuration without creating separate long-lived branches.

## ADF Git Integration

Azure Data Factory was connected to the GitHub repository.

| Setting | Value |
|---|---|
| Repository type | GitHub |
| GitHub account | sgeduhubspot-sketch |
| Repository | ADM12L01-git-branching-strategy |
| Collaboration branch | develop |
| Publish branch | adf_publish |
| Root folder | /adf |

## ADF Pipeline Validation

The pipeline PL_ADM12L01_Customer_Ingestion appeared in ADF Studio under the develop branch.

An initial JSON validation issue was fixed by replacing the pipeline artifact with an ADF-compatible JSON definition.

Validate all was executed successfully in ADF Studio.

## Databricks Integration Status

Azure Databricks workspace creation was attempted but blocked by Azure Policy.

The policy denied the resource type:

Microsoft.Databricks/workspaces

Therefore, Databricks Git folder integration could not be completed in this environment.

## Final Result

The lab successfully demonstrated Git branching, GitHub repository integration, branch protection, required reviewer enforcement, linked issue tracking, feature flag usage, and Azure Data Factory Git integration.

The Databricks Repo integration portion was documented as blocked due to Azure Policy.
