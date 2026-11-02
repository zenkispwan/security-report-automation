# 每日資安威脅情報簡報

> **資料來源模式：Verified facts only（deterministic）。** Google Search grounding 不可用或已停用；本報告由程式直接從 CISA KEV、NVD、FIRST EPSS 與 deterministic delta/risk 資料產生，**沒有使用 LLM model memory 產生正文**。未確認資料維持「未確認」。

## 執行摘要

- Daily Delta：**14** 筆符合目前門檻的重要變化；事件統計：NEW_CVE=14。
- Intelligence 候選：**30** 筆；P1 **16**、P2 **0**、P3 **0**、WATCH **14**。
- Baseline：state / generated_at=2026-11-01T07:00:11.176869+00:00 / available=true。
- 目前排序最前的 P1：CVE-2026-97229、CVE-2026-9586、CVE-2026-9198、CVE-2026-9082、CVE-2026-88772。此排序直接沿用 deterministic risk score，不由本報告重新評分。

## Daily Delta｜自上一份報告的重要變化

本次共有 **14** 筆 delta item；以下欄位直接取自 `data/delta.json`。

### 1. CVE-2026-62048｜Liquid Web / StellarWP / BookIt
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-01T16:18:15.170)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=none / source=nvd_ssvc
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-01T16:18:15.170 / 2026-11-01T18:18:11.907
- **官方描述（原文）**：Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Liquid Web / StellarWP BookIt bookit allows SQL Injection.This issue affects BookIt: from n/a through 2.6.0.6.

### 2. CVE-2026-120345｜WAVLINK / WN551X3-A
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T06:17:43.410)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T06:17:43.410 / 2026-11-02T06:17:43.410
- **官方描述（原文）**：A vulnerability was found in WAVLINK WN551X3-A M51X3_V251020-WO-182e965. This impacts the function sub_41a430 of the file /bin/ioos of the component DNS Resolution Handler. Performing a manipulation of the argument data results in os command injection. It is possible to initiate the attack remotely. The exploit has been made public and could be used. The vendor was contacted early about this disclosure.

### 3. CVE-2026-120344｜WAVLINK / WN551X3-A
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T05:18:25.450)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T05:18:25.450 / 2026-11-02T05:18:25.450
- **官方描述（原文）**：A vulnerability has been found in WAVLINK WN551X3-A M51X3_V251020-WO-182e965. This affects the function system of the file /bin/ioos of the component WireGuard CLI Group Handler. Such manipulation of the argument group_name leads to os command injection. The attack may be performed from remote. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure.

### 4. CVE-2026-120338｜PrefectHQ / prefab-ui
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-01T16:18:14.970)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-01T16:18:14.970 / 2026-11-01T16:18:14.970
- **官方描述（原文）**：Prefab UI's Generative UI sandbox runs caller-supplied Python inside Pyodide, Python compiled to WebAssembly, in a Deno subprocess. The feature is documented as isolation for untrusted code, including LLM-written UI. From prefab-ui 0.14.0 through 0.20.2 the launcher starts Deno with unrestricted --allow-read, --allow-write, and --allow-net, and the runner leaves the Deno API on the JavaScript global object. Pyodide's js module proxies that global, so the Python can call Deno.readTextFileSync and Deno.writeTextFileSync. A caller who can supply the code can read and write files as the server OS user, and can persist code execution by writing a .pth file into the server virtualenv's site-packages. The usual remote path is FastMCP's GenerativeUI provider, which registers the MCP tool generate_prefab_ui and forwards that tool's code argument into this sandbox. On a FastMCP server with no authentication configured, any client who can reach the server can call the tool. With authentication, any client allowed to call tools can. Generative UI is opt-in, and the host must have Deno installed. Confirmed on prefab-ui 0.20.2. Fixed in 0.21.0: after the runtime and Prefab sources load, the runner revokes Deno read, write, and network permission before it accepts code, the process is started with --no-prompt so a permission request cannot grant them again, and bootstrap network access is limited to cdn.jsdelivr.net. The fix is commit 030f074 (pull request 538).

