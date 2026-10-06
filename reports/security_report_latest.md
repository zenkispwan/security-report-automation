# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**59** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=59。
- Intelligence 候選：**30** 筆；P1 **0**、P2 **0**、P3 **6**、WATCH **24**。
- Baseline：state / generated_at=2026-10-05T06:26:23.594502+00:00 / available=true。
- 目前 compact intelligence 中沒有 P1 項目。

## Daily Delta｜自上一份報告的重要變化

本次共有 **59** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-88395｜未確認 / 未確認
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T16:17:16.957)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T16:17:16.957 / 2026-10-05T19:17:25.860
- **官方描述（原文）**：GouGuOA v6.0.5 and before is vulnerable to SQL Injection in /home/message/rubbish via the keywords parameter.

### 2. CVE-2026-105640｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T19:17:18.383)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T19:17:18.383 / 2026-10-05T19:17:18.520
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, Plane trusts email addresses returned by Gitea OAuth and by self-managed GitLab OAuth deployments where email confirmation is disabled, without verifying that the provider authenticated ownership of the address. An attacker can set an OAuth identity's unverified provider email to a victim's address, which Plane matches directly to the victim's existing local account. The attacker can then log in to the victim's Plane account without knowing the victim's password. GitHub, GitLab.com, and Google are not affected because those providers return verified email addresses. This issue is fixed in 1.4.0.

### 3. CVE-2026-105638｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T19:17:18.030)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.1 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T19:17:18.030 / 2026-10-05T19:17:18.173
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, Plane's magic-code email login uses a six-digit numeric OTP with approximately 20 bits of entropy. The verifier has no per-code failed-attempt counter, and an incorrect code does not increment a counter, invalidate the Redis entry, or lock the email address. The verifier extends django.views.View rather than DRF's APIView, so the configured AnonRateThrottle limit does not apply. The middleware stack also contains no Django-level rate limiter such as django-ratelimit, django-axes, or an IP-throttling middleware. This vulnerability is fixed in 1.4.0.

### 4. CVE-2026-105637｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T19:17:17.860)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T19:17:17.860 / 2026-10-05T20:17:11.203
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, ProjectBulkAssetEndpoint.post in apps/api/plane/app/views/asset/v2.py retrieves assets using id__in=asset_ids and workspace__slug=slug but does not constrain the query with project_id from the URL. A workspace Guest can provide asset UUIDs from another project in the same workspace and reassign their issue_id, comment_id, page_id, draft_issue_id, or project_id to an entity the attacker controls. Plane then treats the attacker's project as the new owner and provides a presigned download URL for the hijacked file. This issue is fixed in 1.4.0.

### 5. CVE-2026-105285｜Totolink / A3002MU
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T10:16:38.520)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.01096 / percentile=0.64399
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T10:16:38.520 / 2026-10-05T13:16:52.460
- **官方描述（原文）**：A security vulnerability has been detected in Totolink A3002MU 1.0.0-B20230403.1455. This affects an unknown function of the file /boafrm/formIpQoS of the component QoS Rule Handler. The manipulation of the argument addQos/comment/entry_name leads to stack-based buffer overflow. Remote exploitation of the attack is possible. The exploit has been disclosed publicly and may be used.

### 6. CVE-2026-105284｜Totolink / A3002MU
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T09:17:12.350)
- **Risk**：P3 / score 38；reasons：POC_AVAILABLE(+10)、CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.00784 / percentile=0.54511
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T09:17:12.350 / 2026-10-05T16:17:12.020
- **官方描述（原文）**：A weakness has been identified in Totolink A3002MU 1.0.0-B20230403.1455. The impacted element is the function sub_40FCFC of the file /bin/boa of the component Authentication Check. Executing a manipulation can lead to improper authorization. The attack may be launched remotely. The exploit has been made available to the public and could be used for attacks.

### 7. CVE-2026-12171｜cookpete / auto-changelog
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T17:17:14.510)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T17:17:14.510 / 2026-10-05T20:17:21.030
- **官方描述（原文）**：auto-changelog before 2.6.1 merges configuration from inside the target repository (the .auto-changelog file and the auto-changelog key in package.json) into its options, and honors security-sensitive options from that untrusted source. The handlebarsSetup option is passed to require(), so running auto-changelog over attacker-controlled repository content (for example, in a CI workflow that checks out an untrusted pull request head, or locally on a forked or third-party repository) executes attacker-chosen code with the privileges of the invoking user or CI job, including access to workflow secrets, without the repository dependencies ever being installed. The plugins option similarly loads attacker-controlled modules from the repository. Under the same conditions, appendGitLog/appendGitTag allow git argument injection (e.g. --output= to write arbitrary files), output allows writing attacker-influenced content to arbitrary paths, and template causes an outbound request to an attacker-chosen URL. Version 2.6.1 treats in-repository configuration as untrusted and refuses to run when it sets these options, unless the new --unsafe-config flag is passed.

### 8. CVE-2026-105773｜Canimaan Software / ClamXAV
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T21:16:36.093)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.3 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T21:16:36.093 / 2026-10-05T21:16:36.093
- **官方描述（原文）**：Canimaan Software ClamXAV versions 3.3 - 3.11 contains a local privilege escalation vulnerability in the Privileged Helper Tool caused by a race condition and insufficient file validation, allowing a local attacker to execute arbitrary code with system privileges. Fixed in 3.11.1.

