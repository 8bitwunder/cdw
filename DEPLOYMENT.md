# Canberra Data Week deployment setup

This document records the current CDW website deployment setup as of August 2026.

## Current architecture

### Production

- Source repository: `8bitwunder/cdw`
- Production branch: `main`
- Production host: Cloudflare Pages
- Production domain: `canberradataweek.com`
- Cloudflare Pages project: `cdw`
- Production deployments are automatic from `main`.

### Preview deployments

- Preview host: Cloudflare Workers
- Workers application: `cdw`
- Non-production branches are deployed automatically as preview versions.
- Example stable branch preview format: `https://<branch>-cdw.onedatastepatatime.workers.dev`
- Preview deployments should be reviewed before merging a pull request into `main`.

### GitHub Pages

- GitHub Pages is still enabled and may continue to report deployment checks.
- The repository currently contains a `CNAME` file for `canberradataweek.com`.
- Do not change or remove GitHub Pages or the `CNAME` file during active event delivery unless the production hosting path has first been re-verified.

## Standard change workflow

1. Create a feature or fix branch from `main`.
2. Make website changes only on that branch.
3. Open a pull request into `main`.
4. Wait for the Cloudflare preview deployment to complete.
5. Review the preview URL visually on desktop and mobile where relevant.
6. Review the GitHub diff and deployment checks.
7. Merge the pull request only after the preview is approved.
8. Confirm the production deployment succeeds after merge.
9. Delete the merged feature branch when no longer needed. The pull request and merged commit history remain available in GitHub.

## What not to change casually

- Do not delete the Cloudflare Pages `cdw` project. It currently serves `canberradataweek.com`.
- Do not delete the Cloudflare Workers `cdw` application. It provides branch previews.
- Do not change DNS or the production custom domain while the current setup is working.
- Do not manually deploy a preview version to production using Wrangler unless there is a deliberate reason to bypass the normal merge workflow.

## Current known duplication

The repository currently triggers successful checks from more than one hosting system, including Cloudflare Pages, Cloudflare Workers and GitHub Pages. This is acceptable for now, but it creates extra deployment noise and some ambiguity about hosting responsibilities.

## Future tidy-up checklist

When there is a low-risk maintenance window:

1. Confirm Cloudflare Pages is still the service receiving production traffic for `canberradataweek.com`.
2. Confirm Cloudflare Workers is still required for branch previews.
3. Review whether GitHub Pages is serving any production or fallback traffic.
4. If GitHub Pages is confirmed redundant, disable it first without changing Cloudflare Pages.
5. Re-test `canberradataweek.com` after the GitHub Pages change.
6. Only then consider removing the repository `CNAME` file in a separate pull request.
7. Keep the architecture simple: GitHub for source control and approvals, Cloudflare Pages for production, Cloudflare Workers for branch previews.

## Quick reference

- `main` = approved production source
- feature branch = temporary workspace
- Pull Request = review and approval record
- Cloudflare Pages = production
- Cloudflare Workers = branch previews
- GitHub Pages = legacy or redundant deployment path to review later