### 5. CVE-2026-120308｜beam-cloud / Beta9 gateway
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-01T13:18:01.670)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-01T13:18:01.670 / 2026-11-01T13:18:01.670
- **官方描述（原文）**：A Beta9 tenant can attach a volume when deploying a function, endpoint, or task queue. The gateway builds the host path by joining the shared volumes root, the workspace name, and the volume identifier from the stub configuration. Nothing checks that the identifier names a volume that workspace owns. Parent-directory segments in the identifier collapse the joined path to the worker's filesystem root, and the worker bind-mounts that path into the sandbox read-write unless the volume was explicitly marked read-only. A tenant with a workspace token can therefore read and write the worker's files, including other tenants' volumes stored on that machine. Confirmed against gateway 0.1.769 and worker 0.1.745. Fixed in gateway 0.1.776 and worker 0.1.756: volume identifiers and mount paths are validated before a mount is built, including for stubs saved before the check existed, and the gateway rejects a volume that does not exist or is not owned by the workspace.

### 6. CVE-2026-120307｜beam-cloud / Beta9 worker
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-01T13:18:01.497)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-01T13:18:01.497 / 2026-11-01T13:18:01.497
- **官方描述（原文）**：The Beta9 worker serves the sandbox file API from outside the container. getHostPathFromContainerPath turns the tenant's container path into a worker path. If the unresolved path starts with a mount destination, including the default upload mount at /tmp/.beta9, the remainder is joined onto that mount's source with filepath.Join, which cleans parent-directory segments after the prefix check. A long enough run of those segments names any absolute path on the worker. A path that matches no mount is joined onto the container root and opened in the worker's own filesystem, so an absolute symbolic link such as /var/run pointing at /run is followed against the worker root. Upload, download, stat, list, find-in-files, replace-in-files, and delete-file all call this helper. A tenant with a workspace token and one running sandbox can read, write, list, and delete files on the hosting worker as root, including files of other tenants on that machine. A read-only proof downloaded the worker pod's Kubernetes service account token through the file API for a path that did not exist inside the sandbox. In the shipped remote-node manifests that service account is bound to cluster-admin. Fixed in worker 0.1.756: sandbox file operations and workspace sync open paths with os.OpenRoot, so parent-directory and symlink lookups stay inside the container root or the mount source.

### 7. CVE-2026-120306｜beam-cloud / Beta9 worker
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-01T13:18:01.300)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.9 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-01T13:18:01.300 / 2026-11-01T13:18:01.300
- **官方描述（原文）**：Beta9 turns each shell command in a tenant image definition into a Dockerfile RUN line and executes it with Buildah on the build worker. The worker image sets BUILDAH_ISOLATION=chroot, and no buildah invocation passes --isolation, so the step only changes its filesystem root. It keeps the worker pod's PID, network, IPC, and user namespaces, runs as uid 0, and holds CAP_DAC_OVERRIDE. PID 1 in that procfs is the worker entrypoint, so /proc/1/root is the worker container's filesystem and is writable. That filesystem contains the runc, buildah, and runsc binaries the worker uses to start tenant containers, the worker's Kubernetes service account token, and the host directories mounted into the pod. Worker pods are privileged. Clip v2 layered builds are the default, so a tenant with a workspace token reaches this by submitting one image build. The read-only proof confirmed the shared namespaces, CAP_DAC_OVERRIDE, and that the worker's runc binary is visible at /proc/1/root. Fixed in worker 0.1.756: Buildah RUN steps, including the WORKDIR mkdir, use OCI isolation with private PID, IPC, and network namespaces, and tenant ARG values are passed only into the build container.

### 8. CVE-2026-120283｜Linksys / E8450
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T01:17:27.500)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T01:17:27.500 / 2026-11-02T01:17:27.500
- **官方描述（原文）**：A vulnerability was identified in Linksys E8450 1.2.00.360516. Affected is the function strcpy of the file /www/cgi-bin/portal.cgi. Such manipulation of the argument hidden_timezone leads to stack-based buffer overflow. The attack can be executed remotely. The vendor was contacted early about this disclosure but did not respond in any way.