### 9. CVE-2026-105635｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T19:17:17.503)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.4 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T19:17:17.503 / 2026-10-05T19:17:17.650
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, ProjectJoinEndpoint at GET /api/workspaces/{slug}/projects/{project_id}/join/{pk}/ uses permission_classes = [AllowAny] and returns the full ProjectMemberInvite record, including its email, token, and role, to unauthenticated callers. The corresponding POST endpoint checks only whether the submitted email matches project_invite.email and does not validate the invitation token. An attacker who knows the invitation UUID can discover the invited email, register an account with that email, and accept the invitation without receiving the original invite. This issue is fixed in 1.4.0.

### 10. CVE-2026-105633｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T18:17:36.757)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T18:17:36.757 / 2026-10-05T19:17:17.213
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, the V2 issue-attachment PATCH endpoint accepts issue_id in the URL but omits it from the database query. A project member can use an issue_id they control in the URL while targeting another user's attachment by its pk UUID. Because the server matches only pk, workspace, and project_id, it modifies the attachment regardless of the issue_id in the URL. When the attachment is pending and has not been confirmed as uploaded, the PATCH handler sets created_by = request.user and transfers attachment ownership to the attacker. This issue is fixed in 1.4.0.

### 11. CVE-2026-105632｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T18:17:36.593)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T18:17:36.593 / 2026-10-05T20:17:11.050
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, the GraphQL joinProject mutation lets any workspace member add themselves to any project in that workspace including network=0 (secret/private) projects they were never invited to and grants them a full Member role (read + write). The resolver checks only workspace-level membership/role and never checks the target project's visibility (network). This collapses project-level tenant isolation within a workspace: a low-privilege member can read and modify confidential data in every private project. This issue is fixed in 1.4.0.

### 12. CVE-2026-105630｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T18:17:36.250)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T18:17:36.250 / 2026-10-05T19:17:17.093
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, an authenticated low-privilege workspace member, including a Guest, can upload an image/svg+xml file as a generic or issue attachment. The file retains the attacker-controlled Content-Type, and the asset-download endpoint creates a presigned URL with Content-Disposition: inline. In the default self-hosted MinIO deployment, the asset URL is served from the same origin as the Plane application, allowing embedded SVG JavaScript to execute in the application's security context. A victim, including a workspace administrator, who opens the link can have the session compromised through stored XSS, leading to account takeover. This issue is fixed in 1.4.0.

### 13. CVE-2026-105628｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T18:17:35.917)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.6 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T18:17:35.917 / 2026-10-05T18:17:36.050
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, Plane's OAuth avatar synchronization flow fetches avatar_url from provider user data through a server-side HTTP request without internal IP validation and follows redirects by default. An attacker can provide an avatar URL that redirects to an internal-only resource, such as a metadata endpoint, and Plane uploads the fetched response as a user avatar file. The object is then exposed through /api/assets/v2/static/{asset_id}/, allowing exfiltration of internally fetched content. This issue is fixed in 1.4.0.

### 14. CVE-2026-104979｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T18:17:33.420)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T18:17:33.420 / 2026-10-05T20:17:10.243
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, IntakeIssuePublicViewSet.create in Plane v1.3.1 writes description_html through Issue.objects.create(...) without calling validate_html_content from nh3. Any authenticated user, including a new user with no workspace memberships, can plant arbitrary HTML in a project that has a published DeployBoard with intake enabled. When a project member or viewer of a closed intake item clicks the planted link, the TipTap \tjavascript: parser bypass and the target="_self" click handler execute JavaScript in the viewer's session and exfiltrate a long-lived API token. This issue is fixed in 1.4.0.

### 15. CVE-2026-104977｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T18:17:33.080)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T18:17:33.080 / 2026-10-05T19:17:15.790
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, the fix for CVE-2026-27706 and GHSA-jcc6-f9v6-f7jw, an SSRF in work-item link unfurling shipped in v1.2.2, remains incomplete in the v1.3.1 GA release. Any authenticated project member can make the server fetch attacker-selected internal targets, including cloud metadata at 169.254.169.254, and read the response body returned as the link title or favicon. Complete hardening exists on main in PR 9163 but was not included in an earlier released tag. This issue is fixed in 1.4.0.

### 16. CVE-2026-104975｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T18:17:32.747)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 7.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T18:17:32.747 / 2026-10-05T19:17:15.657
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, Plane's dashboard asset endpoints in plane/app/views/asset/v2.py were remediated for two cross-tenant asset IDORs, CVE-2026-27705 and CVE-2026-46558. Those fixes added a membership check and project_id and workspace__slug scoping to the asset endpoints in that file. The Spaces app in plane/space/views/asset.py serves related public-board operations under /api/public/ but was not remediated. Its EntityAssetEndpoint and AssetRestoreEndpoint resolve a DeployBoard from a public anchor and then read or modify FileAsset rows scoped only to the board's workspace, without a membership check or project_id constraint. An attacker can therefore read, overwrite, or restore assets across projects and workspaces. This issue is fixed in 1.4.0.

### 17. CVE-2026-104974｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T18:17:32.473)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.1 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T18:17:32.473 / 2026-10-05T20:17:10.110
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, a user whose account has been deactivated by setting is_active=False can still log in with existing credentials. Successful authentication silently changes is_active back to True, reactivating the account without notifying the administrator. This issue is fixed in 1.4.0.

### 18. CVE-2026-104971｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T18:17:32.113)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 8.5 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T18:17:32.113 / 2026-10-05T19:17:15.537
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, DuplicateAssetEndpoint fetches a source FileAsset without limiting it to the caller's workspace, allowing cross-workspace asset duplication. WorkspaceFileAssetEndpoint and the legacy FileAssetEndpoint omit workspace authorization, allowing authenticated users to read, create, modify, or delete assets in workspaces where they are not members. Separately, WorkspaceViewViewSet.retrieve lacks the authorization decorator used by its sibling actions, exposing an unauthorized workspace-view read surface. This issue is fixed in 1.4.0.

### 19. CVE-2026-104968｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T17:17:12.627)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 8.7 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T17:17:12.627 / 2026-10-05T20:17:09.970
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, GET /api/workspaces/{slug}/entity-search/?query_type=user_mention returns workspace-member display names, UUIDs, and avatar URLs to any authenticated user who knows the workspace slug, even when the caller is not a workspace member. The endpoint also exposes ProjectMember rows under the same condition. SearchEndpoint in apps/api/plane/app/views/search/base.py inherits BaseAPIView with only permission_classes = [IsAuthenticated] and performs no workspace-membership check. This issue is fixed in 1.4.0.

### 20. CVE-2026-102262｜Newell Brands / DYMO ID
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T21:16:32.400)
- **Risk**：WATCH / score 30；reasons：POC_AVAILABLE(+10)、CVSS_HIGH(+12)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 7.0 (HIGH)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T21:16:32.400 / 2026-10-05T21:16:32.400
- **官方描述（原文）**：Newell Brands DYMO ID 1.5.1.71 resolves its plugin Modules directory relative to the process working directory. An attacker could store a job file alongside malicious modules / DLL that sets the process working directory to the job file's folder when a victim clicks on the file, resulting in code execution at the victim's privilege level. Fixed in 1.6.0.

### 21. CVE-2026-97283｜Liquid Web / StellarWP / Advanced Post Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T19:17:27.133)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T19:17:27.133 / 2026-10-05T19:17:27.133
- **官方描述（原文）**：Deserialization of Untrusted Data vulnerability in Liquid Web / StellarWP Advanced Post Manager advanced-post-manager allows Object Injection.This issue affects Advanced Post Manager: from n/a through 4.5.5.

### 22. CVE-2026-91107｜OS4ED / openSIS-Classic
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T22:16:58.657)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T22:16:58.657 / 2026-10-05T22:16:58.657
- **官方描述（原文）**：openSIS Classic 9.3 allows an authenticated user with the built-in teacher role can select an arbitrary staff record through staff_id and cause the School Information update path to reset that selected account's password.

### 23. CVE-2026-79820｜Hewlett Packard Enterprise (HPE) / HPE Integrated Lights-Out (iLO) 7
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T15:17:22.290)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T15:17:22.290 / 2026-10-05T16:17:16.563
- **官方描述（原文）**：A remote user validation failure vulnerability exists in HPE Integrated Lights-Out (iLO) 7 firmware.

### 24. CVE-2026-77226｜Camunda / Camunda 7
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T21:16:37.337)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.2 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T21:16:37.337 / 2026-10-05T21:16:37.337
- **官方描述（原文）**：Camunda 7.24.0 before 7.24.15 contains an incorrect authorization vulnerability in the Admin web application's first-run setup endpoint, where SetupResource incorrectly determines setup availability by counting only direct members of the camunda-admin group rather than recognizing all configured administrators. An unauthenticated remote attacker can exploit this logic flaw to call the setup user-create endpoint and create a new administrator account when the camunda-admin group is empty but the system is fully administered, resulting in account takeover and potential process deployment or script execution as the engine's service user.

### 25. CVE-2026-21589｜Atlassian / Bamboo Data Center
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T22:16:58.423)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T22:16:58.423 / 2026-10-05T22:16:58.423
- **官方描述（原文）**：h3. Summary This is a vulnerability in Bitbucket Data Center, Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center. Crowd Data Center, Crucible and Fisheye. This Arbitrary File Access vulnerability allows an unauthenticated attacker to access specific files within the web application root directory in affected versions. Exploitation requires prior knowledge of the target file's exact name and path; this vulnerability does not allow attackers to enumerate or list directory contents. In some configurations, there may be some sensitive files that make this highly severe. h3. Context This vulnerability allows an unauthenticated remote attacker to access specific files within the web application root directory in affected versions. h3. Details: * The vulnerability must be addressed for affected versions of: Bitbucket Data Center, introduced in version >= 4.6.0, fix versions: 9.4.26, 10.2.8, 10.5.1 Confluence Data Center, introduced in version >= 5.10.0, fix versions 9.2.26, 10.2.19 Crowd Data Center, introduced in version >= 2.11.0, fix versions 6.3.7, 7.0.3, 7.1.1, 7.2.4 Jira Software Data Center, introduced in version >= 7.1.0, fix versions 9.12.40, 10.3.26, 11.3.12 Jira Service Management Data Center, introduced in version >= 3.1.0, fix versions 5.12.40, 10.3.26, 11.3.12 Bamboo Data Center >= 7.0.1, fix versions 10.2.24, 12.1.12 Crucible, fix versions 4.9.15 Fisheye, fix version 4.9.15 * Exploitation requires prior knowledge of the target file's exact name and path. * The vulnerability does not include the capability to enumerate or list directory contents.

### 26. CVE-2026-105763｜twentyhq / twenty
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-06T00:16:33.247)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.6 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-06T00:16:33.247 / 2026-10-06T00:16:33.380
- **官方描述（原文）**：Twenty is an open-source CRM (customer relationship management) platform. From 1.20.10 until 2.7.0, the /metadata GraphQL connectedAccounts query returned connectionParameters from ConnectedAccountDTO for every connected account in a workspace, including plaintext IMAP, SMTP, and CalDAV passwords, because the field was not hidden and the lookup did not enforce the calling user's identity or account visibility. A normal workspace member could obtain other members' external-service credentials and use them to access mail or calendars and potentially reset third-party accounts. Google and Microsoft OAuth-only workspaces were not affected. This issue is fixed in version 2.7.0.