### 9. CVE-2026-120281｜WAVLINK / WN536AX6-A
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T01:17:27.070)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T01:17:27.070 / 2026-11-02T01:17:27.070
- **官方描述（原文）**：A vulnerability was found in WAVLINK WN536AX6-A V260507. This affects the function strcpy of the file /protocol.csp of the component OpenVPN Handler. The manipulation of the argument openvpn_ip results in stack-based buffer overflow. The attack may be launched remotely. The exploit has been made public and could be used. The vendor was contacted early about this disclosure.

### 10. CVE-2026-120280｜WAVLINK / WN536AX6-A
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T01:17:26.873)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T01:17:26.873 / 2026-11-02T01:17:26.873
- **官方描述（原文）**：A vulnerability has been found in WAVLINK WN536AX6-A V260507. The impacted element is the function wireguard_cli_group handler of the file /protocol.csp of the component WireGuard. The manipulation of the argument group_id/group_name leads to os command injection. The attack may be initiated remotely. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure.

### 11. CVE-2026-120279｜WAVLINK / WN536AX6-A
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T01:17:26.677)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T01:17:26.677 / 2026-11-02T01:17:26.677
- **官方描述（原文）**：A flaw has been found in WAVLINK WN536AX6-A V260507. The affected element is an unknown function of the file /protocol.csp of the component openvpn_cli Handler. Executing a manipulation of the argument file_id can lead to os command injection. The attack can be launched remotely. The exploit has been published and may be used. The vendor was contacted early about this disclosure.

### 12. CVE-2026-120277｜WAVLINK / WN536AX6-A
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T00:18:10.810)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T00:18:10.810 / 2026-11-02T00:18:10.810
- **官方描述（原文）**：A security vulnerability has been detected in WAVLINK WN536AX6-A V260507_2.0.0. This issue affects the function sub_41a1d8 of the file /bin/ioos of the component WireGuard CLI Group Handler. Such manipulation of the argument group_name leads to os command injection. It is possible to launch the attack remotely. The exploit has been disclosed publicly and may be used. The vendor was contacted early about this disclosure.

### 13. CVE-2026-120276｜WAVLINK / WN536AX6-A
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T00:18:09.897)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T00:18:09.897 / 2026-11-02T00:18:09.897
- **官方描述（原文）**：A weakness has been identified in WAVLINK WN536AX6-A V260507_2.0.0. This vulnerability affects the function sub_416760 of the file /bin/ioos of the component Web Management Interface. This manipulation of the argument group_name causes os command injection. It is possible to initiate the attack remotely. The exploit has been made available to the public and could be used for attacks. The vendor was contacted early about this disclosure.

### 14. CVE-2025-11969｜WSO2 / WSO2 API Manager
- **Delta event**：NEW_CVE (from=未確認; to=2026-11-02T06:17:42.087)
- **Risk**：WATCH / score 28；reasons：CVSS_CRITICAL(+20)、RECENTLY_PUBLISHED(+8)
- **CVSS**：v3.1 9.4 (CRITICAL)
- **EPSS**：未確認
- **CISA KEV**：listed=false
- **Exploitation status**：status=unconfirmed / source=未確認
- **Known ransomware campaign use**：未確認
- **Published / Updated**：2026-11-02T06:17:42.087 / 2026-11-02T06:17:42.087
- **官方描述（原文）**：The System REST APIs do not correctly enforce access control mechanisms, allowing users with lower privilege roles to execute administrative actions that should be restricted. This weakness permits unauthorized operations on the affected product. Successful exploitation could enable a malicious actor to perform unauthorized administrative operations, including executing administrative functions. APIs exposed through the WSO2 API Manager's API Gateway are not affected by this vulnerability.


## P1｜立即優先處理

以下為 deterministic risk engine 標記為 P1 的項目；不額外推論攻擊鏈、受影響版本或修補版本。