### 27. CVE-2026-105740｜langflow-ai / langflow
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T21:16:35.567)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T21:16:35.567 / 2026-10-05T21:16:35.567
- **官方描述（原文）**：Langflow is a tool for building and deploying AI-powered agents and workflows. Prior to 1.9.0, any authenticated Langflow user can achieve Remote Code Execution (RCE) on the server by adding an MCP server with the "Stdio" transport. The user-supplied command field is passed directly to bash -c "exec {command}" with zero validation, no allowlisting, and no sandboxing. The command executes immediately when the server list is fetched. Additionally, the env field allows arbitrary environment variable injection (e.g., LD_PRELOAD, PATH override). This vulnerability is fixed in 1.9.0.

### 28. CVE-2026-105697｜langflow-ai / langflow
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T21:16:35.087)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T21:16:35.087 / 2026-10-05T21:16:35.087
- **官方描述（原文）**：Langflow is a tool for building and deploying AI-powered agents and workflows. Before Langflow 1.10.3, the MCP stdio transport launched whatever command / args a user put in an MCP server configuration, with no allowlist and (before 1.10.3) wrapped in bash -c "exec {command} ...". Any user able to reach the MCP server settings ("Settings → MCP Servers → Add MCP Server", POST/PATCH /api/v2/mcp/servers/{server_name}) or to build a flow with the MCP Tools component could add a "server" whose command is an arbitrary OS command (touch, rm -rf, a reverse shell, ...). The command runs on the Langflow host as the Langflow process user as soon as Langflow tries to connect to the server (listing servers, loading tools, running the flow) — even when the UI then reports that the stdio server failed to start. With the default LANGFLOW_AUTO_LOGIN=true, GET /api/v1/auto_login hands out a token without credentials, so on an exposed instance running the default configuration this is reachable without an account. AUTO_LOGIN is documented as a development-only setting; with it disabled, any authenticated (non-admin) user can exploit it. This issue is fixed in Langflow 1.10.3, langflow-base 0.10.3, and lfx 1.10.3.

### 29. CVE-2026-105691｜penpot / penpot
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T20:17:19.137)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T20:17:19.137 / 2026-10-05T20:17:19.363
- **官方描述（原文）**：Penpot is an open-source design and prototyping platform. Prior to 2.18.0, the SVG exporter places an attacker-controlled text object's fill-color value into a ppmcolormask command string and executes that string through child_process.exec. A user who can edit a file can store shell metacharacters in the fill color and trigger SVG export, causing commands to execute with the exporter service's privileges. The same export can be triggered through a valid public share link to a malicious file. This vulnerability is fixed in 2.18.0.

### 30. CVE-2026-105641｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T19:17:18.560)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T19:17:18.560 / 2026-10-05T19:17:18.693
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, the deployments/aio/community/ and deployments/cli/community/ manifests provide fixed, publicly known SECRET_KEY and LIVE_SERVER_SECRET_KEY defaults that remain active when operators do not override them. The top-level setup.sh randomizes secrets only for the development Docker Compose path, leaving unchanged aio and cli community deployments with shared production secrets. Knowledge of SECRET_KEY enables attackers to forge Django-signed values and compromise accounts or sessions. Knowledge of LIVE_SERVER_SECRET_KEY bypasses live-service authentication on unchanged community deployments. This issue is fixed in 1.4.0.

### 31. CVE-2026-105639｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T19:17:18.213)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T19:17:18.213 / 2026-10-05T19:17:18.343
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, Plane's signup flow creates a logged-in User row for any submitted email without an out-of-band ownership check, while User.email is unique=True. The authenticated user can call GET /api/users/me/workspaces/invitations/, which returns each WorkspaceMemberInvite whose email matches request.user.email. WorkSpaceMemberInviteSerializer uses fields = "all", exposing the token that protects the invitation join endpoint. An unauthenticated attacker who knows a target's email can register an account using that address, enumerate pending invitations, and accept an invitation as the target, joining a workspace at the invited role. The term pre-auth describes the attacker's initial state: the attacker has no credential before signup, while the enumeration and join requests use the session created by that signup. This issue is fixed in 1.4.0.

### 32. CVE-2026-105636｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T19:17:17.693)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T19:17:17.693 / 2026-10-05T19:17:17.827
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, the webhook delivery task in apps/api/plane/bgtasks/webhook_task.py calls requests.post() without allow_redirects=False and does not validate redirect targets. validate_url() blocks private, loopback, link-local, and reserved addresses in the original webhook URL, but the final URL reached after one or more redirects is not checked. A user who can create a workspace can register a webhook pointing to an attacker-controlled public endpoint that returns a 302 redirect to an internal address. The Plane worker then fetches internal resources, including cloud metadata, and stores the response body in webhook_logs, where the attacker can retrieve it through the workspace webhook-logs API. This issue is fixed in 1.4.0.

### 33. CVE-2026-105484｜TOTOLINK / X6000R
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-06T02:17:04.040)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-06T02:17:04.040 / 2026-10-06T02:17:04.040
- **官方描述（原文）**：A security vulnerability has been detected in TOTOLINK X6000R 9.4.0cu.652_B20230116. The impacted element is the function firmware_check of the file /cgi-bin/cstecgi.cgi of the component UploadFirmwareFile Handler. Such manipulation of the argument file_name leads to os command injection. The attack may be performed from remote.

### 34. CVE-2026-103510｜Perforce / P4 (Helix Core)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T09:17:06.977)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.00348 / percentile=0.26145
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T09:17:06.977 / 2026-10-05T13:16:50.733
- **官方描述（原文）**：P4 Search prior to 2026.4.2 does not fail securely when its service authentication token is blank. In affected configurations, an unauthenticated attacker with network access can obtain the highest application privilege, potentially leading to compromise of P4 Search and the connected P4 Server.

### 35. CVE-2026-103352｜WP BASE / WP BASE Booking
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T19:17:13.847)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T19:17:13.847 / 2026-10-05T19:17:13.847
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in WP BASE WP BASE Booking wp-base-booking-of-appointments-services-and-events allows Blind SQL Injection.This issue affects WP BASE Booking: from n/a through 6.4.0.

### 36. CVE-2026-102428｜ordasoft.com / OrdaSoft Joomla CCK
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T16:17:04.177)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T16:17:04.177 / 2026-10-05T17:17:09.403
- **官方描述（原文）**：Joomla Extension - ordasoft.com - Unauthenticated SQL injection in OrdaSoft Joomla CCK < 8.3.16 - The order column for records was user provided and not properly validated, leading to a SQL injection vector.

### 37. CVE-2026-100103｜Perfoce / P4 (Helix Core)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T09:17:05.717)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 10.0 (CRITICAL)
- **EPSS**：0.00424 / percentile=0.34485
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T09:17:05.717 / 2026-10-05T14:17:15.167
- **官方描述（原文）**：Perforce P4 Search container images prior to 2026.4.2 reset the service authentication token to a publicly documented default value. An unauthenticated attacker with network access can obtain the highest application privilege, potentially leading to arbitrary code execution and compromise of the connected P4 Server.

### 38. CVE-2026-100102｜Perforce / P4 (Helix Core)
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T09:17:05.540)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.00357 / percentile=0.27154
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T09:17:05.540 / 2026-10-05T14:17:13.667
- **官方描述（原文）**：Perforce P4 Search container images prior to 2026.4.2 enable an unauthenticated Java debug interface. An attacker with network access to this interface can execute arbitrary code as the P4 Search service account, potentially leading to compromise of the connected P4 Server.

### 39. CVE-2026-105695｜penpot / penpot
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T20:17:20.017)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.9 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T20:17:20.017 / 2026-10-05T21:16:34.983
- **官方描述（原文）**：Penpot is an open-source design and prototyping platform. Prior to 2.18.0, assemble-chunks retrieves an upload session using only its session ID, while upload-chunk correctly scopes the lookup to the authenticated profile. An authenticated user who obtains another user's live, completed upload-session UUID can assemble the victim's chunks into the attacker's own file, team font, or project import, disclosing the uploaded bytes and deleting the victim's pending session. This issue is fixed in version 2.18.0.

### 40. CVE-2026-105384｜UNION / HospitalManagementSystem
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T18:17:35.553)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T18:17:35.553 / 2026-10-05T19:17:16.557
- **官方描述（原文）**：A vulnerability was found in UNION HospitalManagementSystem up to 9ef91ed6007314b6473110ed699dff76d158f61d. Affected is an unknown function of the file patient_info.php. Performing a manipulation of the argument patient_id results in sql injection. The attack is possible to be carried out remotely. The exploit has been made public and could be used. This product adopts a rolling release strategy to maintain continuous delivery. Therefore, version details for affected or updated releases cannot be specified. The project was informed of the problem early through an issue report but has not responded yet.

### 41. CVE-2026-105382｜onetwothreeneth / HospitalManagementSystem
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T17:17:14.147)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T17:17:14.147 / 2026-10-05T18:17:35.413
- **官方描述（原文）**：A flaw has been found in onetwothreeneth HospitalManagementSystem up to 9ef91ed6007314b6473110ed699dff76d158f61d. This affects the function update_subaccount of the file php/controller.php of the component Account Administration. This manipulation of the argument user_id causes improper authorization. Remote exploitation of the attack is possible. The exploit has been published and may be used. This product follows a rolling release approach for continuous delivery, so version details for affected or updated releases are not provided. The project was informed of the problem early through an issue report but has not responded yet.

### 42. CVE-2026-105253｜itsourcecode / Online Admission System Project
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T09:17:11.753)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00263 / percentile=0.16502
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T09:17:11.753 / 2026-10-05T14:17:19.937
- **官方描述（原文）**：A vulnerability was determined in itsourcecode Online Admission System Project 1.0. This issue affects some unknown processing of the file /admin/login1.php. This manipulation of the argument User causes sql injection. The attack can be initiated remotely. The exploit has been publicly disclosed and may be utilized.

### 43. CVE-2026-105247｜SourceCodester / Online Reviewer Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T08:17:15.020)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00263 / percentile=0.16498
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T08:17:15.020 / 2026-10-05T16:17:11.737
- **官方描述（原文）**：A vulnerability was determined in SourceCodester Online Reviewer Management System 1.0. The affected element is an unknown function of the file /reviewer_0/admins/assessments/Subject/btn_functions.php?action=course. Executing a manipulation of the argument Subject can lead to sql injection. The attack can be launched remotely. The exploit has been publicly disclosed and may be utilized.

### 44. CVE-2026-105246｜SourceCodester / Online Reviewer Management System
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T07:16:30.630)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00269 / percentile=0.17293
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T07:16:30.630 / 2026-10-05T15:17:20.057
- **官方描述（原文）**：A vulnerability was found in SourceCodester Online Reviewer Management System 1.0. Impacted is an unknown function of the file /reviewer_0/admins/assessments/Subject/btn_functions.php?action=update. Performing a manipulation of the argument Subject results in sql injection. The attack can be initiated remotely. The exploit has been made public and could be used.