### 1. CVE-2026-97229｜GitLab / Community Edition and Enterprise Edition
- **Title**：GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 10.0 (CRITICAL)
- **EPSS**：0.273 / percentile=0.98061
- **CISA KEV**：listed=true / date_added=2026-10-29 / due_date=2026-11-01
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：GitLab Community Edition and Enterprise Edition contain a integer overflow or wraparound vulnerability that could allow an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 2. CVE-2026-9586｜Sangoma / Switchvox
- **Title**：Sangoma Switchvox SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.3 (CRITICAL)
- **EPSS**：0.18979 / percentile=0.97303
- **CISA KEV**：listed=true / date_added=2026-09-02 / due_date=2026-09-05
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Sangoma Switchvox contains a SQL injection vulnerability which allows an unauthenticated remote attacker to execute arbitrary SQL statements against the backend PostgreSQL database using a single crafted request, including database operations and remote code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 3. CVE-2026-9198｜IBM / Langflow
- **Title**：IBM Langflow Code Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.28658 / percentile=0.98138
- **CISA KEV**：listed=true / date_added=2026-08-04 / due_date=2026-08-07
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Langflow contains a code injection vulnerability that allows unauthenticated attackers to achieve full remote code execution on default Langflow deployments.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 4. CVE-2026-9082｜Drupal / Core
- **Title**：Drupal Core SQL Injection Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.89381 / percentile=0.99784
- **CISA KEV**：listed=true / date_added=2026-05-22 / due_date=2026-05-27
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Drupal Core contains a SQL injection vulnerability that could allow for privilege escalation and remote code execution via specially crafted requests sent with the database abstraction API.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 5. CVE-2026-88772｜Citrix / NetScaler
- **Title**：Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.78162 / percentile=0.99578
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for remote code execution or denial of service
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 6. CVE-2026-88771｜Citrix / NetScaler
- **Title**：Citrix NetScaler Improper Input Validation Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v4.0 9.5 (CRITICAL)
- **EPSS**：0.8216 / percentile=0.99655
- **CISA KEV**：listed=true / date_added=2026-09-27 / due_date=2026-09-30
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Citrix NetScaler ADC and NetScaler Gateway contain an improper input validation vulnerability that could allow an unauthenticated attacker to execute arbitrary commands.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 7. CVE-2026-86950｜Apple / Multiple Products
- **Title**：Apple Multiple Products Out-of-Bounds Write Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 8.8 (HIGH)
- **EPSS**：0.26166 / percentile=0.97995
- **CISA KEV**：listed=true / date_added=2026-09-29 / due_date=2026-10-13
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Apple iOS, macOS, and iPadOS contain an out-of-bounds write vulnerability in CoreGraphics that may lead to arbitrary code execution.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 8. CVE-2026-6973｜Ivanti / Endpoint Manager Mobile (EPMM)
- **Title**：Ivanti Endpoint Manager Mobile (EPMM) Improper Input Validation Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_HIGH(+12)、EPSS_HIGH(+14)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 7.2 (HIGH)
- **EPSS**：0.34454 / percentile=0.98414
- **CISA KEV**：listed=true / date_added=2026-05-07 / due_date=2026-05-10
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：Ivanti Endpoint Manager Mobile (EPMM) contains an improper input validation vulnerability that allows a remotely authenticated user with administrative access to achieve remote code execution.
- **CISA Required Action（原文）**：Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 9. CVE-2026-63077｜JetBrains / TeamCity
- **Title**：JetBrains TeamCity Deserialization of Untrusted Data Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、KNOWN_RANSOMWARE_USE(+20)、CVSS_CRITICAL(+20)、EPSS_VERY_HIGH(+20)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.93558 / percentile=0.99841
- **CISA KEV**：listed=true / date_added=2026-08-05 / due_date=2026-08-08
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Known
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：JetBrains TeamCity contains a deserialization of untrusted data vulnerability that could allow unauthenticated remote code execution via the agent polling protocol.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。