### 45. CVE-2026-105238｜ChatGPTNextWeb / NextChat
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T07:16:30.180)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.5 (MEDIUM)
- **EPSS**：0.00392 / percentile=0.30972
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T07:16:30.180 / 2026-10-05T14:17:18.997
- **官方描述（原文）**：A flaw has been found in ChatGPTNextWeb NextChat up to 2.16.1. This vulnerability affects the function proxyHandler of the file app/api/proxy.ts of the component Proxy Fallback Handler. This manipulation of the argument x-base-url causes server-side request forgery. It is possible to initiate the attack remotely. The exploit has been published and may be used. The pull request to fix this issue awaits acceptance.

### 46. CVE-2026-104969｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T17:17:12.783)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T17:17:12.783 / 2026-10-05T18:17:32.003
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, the cycle-issues endpoint accepts issue UUIDs in the request body without validating that they belong to the caller's workspace. An authenticated user can add issues from any workspace to a cycle they control. If a victim issue is already assigned to a cycle, the operation removes it from the victim's cycle, causing a destructive cross-tenant write. This issue is fixed in 1.4.0.

### 47. CVE-2026-104965｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T17:17:12.103)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.4 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T17:17:12.103 / 2026-10-05T18:17:31.887
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, the issue-relation endpoint accepts issue UUIDs in the request body without validating that they belong to the caller's workspace. An authenticated user can create relations linking their own issues to issues in any other workspace on the instance, leaking issue metadata through activity events. This issue is fixed in 1.4.0.

### 48. CVE-2026-104964｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T17:17:11.943)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.8 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T17:17:11.943 / 2026-10-05T20:17:09.833
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, Plane's project update endpoint authorizes the caller against the workspace slug in the request URL but loads the target project globally by UUID without binding it to that workspace. An administrator of one workspace can modify a project in another workspace when the victim project UUID is known. This violates tenant isolation and permits unauthorized cross-workspace changes to project metadata and configuration. This issue is fixed in 1.4.0.

### 49. CVE-2026-104962｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T17:17:11.610)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T17:17:11.610 / 2026-10-05T19:17:15.310
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, GET /api/v1/workspaces/{slug}/projects/{project_id}/members/ returns the complete project-member roster, including each member's email address, first and last name, display name, avatar, and role. ProjectMemberPermission gates the endpoint, but its SAFE_METHODS branch checks only whether the caller is an active ProjectMember of any project in the workspace and does not bind the check to view.project_id. The view then filters solely by the project_id supplied in the URL. Consequently, any authenticated user who belongs to one project in a workspace, including a Guest, can read the roster of another private project in the same workspace. This issue is fixed in 1.4.0.

### 50. CVE-2026-104960｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T17:17:11.307)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 6.5 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T17:17:11.307 / 2026-10-05T18:17:31.780
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, Plane exposes the workspace-scoped GET /api/assets/v2/workspaces/{workspace_slug}/download/{asset_id}/ endpoint for project-bound FileAsset objects without enforcing access to the asset's owning project. An authenticated user who belongs to the same workspace, is not a member of the victim's secret project, and knows the target asset UUID can receive a 302 redirect to a signed download URL. The intended project-scoped route for the same asset correctly returns 403. Confirmed affected project-bound asset types are ISSUE_ATTACHMENT, COMMENT_DESCRIPTION, PAGE_DESCRIPTION, and PROJECT_COVER. This bypass exposes private file content protected by the secret project boundary. This issue is fixed in 1.4.0.

### 51. CVE-2026-104956｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T17:17:11.143)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 5.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T17:17:11.143 / 2026-10-05T20:17:09.707
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, the unauthenticated public issues endpoint accepts group_by and sub_group_by query parameters and passes them without an allowlist to grouped paginators, where they are used as ORM field names by F(field), .values(field), .order_by(field), and Window partition_by operations. An anonymous attacker can supply arbitrary field paths that trigger an unhandled FieldError or KeyError and an HTTP 500 response, or force the ORM to resolve __-separated relational paths as a blind traversal oracle. This is the same field-name injection class addressed by earlier order_by sanitization, but that remediation left group_by and sub_group_by unvalidated. The issue does not directly disclose column values because issue_group_values() returns an empty list for unknown fields, the result projection uses a fixed required_fields list, and the subgrouped path raises KeyError before serialization. This issue is fixed in 1.4.0.

### 52. CVE-2026-104905｜NeoRazorX / facturascripts
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T18:17:31.623)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 6.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T18:17:31.623 / 2026-10-05T19:17:15.163
- **官方描述（原文）**：FacturaScripts before version 2026.7 contains a PHP object injection vulnerability in WidgetSelect::processFormData() that allows authenticated attackers to trigger unserialize() on raw POST data without an allowed_classes filter for multiple-select fields. Attackers can submit a serialized XLSXWriter object as the field value to invoke its __destruct() method, deleting arbitrary attacker-specified files such as config.php or backup data, resulting in denial of service and potential application reinstall hijack.

### 53. CVE-2026-104894｜makeplane / plane
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T17:17:10.810)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 4.3 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T17:17:10.810 / 2026-10-05T19:17:15.013
- **官方描述（原文）**：Plane is an open-source project management tool. Prior to 1.4.0, the modules endpoint accepts issue UUIDs in the URL path without validating that they belong to the caller's workspace. An authenticated user can link issues from any workspace to modules in their own workspace. This issue is fixed in 1.4.0.