### 10. CVE-2026-63030｜WordPress / Core
- **Title**：WordPress Core Interpretation Conflict Vulnerability
- **Risk**：P1 / score 100；reasons：CISA_KEV(+45)、ACTIVE_OR_KNOWN_EXPLOITATION(+25)、CVSS_CRITICAL(+20)、EPSS_ELEVATED(+8)、EPSS_TOP_5_PERCENT(+5)
- **CVSS**：v3.1 9.8 (CRITICAL)
- **EPSS**：0.10649 / percentile=0.95799
- **CISA KEV**：listed=true / date_added=2026-07-21 / due_date=2026-07-24
- **Exploitation status**：status=known_exploited / source=cisa_kev
- **Known ransomware campaign use**：Unknown
- **受影響版本**：未確認（compact intelligence 未提供結構化受影響版本）
- **官方描述（原文）**：WordPress Core contains an interpretation conflict vulnerability that could allow an attacker to perform SQL Injection and achieve Remote Code Execution. This vulnerability can be chained with CVE-2026-60137.
- **CISA Required Action（原文）**：Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.
- **處置原則（系統規則）**：先比對組織資產與適用版本，再依上方官方來源/required action 執行；本報告不自行推定 patch 名稱或版本。


### 其他 P1

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-56291 | P1 / 100 | Balbooa / Forms | v4.0 10.0 (CRITICAL) | 0.14854 / percentile=0.96696 | listed=true / date_added=2026-07-10 / due_date=2026-07-13 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-56290 | P1 / 100 | Joomlack / Page Builder | v4.0 10.0 (CRITICAL) | 0.30866 / percentile=0.98252 | listed=true / date_added=2026-07-07 / due_date=2026-07-10 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-48939 | P1 / 100 | iCagenda / iCagenda | v4.0 10.0 (CRITICAL) | 0.20069 / percentile=0.97447 | listed=true / date_added=2026-07-10 / due_date=2026-07-13 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-48908 | P1 / 100 | JoomShaper / SP Page Builder | v4.0 10.0 (CRITICAL) | 0.88512 / percentile=0.99771 | listed=true / date_added=2026-07-07 / due_date=2026-07-10 | status=known_exploited / source=cisa_kev | Unknown |
| CVE-2026-45321 | P1 / 100 | TanStack / TanStack | v3.1 9.6 (CRITICAL) | 0.03278 / percentile=0.88427 | listed=true / date_added=2026-05-27 / due_date=2026-06-10 | status=known_exploited / source=cisa_kev | Known |
| CVE-2026-42271 | P1 / 100 | BerriAI / LiteLLM | v4.0 8.7 (HIGH) | 0.91445 / percentile=0.99812 | listed=true / date_added=2026-06-08 / due_date=2026-06-22 | status=known_exploited / source=cisa_kev | Unknown |

## P2 / P3｜排程處理與監控

目前沒有 P2 / P3 項目。

## WATCH｜新增或待觀察項目

| CVE | Priority / Score | Vendor / Product | CVSS | EPSS | KEV | Exploitation | Ransomware use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE-2026-62048 | WATCH / 28 | Liquid Web / StellarWP / BookIt | v3.1 9.3 (CRITICAL) | 未確認 | listed=false | status=none / source=nvd_ssvc | 未確認 |
| CVE-2026-120345 | WATCH / 28 | WAVLINK / WN551X3-A | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120344 | WATCH / 28 | WAVLINK / WN551X3-A | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120338 | WATCH / 28 | PrefectHQ / prefab-ui | v3.1 10.0 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120308 | WATCH / 28 | beam-cloud / Beta9 gateway | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120307 | WATCH / 28 | beam-cloud / Beta9 worker | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120306 | WATCH / 28 | beam-cloud / Beta9 worker | v3.1 9.9 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120283 | WATCH / 28 | Linksys / E8450 | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120281 | WATCH / 28 | WAVLINK / WN536AX6-A | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120280 | WATCH / 28 | WAVLINK / WN536AX6-A | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120279 | WATCH / 28 | WAVLINK / WN536AX6-A | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120277 | WATCH / 28 | WAVLINK / WN536AX6-A | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2026-120276 | WATCH / 28 | WAVLINK / WN536AX6-A | v4.0 9.3 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |
| CVE-2025-11969 | WATCH / 28 | WSO2 / WSO2 API Manager | v3.1 9.4 (CRITICAL) | 未確認 | listed=false | status=unconfirmed / source=未確認 | 未確認 |

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