### 54. CVE-2026-101893｜Newell Brands / DYMO ID
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T21:16:32.227)
- **Risk**：WATCH / score 22；reasons：POC_AVAILABLE(+10)、CVSS_MEDIUM(+4)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 5.1 (MEDIUM)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T21:16:32.227 / 2026-10-05T21:16:32.227
- **官方描述（原文）**：Newell Brands DYMO ID 1.5.1.71 parses job files using XmlDocument.Load() without disabling DTD processing. The PC Job Files view automatically parses every recognized job file extension on folder browse. A crafted file on any browsed network share can perform SSRF, capture NTLMv2 credentials, read local files, or crash the process. Fixed in 1.6.0.

### 55. CVE-2026-105315｜未確認 / django-haystack
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T13:16:52.823)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T13:16:52.823 / 2026-10-05T14:17:20.537
- **官方描述（原文）**：A vulnerability has been found in django-haystack up to 3.3.0. Affected is the function _to_python of the file haystack/backends/elasticsearch_backend.py of the component more_like_this Template Tag Handler. Such manipulation of the argument result_class leads to improper neutralization of directives in dynamically evaluated code. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. Upgrading to version 3.4.0 is able to address this issue. The name of the patch is eb05f193c9771a68dcc8cfac6674a0d48a52ee9d. It is suggested to upgrade the affected component.

### 56. CVE-2026-105291｜feelec-yishu / feelcrm-os
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T11:16:46.983)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T11:16:46.983 / 2026-10-05T11:16:46.983
- **官方描述（原文）**：A vulnerability was identified in feelec-yishu feelcrm-os 1.0.0. This vulnerability affects the function GroupController::index of the file App/Feelcrm/Index/Controller/GroupController.class.php of the component Department Search Endpoint. The manipulation of the argument keyword leads to cross site scripting. The attack can be initiated remotely. The exploit is publicly available and might be used. The project was informed of the problem early through an issue report but has not responded yet.

### 57. CVE-2026-105289｜feelec-yishu / feelcrm-os
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T11:16:46.617)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.0 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T11:16:46.617 / 2026-10-05T13:16:52.650
- **官方描述（原文）**：A vulnerability was found in feelec-yishu feelcrm-os 1.0.0. Affected by this issue is the function htmlspecialchars_decode of the file App/Feelcrm/Common/Model/CrmDefineFormModel.class.php of the component Create Customer Endpoint. Performing a manipulation of the argument customer_form[remark] results in cross site scripting. It is possible to initiate the attack remotely. The exploit has been made public and could be used. The project was informed of the problem early through an issue report but has not responded yet.

### 58. CVE-2026-105288｜feelec-yishu / feelcrm-os
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T10:16:41.713)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T10:16:41.713 / 2026-10-05T16:17:12.167
- **官方描述（原文）**：A vulnerability has been found in feelec-yishu feelcrm-os 1.0.0. Affected by this vulnerability is the function IndexController::index of the file App/ThinkPHP/Common/functions.php of the component Crm Endpoint. Such manipulation of the argument redirect_url leads to cross site scripting. The attack may be performed from remote. The exploit has been disclosed to the public and may be used. The project was informed of the problem early through an issue report but has not responded yet.

### 59. CVE-2026-105287｜feelec-yishu / feelcrm-os
- **Delta event**：NEW_CVE (from=未確認; to=2026-10-05T10:16:41.490)
- **Risk**：WATCH / score 18；reasons：POC_AVAILABLE(+10)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 2.1 (LOW)
- **EPSS**：0.00319 / percentile=0.22642
- **CISA KEV**：listed=false
- **Exploitation status**：status=poc / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-10-05T10:16:41.490 / 2026-10-05T12:17:09.180
- **官方描述（原文）**：A flaw has been found in feelec-yishu feelcrm-os 1.0.0. Affected is an unknown function of the file App/Feelcrm/Crm/Controller/AjaxRequestController.class.php of the component getMemberByGroups Endpoint. This manipulation of the argument groups[] causes sql injection. The attack is possible to be carried out remotely. The exploit has been published and may be used. The project was informed of the problem early through an issue report but has not responded yet.


## P1｜立即優先處理

目前沒有 P1 項目。

## P2 / P3｜排程處理與監控

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-88395 | P3 / 38 | 未確認 / 未確認 | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105640 | P3 / 38 | makeplane / plane | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105638 | P3 / 38 | makeplane / plane | v3.1 9.1 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105637 | P3 / 38 | makeplane / plane | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105285 | P3 / 38 | Totolink / A3002MU | v4.0 9.3 (CRITICAL) | 0.01096 / percentile=0.64399 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105284 | P3 / 38 | Totolink / A3002MU | v4.0 9.3 (CRITICAL) | 0.00784 / percentile=0.54511 | listed=false | status=poc / source=nvd_ssvc | 未確認 |

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-12171 | WATCH / 30 | cookpete / auto-changelog | v4.0 8.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105773 | WATCH / 30 | Canimaan Software / ClamXAV | v4.0 7.3 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105635 | WATCH / 30 | makeplane / plane | v3.1 7.4 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105633 | WATCH / 30 | makeplane / plane | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105632 | WATCH / 30 | makeplane / plane | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105630 | WATCH / 30 | makeplane / plane | v3.1 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-105628 | WATCH / 30 | makeplane / plane | v3.1 7.6 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104979 | WATCH / 30 | makeplane / plane | v3.1 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104977 | WATCH / 30 | makeplane / plane | v3.1 7.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104975 | WATCH / 30 | makeplane / plane | v3.1 7.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104974 | WATCH / 30 | makeplane / plane | v3.1 8.1 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104971 | WATCH / 30 | makeplane / plane | v3.1 8.5 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-104968 | WATCH / 30 | makeplane / plane | v4.0 8.7 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-102262 | WATCH / 30 | Newell Brands / DYMO ID | v4.0 7.0 (HIGH) | 未確認 | listed=false | status=poc / source=nvd_ssvc | 未確認 |
| CVE-2026-97283 | WATCH / 28 | Liquid Web / StellarWP / Advanced Post Manager | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-91107 | WATCH / 28 | OS4ED / openSIS-Classic | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-79820 | WATCH / 28 | Hewlett Packard Enterprise (HPE) / HPE Integrated Lights-Out (iLO) 7 | v3.1 9.0 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-77226 | WATCH / 28 | Camunda / Camunda 7 | v4.0 9.2 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-21589 | WATCH / 28 | Atlassian / Bamboo Data Center | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105763 | WATCH / 28 | twentyhq / twenty | v3.1 9.6 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105740 | WATCH / 28 | langflow-ai / langflow | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105697 | WATCH / 28 | langflow-ai / langflow | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105691 | WATCH / 28 | penpot / penpot | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-105641 | WATCH / 28 | makeplane / plane | v3.1 9.8 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

## 建議行動

### 24 小時內
- 以資產清冊、CMDB 或 SBOM 比對所有 P1 與 CISA KEV 項目是否存在於環境；本報告未取得組織資產清冊，因此實際曝險狀態為**未確認**。
- 對已列 CISA KEV 的項目，依本報告列出的 **CISA Required Action（原文）** 與官方來源核對後執行；不要由本報告自行推定適用版本。

### 本週內
- 檢視 P2 / P3 與 WATCH 項目的 NVD / vendor 來源，確認實際使用版本與官方處置；compact intelligence 未提供結構化受影響版本時，一律視為**未確認**。
- 對 exploitation status 為 `unconfirmed` 的項目持續等待官方或可信來源更新；EPSS 不作為『已遭利用』的證據。

### 持續監控
- 持續比較 KEV、EPSS、CVSS 與 exploitation status 的跨日變化；只有資料來源狀態變更才更新對應事實。
- Google Search grounding 恢復後，才允許 LLM 以有 citation 的方式補充 vendor advisory、修補與近期攻擊脈絡。

## 產業影響

本 Facts-only 模式**不進行未驗證的產業攻擊歸因**。是否影響台灣金融、製造、科技、政府或關鍵基礎設施，必須與組織自身的 CMDB、SBOM、軟體清冊及外網暴露面比對；目前輸入未提供該類組織資產資料，因此實際產業/組織受影響狀態為**未確認**。

## 資料品質與未確認事項

- Intelligence items：30；缺少 Vendor：1；缺少 Product：1；缺少 Title：30。
- EPSS 未確認：28；Exploitation status 未確認：8。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-10-06T07:01:43.975313+00:00`；Delta generated at：`2026-10-06T07:01:43.975313+00:00`。

---

## 可驗證資料來源

- **CVE-2026-88395** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88395)
- **CVE-2026-105640** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105640)
- **CVE-2026-105638** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105638)
- **CVE-2026-105637** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105637)
- **CVE-2026-105285** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105285) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105285)
- **CVE-2026-105284** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105284) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105284)
- **CVE-2026-12171** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-12171)
- **CVE-2026-105773** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105773)
- **CVE-2026-105635** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105635)
- **CVE-2026-105633** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105633)
- **CVE-2026-105632** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105632)
- **CVE-2026-105630** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105630)
- **CVE-2026-105628** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105628)
- **CVE-2026-104979** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104979)
- **CVE-2026-104977** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104977)
- **CVE-2026-104975** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104975)
- **CVE-2026-104974** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104974)
- **CVE-2026-104971** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104971)
- **CVE-2026-104968** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104968)
- **CVE-2026-102262** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102262)
- **CVE-2026-97283** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97283)
- **CVE-2026-91107** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91107)
- **CVE-2026-79820** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79820)
- **CVE-2026-77226** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77226)
- **CVE-2026-21589** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21589)
- **CVE-2026-105763** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105763)
- **CVE-2026-105740** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105740)
- **CVE-2026-105697** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105697)
- **CVE-2026-105691** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105691)
- **CVE-2026-105641** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105641)
- **CVE-2026-105639** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105639)
- **CVE-2026-105636** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105636)
- **CVE-2026-105484** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105484)
- **CVE-2026-103510** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103510) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-103510)
- **CVE-2026-103352** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103352)
- **CVE-2026-102428** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102428)
- **CVE-2026-100103** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100103) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-100103)
- **CVE-2026-100102** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-100102) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-100102)
- **CVE-2026-105695** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105695)
- **CVE-2026-105384** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105384)
- **CVE-2026-105382** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105382)
- **CVE-2026-105253** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105253) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105253)
- **CVE-2026-105247** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105247) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105247)
- **CVE-2026-105246** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105246) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105246)
- **CVE-2026-105238** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105238) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105238)
- **CVE-2026-104969** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104969)
- **CVE-2026-104965** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104965)
- **CVE-2026-104964** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104964)
- **CVE-2026-104962** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104962)
- **CVE-2026-104960** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104960)
- **CVE-2026-104956** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104956)
- **CVE-2026-104905** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104905)
- **CVE-2026-104894** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104894)
- **CVE-2026-101893** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101893)
- **CVE-2026-105315** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105315)
- **CVE-2026-105291** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105291)
- **CVE-2026-105289** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105289)
- **CVE-2026-105288** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105288)
- **CVE-2026-105287** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-105287) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-105287)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