- Intelligence items：30；缺少 Vendor：0；缺少 Product：0；缺少 Title：14。
- EPSS 未確認：14；Exploitation status 未確認：13。
- 結構化受影響版本未提供：30。本 renderer **不會**從 description 自行解析或猜測版本。
- Google Search grounding：本次不可用或已停用，因此沒有 Search query / citation，也不會用模型既有知識補齊 vendor advisory 或攻擊背景。
- Intelligence generated at：`2026-11-02T06:59:28.559925+00:00`；Delta generated at：`2026-11-02T06:59:28.559925+00:00`。

---

## 可驗證資料來源

- **CVE-2026-97229** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-97229) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-97229) · [Vendor / Advisory (ruby-lang.org)](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves) · [Vendor / Advisory (docs.gitlab.com)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9586** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9586) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9586) · [Vendor / Advisory (sangomakb.atlassian.net)](https://sangomakb.atlassian.net/wiki/spaces/Switchvox/pages/1802371073/Switchvox+-+Release+Notes+Version+8.4.0.2+July+14+2026) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9198** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9198) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9198) · [Vendor / Advisory (ibm.com)](https://www.ibm.com/support/pages/node/7278927) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-9082** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-9082) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-9082) · [Vendor / Advisory (drupal.org)](https://www.drupal.org/sa-core-2026-004)
- **CVE-2026-88772** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88772) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88772) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-62048** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62048)
- **CVE-2026-120345** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120345)
- **CVE-2026-120344** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120344)
- **CVE-2026-120338** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120338)
- **CVE-2026-120308** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120308)
- **CVE-2026-120307** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120307)
- **CVE-2026-120306** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120306)
- **CVE-2026-120283** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120283)
- **CVE-2026-120281** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120281)
- **CVE-2026-120280** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120280)
- **CVE-2026-120279** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120279)
- **CVE-2026-120277** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120277)
- **CVE-2026-120276** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120276)
- **CVE-2025-11969** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-11969)
- **CVE-2026-88771** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88771) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-88771) · [Vendor / Advisory (community.citrix.com)](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) · [Vendor / Advisory (support.citrix.com)](https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-88772)
- **CVE-2026-86950** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-86950) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-86950) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149226) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149228) · [Vendor / Advisory (support.apple.com)](https://support.apple.com/en-us/149229) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-6973** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-6973) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-6973) · [Vendor / Advisory (hub.ivanti.com)](https://hub.ivanti.com/s/article/May-2026-Security-Advisory-Ivanti-Endpoint-Manager-Mobile-EPMM-Multiple-CVEs?language=en_US)
- **CVE-2026-63077** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63077) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Vendor / Advisory (blog.jetbrains.com)](https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/) · [Vendor / Advisory (jetbrains.com)](https://www.jetbrains.com/privacy-security/issues-fixed/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-63030** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-63030) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-63030) · [Vendor / Advisory (wordpress.org)](https://wordpress.org/news/2026/07/wordpress-7-0-2-release/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-56291** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-56291) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-56291) · [Vendor / Advisory (balbooa.com)](https://www.balbooa.com/joomla-forms) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-56290** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-56290) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-56290) · [Vendor / Advisory (joomlack.fr)](https://www.joomlack.fr/en/joomla-extensions/page-builder-ck) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-48939** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48939) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48939) · [Vendor / Advisory (icagenda.com)](https://www.icagenda.com/#download) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-48908** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-48908) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-48908) · [Vendor / Advisory (extensions.joomla.org)](https://extensions.joomla.org/extension/sp-page-builder/) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk)
- **CVE-2026-45321** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-45321) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-45321) · [Vendor / Advisory (github.com)](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx)
- **CVE-2026-42271** — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-42271) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://api.first.org/data/v1/epss?cve=CVE-2026-42271) · [Vendor / Advisory (github.com)](https://github.com/BerriAI/litellm/security/advisories/GHSA-v4p8-mg3p-g94g) · [Vendor / Advisory (github.com)](https://github.com/BerriAI/litellm/releases/tag/v1.83.7-stable)

> 核心漏洞 Facts 來自 CISA KEV、NVD 與 FIRST EPSS；Google Search 僅用於補充即時背景與處置脈絡。未經確認的欄位應維持「未確認」。
