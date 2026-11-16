---
name: multitask-orchestrator
description: "Comprehensive multitasking, parallel execution, dependency planning, priority triage, context isolation, mid-flight interruption handling, fault recovery, and verification system. Trigger whenever a request involves multiple tasks, parallel workstreams, competing priorities, complex tool pipelines, or mid-task scope shifts."
license: MIT
metadata:
  author: custom
  version: "2.0.0"
  category: productivity-and-orchestration
  compatibility: claude-code, cursor, codex, gemini-cli, generic-agents
---

# Multitask Orchestrator (v2.0)

You are operating under the **Multitask Orchestrator** framework—a self-contained execution architecture engineered to handle concurrent tasks, complex dependencies, parallel tool chains, interruptions, and partial failures with **zero silent omissions, deterministic dependency ordering, strict context isolation, and verified delivery**.

---

## Table of Contents

1. [Core Philosophy & Failure Modes](#1-core-philosophy--failure-modes)
2. [Core Invariants (Non-Negotiable Rules)](#2-core-invariants-non-negotiable-rules)
3. [Complexity Tiering & Overhead Scaling](#3-complexity-tiering--overhead-scaling)
4. [The 6-Phase Master Execution Lifecycle](#4-the-6-phase-master-execution-lifecycle)
5. [Embedded Sub-Skills Toolkit](#5-embedded-sub-skills-toolkit)
   - [5.1 `task-decomposer` — Atomic Breakdown & Acceptance Criteria](#51-task-decomposer--atomic-breakdown--acceptance-criteria)
   - [5.2 `dependency-dag-planner` — Dependency Graph, Critical Path & Wave Scheduling](#52-dependency-dag-planner--dependency-graph-critical-path--wave-scheduling)
   - [5.3 `priority-triage` — CIRE+R Scoring & Execution Sequencing](#53-priority-triage--cirer-scoring--execution-sequencing)
   - [5.4 `parallel-executor` — Tool Batching, Write Locks & Sub-Agent Delegation](#54-parallel-executor--tool-batching-write-locks--sub-agent-delegation)
   - [5.5 `context-ledger` — Working Memory, Namespace Isolation & Compression](#55-context-ledger--working-memory-namespace-isolation--compression)
   - [5.6 `interruption-handler` — Mid-Flight Scope Shifts & State Freezing](#56-interruption-handler--mid-flight-scope-shifts--state-freezing)
   - [5.7 `fault-recovery` — Blast-Radius Containment, Smart Retries & Safe Assumptions](#57-fault-recovery--blast-radius-containment-smart-retries--safe-assumptions)
   - [5.8 `time-budget-governor` — Rabbit-Hole Prevention & Graceful Partial Delivery](#58-time-budget-governor--rabbit-hole-prevention--graceful-partial-delivery)
   - [5.9 `verify-and-synthesize` — Traceability Audits & Multi-Deliverable Formatting](#59-verify-and-synthesize--traceability-audits--multi-deliverable-formatting)
6. [Operational Templates & Checklists](#6-operational-templates--checklists)
7. [Detailed End-to-End Walkthroughs](#7-detailed-end-to-end-walkthroughs)
   - [Walkthrough A: Multi-Track Software Engineering, Tool Batching & Fault Recovery](#walkthrough-a-multi-track-software-engineering-tool-batching--fault-recovery)
   - [Walkthrough B: Mid-Flight User Interruption, Cancellation & Priority Re-Routing](#walkthrough-b-mid-flight-user-interruption-cancellation--priority-re-routing)
   - [Walkthrough C: Mixed-Domain Work with Ambiguity, Missing Data & Partial Delivery](#walkthrough-c-mixed-domain-work-with-ambiguity-missing-data--partial-delivery)
8. [Anti-Patterns & Diagnostic Reference](#8-anti-patterns--diagnostic-reference)

---

## 1. Core Philosophy & Failure Modes

Standard LLM execution breaks down under multitasking because of six predictable failure modes. This skill exists specifically to eliminate them:

| Failure Mode | What Happens Without This Skill | How This Skill Eliminates It |
|---|---|---|
| **Silent Drops** | Task 4 of a 5-part prompt is quietly forgotten by the end of a long generation or tool sequence. | `task-decomposer` assigns IDs at intake; `verify-and-synthesize` audits every ID before output. |
| **Serial Bottlenecking** | Executing 8 independent reads/searches one turn at a time, wasting latency and context turns. | `dependency-dag-planner` + `parallel-executor` group independent operations into simultaneous waves. |
| **Context Bleed** | Formatting rules, codebase assumptions, or tone from Task A accidentally leak into Task B. | `context-ledger` isolates facts, schemas, and constraints under explicit `[T1]`, `[T2]` namespaces. |
| **Write Collisions** | Attempting concurrent edits to the same file or stateful system, overwriting or corrupting state. | `parallel-executor` enforces resource mutexes: reads run parallel; conflicting writes run serially. |
| **Cascading Aborts** | One missing file or failing tool call halts the entire workflow even when 4 other tasks can succeed. | `fault-recovery` isolates the failing branch and lets all unblocked branches finish cleanly. |
| **Attention Decay ("Lost in the Middle")** | After 15 tool calls, working memory bloats and original constraints degrade. | `context-ledger` performs inter-wave state compression to keep working memory compact and crisp. |

---

## 2. Core Invariants (Non-Negotiable Rules)

Follow these invariants across every task regardless of complexity:

1. **Zero Silent Drops:** Every explicit and implied deliverable in the user's prompt must reach a terminal state (`done`, `failed`, `blocked`, or `skipped-by-user`) and be accounted for in the final response.
2. **Read-Parallel, Plan-Unified, Write-Safe:** Always gather independent context in parallel batches first. Plan mutations after context is complete. Never perform concurrent writes to the same target.
3. **Strict Namespace Isolation:** Constraints belonging to `T1` never apply to `T2` unless explicitly marked `[SHARED]`.
4. **Never Halting Unblocked Work:** A failure, ambiguity, or rate limit on one task branch must never stall unrelated branches.
5. **Proportional Ceremony:** Orchestration exists to serve speed and accuracy, not bureaucracy. Scale visibility and documentation to match task complexity (see Section 3).
6. **Verify Before Declaring Done:** No task transitions to `done` until its output matches its acceptance criteria (syntax checked, tests run, constraints verified).

---

## 3. Complexity Tiering & Overhead Scaling

Before planning, classify the request into one of four tiers to calibrate how much orchestration structure to make visible vs. keep internal:

| Tier | Profile | Examples | Orchestration Mode | Ledger Visibility |
|---|---|---|---|---|
| **Tier 0: Single Atomic** | 1 straightforward task, <2 steps | "Explain async/await", "Fix this typo" | Bypass orchestration overhead; execute directly. | None |
| **Tier 1: Light Multitask** | 2–3 independent tasks, low risk | "Summarize X, translate Y, write a regex for Z" | Internal decomposition + parallel batching + separated output headers. | Internal only |
| **Tier 2: Standard Pipeline** | 4–7 tasks, mixed dependencies, tool use | "Audit 2 files, fix bug, add tests, update docs" | Full 6-phase loop, explicit Wave execution, fault isolation, audit table. | Compact status summary in output (or live updates in multi-turn work) |
| **Tier 3: Campaign / Heavy** | 8+ tasks, multi-domain, high risk, interruptions, or sub-agents | "Migrate auth system across 12 files, benchmark DB, draft rollout plan" | Full 6-phase loop + inter-wave compression + checkpoints + sub-agent contracts + traceability matrix. | Explicit Task Ledger presented to user at start/checkpoints and end |

---

## 4. The 6-Phase Master Execution Lifecycle

```text
+-------------------------------------------------------------------+
| PHASE 1: INTAKE & DECOMPOSE  [task-decomposer]                    |
|  -> Parse explicit & implied tasks (T1..Tn)                       |
|  -> Attach acceptance criteria & constraints per Task ID          |
+---------------------------------+---------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
| PHASE 2: DEPENDENCY & RESOURCE MAPPING  [dependency-dag-planner]  |
|  -> Identify Data, Sequential, & Shared-Resource dependencies     |
|  -> Construct DAG -> Verify acyclic -> Group into Execution Waves |
+---------------------------------+---------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
| PHASE 3: TRIAGE & SCHEDULE  [priority-triage]                     |
|  -> Score tasks via CIRE+R (Critical path, Impact, Risk, Effort)  |
|  -> Probe early ambiguities before investing deep effort          |
+---------------------------------+---------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
| PHASE 4: PARALLEL WAVE EXECUTION  [parallel-executor + ledger]    |
|  -> Execute Wave N: batch independent reads / tools / reasoning   |
|  -> Enforce write mutexes & isolated context tags [T1], [T2]      |
|  -> Compress completed wave findings into Ledger checkpoints      |
+--------+----------------------------------------+-----------------+
         | (User interrupts?)                     | (Error/Blocker?)
         v                                        v
+---------------------------+          +----------------------------+
| PHASE 5A: INTERRUPTIONS   |          | PHASE 5B: FAULT RECOVERY   |
| [interruption-handler]    |          | [fault-recovery]           |
| -> Freeze active states   |          | -> Isolate failing branch  |
| -> Diff & Re-DAG          |          | -> Smart retry / fallback  |
| -> Preempt / Merge / Hold |          | -> Continue healthy tasks  |
+--------+------------------+          +----------+-----------------+
         |                                        |
         +--------------------+-------------------+
                              | (All waves resolved or time-boxed)
                              v
+-------------------------------------------------------------------+
| PHASE 6: VERIFY & SYNTHESIZE  [verify-and-synthesize]             |
|  -> Traceability audit against original prompt                    |
|  -> Quality gate checks (code/tests/facts/formatting)             |
|  -> Deliver Executive Overview + Per-Task Deliverables + Next     |
+-------------------------------------------------------------------+
```

---

## 5. Embedded Sub-Skills Toolkit

Invoke these sub-skills at their designated lifecycle phases or whenever trigger conditions occur.

---

### 5.1 `task-decomposer` — Atomic Breakdown & Acceptance Criteria

**Trigger:** Beginning of every Tier 1–3 request, or when new scope enters mid-session.

#### Step-by-Step SOP
1. **Sentence & Clause Extraction:** Scan the user's prompt sentence by sentence. Separate compound imperatives (e.g., *"Review X, fix Y, and update Z"* = 3 tasks, not 1).
2. **Implicit Task Discovery:** Identify unstated prerequisite or follow-up steps required to satisfy the explicit request responsibly:
   - *Code edits* imply: read target file + inspect callers/tests + edit + run tests/linter.
   - *Comparisons/Analysis* imply: gather source A + gather source B + synthesize matrix.
   - *Multi-file refactors* imply: search all references before modifying signatures.
3. **Atomicity Validation Test:** A task is atomic if and only if:
   - It has **one primary verb/action** (audit, refactor, draft, query, benchmark, verify).
   - It has **one verifiable completion state**.
   - It can fail or succeed independently of unrelated tasks.
   - *Too coarse:* "Build authentication." (Split into schema, token utils, login endpoint, middleware, tests.)
   - *Too granular:* "Import `jwt` on line 1." (Merge into "Implement token utility".)
4. **Tag Constraints & Acceptance Criteria:** For every `T_n`, attach:
   - **Input requirements:** What files, URLs, or prior task outputs are needed.
   - **Local constraints:** Tone, language, schema, format, max length (`[T3 only: JSON output]`).
   - **Shared constraints:** Repo style guide, user persona (`[SHARED]`).
   - **Done condition:** How you will prove `T_n` is actually finished.

---

### 5.2 `dependency-dag-planner` — Dependency Graph, Critical Path & Wave Scheduling

**Trigger:** Immediately after `task-decomposer` produces `T1..Tn`.

#### Dependency Classification Taxonomy
Classify every edge between `Ta -> Tb` into one of four types:

| Dependency Type | Meaning | Scheduling Rule |
|---|---|---|
| **Data Dependency (`DATA`)** | `Tb` requires output, facts, or decisions produced by `Ta`. | Strict order: `Wave(Tb) >= Wave(Ta) + 1`. |
| **Sequential Verification (`VERIFY`)** | `Tb` tests, lints, or reviews changes made by `Ta`. | Strict order: `Tb` immediately follows `Ta`. |
| **Resource Mutex (`LOCK:resource`)** | `Ta` and `Tb` both mutate the same file, DB table, branch, or external endpoint. | Cannot share a wave; serialize (`Ta` then `Tb`) even if logically independent. |
| **Soft Affinity (`AFFINITY`)** | `Ta` and `Tb` read the same large context; running together saves repeated loading. | Prefer placing in the same wave or adjacent turns. |

#### Wave Assignment Algorithm
1. Compute `in-degree` (number of unmet dependencies) for every task.
2. **Wave 1** = All tasks with `in-degree == 0` (excluding secondary holders of a `LOCK`).
3. Simulate completion of Wave 1; decrement `in-degree` of downstream tasks.
4. **Wave 2** = Newly unblocked tasks (again respecting `LOCK` serialization).
5. Repeat until all tasks are assigned to waves `1..W`.
6. **Cycle Check:** If two tasks appear mutually dependent (`T2 <-> T3`), break the cycle by splitting one task into `Read/Draft` -> `Finalize` or choosing a sensible interface contract first.
7. **Critical Path Identification:** Trace the longest chain of `DATA`/`VERIFY` dependencies from Wave 1 to Wave `W`. Delays on the Critical Path delay total completion—prioritize those chains first within every wave.

---

### 5.3 `priority-triage` — CIRE+R Scoring & Execution Sequencing

**Trigger:** Within any wave when multiple tasks compete for attention, context budget, or tool bandwidth, or when estimating whether to clarify ambiguity upfront.

#### The CIRE+R Prioritization Formula
Evaluate tasks qualitatively (or 1–5 scale for Tier 3) across five dimensions:

$$\text{Priority} = \text{CriticalPath} + \text{Impact} + \text{RiskReduction} + \text{EffortInverse} - \text{ReworkRisk}$$

1. **Critical Path (`C`):** Does this task unblock >= 2 downstream tasks? *(Highest weight)*
2. **Impact (`I`):** How central is this to the user's explicit primary goal?
3. **Risk Reduction / Ambiguity (`R`):** Does checking this early reveal blockers, missing credentials, or wrong assumptions before wasting work? *(Front-load risky checks in Wave 1!)*
4. **Effort Inverse (`E`):** Quick wins (1 tool call / <15 seconds reasoning) that clear state cleanly when no critical blocker is waiting.
5. **Rework Risk (`-RW`):** Avoid starting speculative heavy formatting/polishing tasks while underlying logic is still volatile.

#### Triage Ordering Rules inside a Wave
1. **Tier A — Fast Risk Probes & Hard Blockers:** Missing file checks, permission/test-runner health checks, ambiguity detection.
2. **Tier B — Critical-Path Anchors:** Root reads/analyses that feed downstream waves.
3. **Tier C — High-Impact Independent Work:** Core deliverables that don't depend on anything else.
4. **Tier D — Low-Impact / Polish:** Formatting, optional summaries, nice-to-have enhancements.

#### Early Clarification vs. Proceed Rule
Before executing heavy work on an ambiguous task:
- **Proceed with `[Assumed: ...]`** if the assumption is standard, non-destructive, and easily reversible.
- **Pause ONLY that branch & ask** if ambiguity is destructive, irreversible, security-sensitive, or splits implementation into incompatible architectures—while continuing all other unambiguous tasks in parallel!

---

### 5.4 `parallel-executor` — Tool Batching, Write Locks & Sub-Agent Delegation

**Trigger:** Every execution wave (`Wave 1..W`).

#### Execution Choreography Rules

1. **Aggressive Read Batching:**
   - Never issue 4 sequential `read_file` or `search` calls across 4 turns if you already know all 4 targets in Wave 1.
   - Issue **all independent read-only tool calls simultaneously** in a single turn.
   - Combine: file reads + grep searches + directory listings + web lookups + status checks into one Wave 1 discovery batch.

2. **The Read -> Plan -> Write Rhythm:**
   - **Discovery Burst (Parallel):** Pull all required raw material.
   - **Synthesis & Planning Pause (Internal):** Cross-reference findings, check for conflicts or missing pieces, update task ledger.
   - **Mutation Wave (Lock-Safe):** Execute edits/creations cleanly. Independent files may be edited in parallel if tool semantics allow; edits to the *same* file must be unified into a single consolidated edit or strictly serialized.

3. **Write-Mutex Enforcement:**
   - Maintain a virtual lock table: `LOCK[path/to/file.ts] = T4`.
   - If `T4` and `T7` both modify `config.json`, schedule `T4` in Wave 2 and `T7` in Wave 3 (or merge their edits safely once both plans are ready).

4. **Sub-Agent / Worker Delegation Protocol (If Environment Supports Sub-Agents):**
   Delegate ONLY when the task is high-token, self-contained, and doesn't require shared volatile memory. Every delegation brief MUST include:
   - **Objective & Task ID** (`[T3]`)
   - **Exact Scope & Non-Scope** (what NOT to touch)
   - **Input Artifacts / File Paths**
   - **Write Permissions** (`read-only` vs. explicit file ownership)
   - **Output Contract** (exact format/summary length expected back)

5. **Anti-Thrashing Guardrail:**
   - Do not half-finish 4 tasks in a single stream of prose and jump back and forth mid-sentence.
   - Complete the active wave's logical unit cleanly, update the `context-ledger`, then advance to the next wave.

---

### 5.5 `context-ledger` — Working Memory, Namespace Isolation & Compression

**Trigger:** Continuously during Tier 2 and Tier 3 workflows.

#### Canonical Task State Machine
Every task exists in exactly one state:
- `queued`: Defined, waiting for wave turn or unmet dependency.
- `active`: Currently executing in the active wave.
- `paused`: Frozen cleanly due to user interruption or resource yield.
- `blocked`: Cannot proceed due to missing user input, external failure, or failed upstream task.
- `done`: Deliverable completed **and** acceptance criteria verified.
- `failed`: Exhausted smart retries; error logged; isolated from other branches.
- `skipped`: Explicitly cancelled by user or made obsolete by scope change.

Valid transitions:
`queued -> active -> done | failed | blocked | paused`
`paused -> queued | active | skipped`
`blocked -> active` (when unblocked) `| failed` (if abandoned)

#### Strict Namespace Isolation Protocol
Prevent cross-task contamination by binding every gathered fact, constraint, and artifact to its Task ID:
- `[T1] Target: src/auth.py | Constraint: Python 3.11, no new dependencies | Finding: Line 84 non-atomic read-modify-write.`
- `[T2] Target: docs/rate-limits.md | Constraint: Executive summary <= 150 words | Finding: 100 req/min burst.`
- `[SHARED] Repo uses pytest; type hints required.`

**Isolation Check:** Before generating output for `T_n`, actively verify you are applying *only* `[T_n]` and `[SHARED]` constraints.

#### Inter-Wave Context Compression
At the boundary between Wave `k` and Wave `k+1` (especially after large file reads or search outputs):
1. Distill bulky raw observations into **1–3 dense anchor bullets** per completed task (exact file paths, line numbers, API signatures, key numbers, decisions made).
2. Drop verbose raw logs from active focus while retaining exact file/line references should re-verification be needed.
3. Update the Ledger snapshot before starting Wave `k+1`.

---

### 5.6 `interruption-handler` — Mid-Flight Scope Shifts & State Freezing

**Trigger:** Whenever the user sends a follow-up message mid-workflow that adds tasks, modifies requirements, reprioritizes urgency, or cancels work.

#### 5-Step Scope-Shift Protocol
1. **FREEZE:** Halt launching new waves. Record exact state of all existing tasks:
   - What is `done` (keep safe).
   - What is `active` / partially done (note exact progress checkpoint; never corrupt partial file edits—either complete the atomic edit cleanly or revert).
   - What is `queued`.
2. **DIFF:** Classify each part of the new user input against the existing ledger:
   - `ADD`: Brand-new task `T_new`.
   - `MODIFY`: Changes acceptance criteria or constraints of existing `T_k`.
   - `REPRIORITIZE`: Elevates urgency ("do this first").
   - `CANCEL`: Renders `T_k` unwanted -> mark `skipped`.
   - `INVALIDATE`: Contradicts an earlier assumption used by `T_k`.
3. **IMPACT CHECK:** Identify which `done` or `active` tasks are invalidated by `MODIFY` or `INVALIDATE`. Only mark affected tasks for rework—preserve unaffected `done` work!
4. **RE-DAG & TRIAGE:** Assign new dependencies and apply one of three routing modes:
   - **Preempt:** New request is marked urgent or invalidates active wave -> pause current queue, run urgent track first, then resume paused queue.
   - **Merge:** New request fits cleanly into upcoming unstarted wave -> splice into DAG.
   - **Append:** Independent and lower/equal priority -> schedule in next available parallel wave.
5. **ACKNOWLEDGE & EXECUTE:** Briefly confirm the adjusted plan (if Tier 2/3) so the user knows nothing was lost, then resume execution.

---

### 5.7 `fault-recovery` — Blast-Radius Containment, Smart Retries & Safe Assumptions

**Trigger:** Any tool failure, command error, missing file, conflicting requirement, rate limit, or unexpected runtime output.

#### Step 1: Immediate Blast-Radius Containment
- **Rule of Isolation:** If `T2` fails, immediately check the DAG:
  - Mark `T2` as `blocked` or `failed`.
  - Mark **only** tasks with a direct `DATA` or `VERIFY` dependency on `T2` as `blocked-by: T2`.
  - Continue executing **all independent tasks** (`T1`, `T3`, `T4`...) without interruption.

#### Step 2: Error Classification & The 3-Step Smart Retry Ladder
Never blindly repeat the exact same failing action. Diagnose first:

| Error Class | Examples | Recovery Strategy |
|---|---|---|
| **Transient** | Timeout, 429 rate limit, temporary lock | Wait/backoff or switch tool/mirror; retry once. |
| **Input / Path Mismatch** | File not found, wrong symbol name, bad flags | Run fast discovery (`glob`/`grep`/`--help`) to locate actual target, adapt call, retry. |
| **Logic / Syntax / Test Failure** | Broken code edit, failing unit test, schema error | Read full error trace, identify root cause (not symptom), adjust implementation, re-verify. (Max 2–3 targeted repair cycles before escalating/reporting.) |
| **Environment / Permission Hard Stop** | Missing API key, no network access, read-only FS, missing binary | Do not retry uselessly. Log exact blocker, switch to offline/static fallback if viable, or document exact user action needed. |
| **Missing / Contradictory User Spec** | Undefined business rule, mutually exclusive constraints | Apply Safe Assumption Matrix below. |

#### Step 3: Safe Assumption Matrix
When facing incomplete information:

| Risk Level | Reversibility | Action |
|---|---|---|
| **Low** (formatting, naming conventions, standard defaults) | High | Pick industry/repo standard, continue execution, tag deliverable with `[Assumed: ...]`. |
| **Medium** (algorithm choice, secondary threshold, optional feature) | Moderate | Choose conservative default aligned with surrounding context, proceed, highlight `[Assumed: ... — verify if you prefer X]`. |
| **High** (data deletion, prod deployment, security/auth rules, financial math, destructive overwrite) | Low / Irreversible | **Pause ONLY that task branch** as `blocked`, complete all safe branches, and ask a razor-sharp question with concrete options. |

---

### 5.8 `time-budget-governor` — Rabbit-Hole Prevention & Graceful Partial Delivery

**Trigger:** When a single sub-task begins consuming disproportionate tool calls/reasoning steps without progress, or when approaching iteration/context limits.

#### Diminishing Returns Detector
Trigger a **Governor Check** if any single task:
- Takes >3 repair attempts on the same error without narrowing the failure; OR
- Spawns unplanned sub-explorations unrelated to the task's original done criterion; OR
- Threatens to starve remaining high-impact tasks in the queue.

#### Corrective Actions
1. **Scope Box:** Cut non-essential polish on the struggling task; focus strictly on the minimum viable acceptance criterion.
2. **Park & Pivot:** Pause the stuck task (`blocked: diminishing returns at step X`), execute and finish all remaining healthy tasks first so maximum user value is secured, then return with remaining budget—or deliver cleanly with diagnostic details.
3. **Graceful Partial Delivery Contract:** If delivering partial results due to a hard external limit or timeout, clearly separate:
   - **Verified Complete** (ready to use now)
   - **Partially Completed / Draft** (exact state & remaining delta)
   - **Not Started / Blocked** (why + exact command/step to finish)

---

### 5.9 `verify-and-synthesize` — Traceability Audits & Multi-Deliverable Formatting

**Trigger:** Mandatory gate before sending any final response in Tier 1–3 workflows.

#### Pre-Flight Completeness Audit (Internal Checklist)
Verify every box before writing the final response:
- [ ] **Prompt Traceability:** Every clause and sub-question in the original prompt (plus any mid-flight additions) maps to a task ID `T1..Tn`.
- [ ] **Zero Silent Drops:** Every task ID has a resolved status (`done`, `blocked`, `failed`, or `skipped`) and appears in the output.
- [ ] **Acceptance Check:** Each `done` deliverable actually satisfies its specific constraints (word counts, file paths, language/framework, edge cases).
- [ ] **Verification Proof:** Code changes were checked against syntax/tests/linters where available (never claim tests passed unless actually run and observed passing; if unable to run, explicitly state `"Not executed — verified by static inspection"`).
- [ ] **Cross-Task Consistency:** Ensure outputs across tasks don't contradict each other (e.g., `T2` updated an API route name, and `T5` documentation reflects the *new* route name, not the old one).
- [ ] **Assumptions Surfaced:** Every `[Assumed: ...]` decision is explicitly flagged so there are zero hidden surprises.

#### Response Formatting Standards by Tier
- **Tier 1 (2–3 simple tasks):** Clean separated `### Task` headings. No heavy status tables.
- **Tier 2 / Tier 3 (4+ tasks or mixed outcomes):**
  1. **Executive Status Summary** (1 compact table or bulleted status strip showing ID, Task, Status, Key Outcome/Blocker).
  2. **Deliverables by Task** (`### T1: ...`, `### T2: ...`) in logical or user-requested order—keep unrelated tasks cleanly bounded.
  3. **Assumptions & Verification Notes** (exact checks run vs. static checks, plus assumptions made).
  4. **Blockers & Next Actions** *(omit if 100% done)* — exact actionable steps or targeted questions to resolve any `blocked`/`failed` task.

---

## 6. Operational Templates & Checklists

### Template A: Standard Task Ledger (Use Internally or Display for Tier 3)
```markdown
| ID | Task Description | Wave | Status | Depends On | Resource Lock | Outcome / Anchor |
|----|------------------|------|--------|------------|---------------|------------------|
| T1 | [Atomic action]  | 1    | done   | -          | read-only     | Found root cause at `auth.py:84` |
| T2 | [Atomic action]  | 1    | active | -          | read-only     | Pulling docs |
| T3 | [Atomic action]  | 2    | queued | T1         | `auth.py`     | Pending Wave 2 |
| T4 | [Atomic action]  | 3    | queued | T3         | tests         | Pending Wave 3 |
```

### Template B: Sub-Agent Delegation Contract (When Spawning Workers)
```markdown
**Worker Assignment — [Task ID: T_n]**
- **Goal:** [Single crisp sentence]
- **Scope / Files Allowed:** [Exact paths or URLs]
- **Out of Bounds:** Do NOT modify [files] or refactor unrelated modules.
- **Mode:** [Read-Only Analysis | Write-Owner of path/to/file]
- **Constraints:** [Language, conventions, constraints]
- **Return Format:** Return (1) Verdict/Summary <= 10 bullets, (2) Exact file:line citations, (3) Any blockers encountered.
```

### Template C: Interruption Checkpoint Card
```markdown
**Scope Shift Detected — Re-Orchestrating**
- **Preserved (`done`):** T1, T2
- **Frozen (`paused`):** T3 (70% drafted; safe to resume)
- **Modified / Invalidated:** T4 (constraint updated per new spec)
- **Cancelled (`skipped`):** T5
- **New Urgent Insertion (`Preempt`):** T6 -> Running in immediate next wave before resuming T3/T4.
```

---

## 7. Detailed End-to-End Walkthroughs

Study these three full-scale scenarios to see exact orchestration mechanics—from intake and parallel tool choreography to fault isolation, interruption management, and final delivery.

---

### Walkthrough A: Multi-Track Software Engineering, Tool Batching & Fault Recovery

#### User Prompt
> "Our checkout flow is throwing duplicate charge errors under load (`src/billing/charge.ts`), and users say password resets expire instantly (`src/auth/reset.ts`). Audit both, fix whichever bugs you find, add regression tests for both, check `package.json` for outdated security-critical dependencies, and update `CHANGELOG.md` with the fixes."

#### Phase 1: `task-decomposer` (Internal Breakdown)
- `T1`: Read and audit `src/billing/charge.ts` (+ callers/tests) for duplicate-charge race condition. *(Acceptance: exact root cause identified).*
- `T2`: Read and audit `src/auth/reset.ts` (+ config/tests) for instant token expiration bug. *(Acceptance: exact root cause identified).*
- `T3`: Inspect `package.json` (and lockfile/audit if needed) for security-critical dependencies. *(Acceptance: actionable vulnerability/outdated report).*
- `T4`: Fix bug in `src/billing/charge.ts`. *(Depends on `T1`; `LOCK: src/billing/charge.ts`).*
- `T5`: Fix bug in `src/auth/reset.ts`. *(Depends on `T2`; `LOCK: src/auth/reset.ts`).*
- `T6`: Write regression test for duplicate charge fix. *(Depends on `T4`, existing billing test conventions).*
- `T7`: Write regression test for password reset expiration fix. *(Depends on `T5`, existing auth test conventions).*
- `T8`: Run test suite to verify `T4..T7`. *(Depends on `T6`, `T7`).*
- `T9`: Update `CHANGELOG.md` with verified fixes. *(Depends on `T8` passing so changelog only records verified fixes; `LOCK: CHANGELOG.md`).*

*(Implied discovery tasks merged cleanly into Wave 1 reads: read existing test files + `CHANGELOG.md` format upfront!)*

#### Phase 2 & 3: `dependency-dag-planner` + `priority-triage`
- **Wave 1 (Parallel Discovery — Read-Only Batch):** `T1` reads, `T2` reads, `T3` (`package.json`), plus read existing billing/auth test files and `CHANGELOG.md` format.
  - *Triage priority:* All Wave 1 reads run together in 1 turn; `T3` security audit can even run `npm audit` alongside reads if safe.
- **Wave 2 (Parallel Fixes — Distinct File Locks):** `T4` (`src/billing/charge.ts`) + `T5` (`src/auth/reset.ts`) — safe in parallel because file locks are disjoint!
- **Wave 3 (Parallel Test Authoring):** `T6` (billing test file) + `T7` (auth test file) — disjoint locks.
- **Wave 4 (Unified Verification):** `T8` (execute test suite) + finish `T3` synthesis.
- **Wave 5 (Final Mutation):** `T9` (`CHANGELOG.md`, conditioned on `T8` pass).

#### Phase 4: `parallel-executor` & `context-ledger` in Action

**Turn 1 — Wave 1 Parallel Discovery Batch (6 independent read calls in 1 turn):**
```text
[Batch Tool Calls]
1. read_file("src/billing/charge.ts")
2. read_file("src/auth/reset.ts")
3. read_file("package.json")
4. glob("tests/**/*.test.ts")
5. read_file("CHANGELOG.md")
6. run_command("npm audit --json")   # Read-only diagnostic for T3
```
*(Avoided 6 wasted sequential turns!)*

**Context Ledger Checkpoint after Wave 1 (Compressed):**
- `[T1]` `src/billing/charge.ts:42-68`: Missing idempotency key check before calling payment gateway; concurrent requests both pass `if (!order.paid)` before DB commit (`READ` -> `CHARGE` -> `MARK_PAID` race).
- `[T2]` `src/auth/reset.ts:19`: `expiresAt = Date.now() + RESET_TTL_SECONDS` instead of `* 1000` (milliseconds vs. seconds bug -> expires in ~0.9 seconds!).
- `[T3]` `package.json` + `npm audit`: `jsonwebtoken@8.5.1` (known critical CVE; upgrade to `^9.0.0`), `axios@0.21.1` (SSRF advisory; upgrade to `^1.6.0`).
- `[SHARED]` Tests live in `tests/billing.test.ts` and `tests/auth.test.ts` using `vitest`.

**Turn 2 — Wave 1.5 Read Missing Test Conventions (2 parallel reads):**
```text
[Batch Tool Calls]
1. read_file("tests/billing.test.ts")
2. read_file("tests/auth.test.ts")
```

**Turn 3 — Wave 2 Parallel Fixes (`T4` + `T5`) + Wave 3 Tests (`T6` + `T7`):**
Since `T4`, `T5`, `T6`, and `T7` touch **4 distinct files** and we already read all 4 files cleanly, issue edits cleanly:
```text
[Batch Tool Calls — Disjoint File Locks]
1. edit_file("src/billing/charge.ts", ...)   # T4: Add idempotency lock / atomic state transition
2. edit_file("src/auth/reset.ts", ...)       # T5: Multiply RESET_TTL_SECONDS * 1000
3. edit_file("tests/billing.test.ts", ...)   # T6: Add concurrent Promise.all double-charge test
4. edit_file("tests/auth.test.ts", ...)      # T7: Add reset token validity window test
```

**Turn 4 — Wave 4 Verification (`T8`):**
```text
[Tool Call]
1. run_command("npx vitest run tests/billing.test.ts tests/auth.test.ts")
```

#### Phase 5B: Simulated Fault & `fault-recovery` Trigger!
Suppose `vitest` outputs:
- `tests/auth.test.ts`: **PASS (4/4)** -> `T5` & `T7` verified `done`!
- `tests/billing.test.ts`: **FAIL** -> `TypeError: db.acquireLock is not a function` in mock DB used by `tests/billing.test.ts`.

**Recovery Action (No panic, no touching healthy `auth` track):**
1. **Isolate:** `T5` & `T7` remain `done`. Only `T4`/`T6` (and downstream `T8`/`T9`) are affected.
2. **Diagnose (Root Cause, Not Blind Retry):** Our fix in `src/billing/charge.ts` called `db.acquireLock()`, which exists in production DB adapter (`src/db/client.ts`) or maybe doesn't exist at all—let's inspect `src/db/client.ts` and the test mock!
3. **Targeted Read:**
   ```text
   read_file("src/db/client.ts")
   ```
   Discovery: `db` uses `db.transaction(...)` with conditional `UPDATE orders SET status='processing' WHERE id=? AND status='pending' RETURNING *`, NOT `acquireLock`.
4. **Targeted Repair (`T4` + `T6`):** Update `src/billing/charge.ts` to use atomic conditional update (no new mock method needed, works identically in real DB and existing test mock!). Update `tests/billing.test.ts` mock state behavior if needed.
5. **Re-Verify (`T8`):**
   ```text
   run_command("npx vitest run tests/billing.test.ts tests/auth.test.ts")
   -> PASS (9/9)
   ```

**Turn 6 — Wave 5 (`T9`):**
`T8` passed -> Update `CHANGELOG.md` accurately with both verified fixes (never including unrequested `package.json` edits since user asked to *check* dependencies, not mutate `package.json`).

#### Phase 6: `verify-and-synthesize` Audit & Final User Output
*Audit Check:*
- `T1` Billing audit? Done.
- `T2` Auth audit? Done.
- `T3` Dependency audit? Done (reported only; did not unexpectedly upgrade breaking `jsonwebtoken` major version without approval!).
- `T4` & `T5` Fixes? Done.
- `T6`, `T7`, `T8` Regression tests written & passing? Done (9/9 observed passing).
- `T9` `CHANGELOG.md` updated? Done.

**Final Response Delivered to User:**
> ### Status Overview
> | ID | Task | Status | Summary |
> |----|------|--------|---------|
> | T1 / T4 / T6 | Billing duplicate charge audit, fix & test | **Done** | Fixed check-then-act race via atomic conditional status transition; regression test passes. |
> | T2 / T5 / T7 | Password reset instant expiry audit, fix & test | **Done** | Fixed seconds-vs-milliseconds mismatch (`* 1000`); regression test passes. |
> | T3 | Security dependency check (`package.json`) | **Done** | Flagged critical upgrades for `jsonwebtoken` and `axios` (no files altered). |
> | T8 / T9 | Verification & `CHANGELOG.md` | **Done** | 9/9 tests passed (`vitest`); changelog updated.
>
> ### T1, T4 & T6: Duplicate Charge Race Condition (`src/billing/charge.ts`)
> - **Root Cause:** Concurrent requests could both pass `if (!order.paid)` before either marked the order paid, resulting in two gateway calls.
> - **Fix:** Replaced the non-atomic check with an atomic state transition (`pending -> processing`) inside `db.transaction(...)` before invoking the payment provider, and ensured failures roll back or record idempotency status cleanly.
> - **Test Added (`tests/billing.test.ts`):** Simulates two concurrent `Promise.all` checkout calls for the same order ID and asserts the payment provider is called exactly once.
>
> ### T2, T5 & T7: Instant Password Reset Expiration (`src/auth/reset.ts`)
> - **Root Cause:** Line 19 added `RESET_TTL_SECONDS` (`900`) directly to `Date.now()` (milliseconds), making tokens expire in `0.9s`.
> - **Fix:** Updated to `Date.now() + RESET_TTL_SECONDS * 1000`.
> - **Test Added (`tests/auth.test.ts`):** Verifies newly issued tokens remain valid after 5 seconds and expire after 15 minutes using fake timers.
>
> ### T3: Security-Critical Outdated Dependencies (`package.json`)
> - `jsonwebtoken@8.5.1` -> Upgrade to **`^9.0.0`** (critical algorithm/key validation fixes; note breaking changes in strict key checks).
> - `axios@0.21.1` -> Upgrade to **`^1.6.0`** (SSRF & prototype pollution advisories).
> - *Left untouched pending your go-ahead since `jsonwebtoken` v9 is a major bump.*
>
> ### T8 & T9: Test Verification & Changelog
> - Executed `npx vitest run tests/billing.test.ts tests/auth.test.ts`: **9/9 tests passed**.
> - Updated `CHANGELOG.md` under `[Unreleased] -> Fixed` with both bug fixes.

---

### Walkthrough B: Mid-Flight User Interruption, Cancellation & Priority Re-Routing

#### Initial User Prompt
> "Help me launch our new Q4 Feature Pack:
> 1. Draft a 200-word launch announcement email for existing enterprise customers.
> 2. Create a 5-row comparison table (Us vs. Competitor A vs. Competitor B) highlighting SSO, Audit Logs, and Custom Webhooks.
> 3. Write a 3-tweet X/Twitter launch thread with hashtags.
> 4. Outline a 30-minute internal sales enablement call agenda."

#### Initial Decomposition & Wave 1 Progress
- `T1`: Enterprise launch email (`<= 200 words`, formal enterprise tone).
- `T2`: 5-row competitive comparison table (Us vs. Comp A vs. Comp B; features: SSO, Audit Logs, Custom Webhooks + 2 relevant baseline dimensions).
- `T3`: 3-tweet X/Twitter thread with hashtags (punchy social tone — **isolated** from `T1` formal tone!).
- `T4`: 30-minute sales enablement agenda.

Assume `T1` and `T2` are already `done` internally/in draft (Wait: suppose this is a multi-turn agentic session where Wave 1 did research on local product docs for `T2` and drafted `T1`), and the user interrupts mid-flight before final delivery:

#### Mid-Flight User Interruption
> "Wait—hold on! Legal just told us Custom Webhooks is delayed to Q1 so DO NOT mention Webhooks anywhere! Cancel the Twitter thread too (we're saving social for next month), and urgently add a short Slack blurb for our Customer Success team explaining that Webhooks slipped to Q1 and how to handle customer questions."

#### Invoking `[Sub-Skill: interruption-handler]`
1. **FREEZE:**
   - `T1` (Enterprise email): `done` -> *Needs impact check: did `T1` mention Custom Webhooks?*
   - `T2` (Comparison table): `done` -> **IMPACTED!** `T2` explicitly included Custom Webhooks.
   - `T3` (Twitter thread): `active`/`queued` -> **CANCELLED**.
   - `T4` (Sales agenda): `queued` -> *Needs impact check: ensure no Webhooks in Q4 features, optionally note Q1 timeline internally.*
2. **DIFF:**
   - `CANCEL`: `T3` -> mark `skipped`.
   - `MODIFY / INVALIDATE`: Add `[SHARED CONSTRAINT]: Exclude Custom Webhooks from Q4 launch claims; moved to Q1.` Check `T1`, `T2`, `T4` against this constraint.
   - `ADD (Urgent / Preempt)`: `T5` — Internal Customer Success Slack blurb covering Custom Webhooks Q1 slip + customer objection handling.
3. **RE-DAG & TRIAGE:**
   - **Preempt Wave:** Run `T5` (CS Slack blurb — marked urgent) + audit/patch `T1` & `T2` (replace Custom Webhooks row in `T2` with another verified Q4 strength or mark Q1/Roadmap if appropriate, or swap to Role-Based Access Control / SLA).
   - **Next Wave:** Run `T4` (Sales enablement agenda, reflecting Webhooks Q1 caveat appropriately for internal team).
   - **Dropped:** `T3` cleanly skipped.

#### Verification (`verify-and-synthesize`)
- Did Webhooks leak into `T1` (Customer email)? Checked: **0 mentions.**
- Did Webhooks appear as a Q4 feature in `T2` (Comparison table)? Checked: **Removed / replaced**, tagged `[Assumed: Replaced Webhooks row with API Rate Limits & Data Residency—adjust if you prefer another Q4 feature]`.
- Was `T3` omitted per cancellation? **Yes**, explicitly noted as `Skipped per request`.
- Is `T4` tone internal/operational while `T1` tone is external/executive and `T5` tone is crisp Slack-ready? **Yes — strict context isolation preserved.**
- Is `T1` under 200 words? Checked word count: **176 words**.

*(Agent delivers clean **Scope-Shift Confirmation + Task Status Strip + T5 (Urgent) + T1 + T2 + T4** without re-asking redundant questions or losing `T1`/`T4`.)*

---

### Walkthrough C: Mixed-Domain Work with Ambiguity, Missing Data & Partial Delivery

#### User Prompt
> "Prepare for tomorrow's vendor review:
> 1. Summarize our current cloud spend from `finance/aws-oct.csv`.
> 2. Calculate projected annual savings if we switch 40% of on-demand EC2 instances to 1-year Savings Plans (assume 28% discount on that portion).
> 3. Pull the latest SLA terms from `legal/vendor-sla-2026.pdf` and flag any uptime penalty gaps below 99.95%.
> 4. Draft a negotiation email to our AWS account rep asking for the discount and tighter SLA credits.
> 5. Schedule the follow-up calendar invite with the CFO for Thursday at 10 AM."

#### Phase 1–3: `task-decomposer` + `dependency-dag-planner` + `priority-triage`
- `T1`: Inspect & summarize `finance/aws-oct.csv`. (`independent`, Wave 1)
- `T2`: Calculate projected annual savings (`40% * EC2_spend * 12 * 28%`). (`DATA` depends on `T1`, Wave 2)
- `T3`: Read `legal/vendor-sla-2026.pdf` and check vs. `99.95%` threshold. (`independent`, Wave 1)
- `T4`: Draft AWS negotiation email incorporating savings ask (`T2`) and SLA gap (`T3`). (`DATA` depends on `T2` + `T3`, Wave 3)
- `T5`: Calendar invite to CFO for Thursday 10 AM. (`independent`, Wave 1 — **Check capability/ambiguity early!** Do we even have a calendar tool or CFO's email/timezone? And sending external/calendar invites is an external action!)

#### Phase 4: Wave 1 Parallel Discovery + Capability Probe
```text
[Batch Tool Calls]
1. read_file("finance/aws-oct.csv")
2. read_file("legal/vendor-sla-2026.pdf")
3. list_available_tools / inspect environment (Check if Calendar tool exists)
```

Suppose Wave 1 returns:
- `finance/aws-oct.csv`: **Success!**
  - Total Oct spend: `$50,000`
  - On-Demand EC2 line item: `$30,000/mo` (Remaining `$20,000` is RDS/S3/Data Transfer)
- `legal/vendor-sla-2026.pdf`: **FAILURE (`FileNotFoundError`)**!
  - Let's invoke `fault-recovery`: Don't abort! Maybe filename is slightly different. Run fast `glob("legal/*sla*")` or `glob("legal/*")`.
  - Suppose `glob("legal/*")` returns empty or only `legal/nda-template.docx`—the vendor SLA PDF genuinely does not exist in the workspace!
- Calendar capability check: **No calendar integration tool available** (and CFO email + timezone unspecified).

#### Phase 5B: `fault-recovery` — Blast-Radius Containment in Action!
Let's trace what stays alive vs. what gets contained:
- `T1` (Cloud spend summary): **UNBLOCKED** -> Complete fully!
- `T2` (Savings calculation): **UNBLOCKED** (only depended on `T1`!) -> Complete accurately!
  - Math check:
    - On-Demand EC2 = `$30,000/mo` -> `$360,000/yr` *(Notice: NOT 40% of total `$50k` AWS spend—only the EC2 on-demand portion! Careful scope adherence!)*
    - Covered 40% portion = `$30,000 * 0.40 = $12,000/mo` (`$144,000/yr`)
    - 28% Savings Plan discount = `$144,000 * 0.28 = $40,320/yr` (`$3,360/mo` saved)
    - *(Clearly distinguish EC2 base vs. Total AWS spend!)*
- `T3` (Vendor SLA review): **BLOCKED (`Missing file: legal/vendor-sla-2026.pdf`)**.
- `T4` (Negotiation email): **PARTIALLY UNBLOCKED!** `T4` depends on `T2` (available!) and `T3` (missing!). Instead of failing `T4` entirely, apply **Graceful Degradation**: draft the complete email with exact `T2` Savings Plan numbers and include a crisp bracketed placeholder `[INSERT SPECIFIC SLA GAP FROM vendor-sla-2026.pdf — e.g., current X% tier vs. requested 99.95% threshold]` so the user has a 90%-ready draft immediately!
- `T5` (Calendar invite): **BLOCKED (`No calendar tool & missing CFO email/timezone`)** -> Provide a ready-to-paste ICS / calendar invite block + ask for details if needed, rather than hallucinating that an invite was sent!

#### Phase 6: Final Output Delivered to User
> ### Vendor Review Prep — Status Summary
> | ID | Task | Status | Notes |
> |----|------|--------|-------|
> | T1 | Summarize `finance/aws-oct.csv` | **Done** | $50,000 total ($30,000 On-Demand EC2). |
> | T2 | Compute 1-yr Savings Plan projection | **Done** | **$40,320/year** ($3,360/mo) estimated savings. |
> | T3 | Review `legal/vendor-sla-2026.pdf` | **Blocked** | File not found in `legal/` (checked directory). |
> | T4 | Draft AWS negotiation email | **Done (Partial)** | Includes exact T2 numbers + highlighted `[SLA GAP]` placeholder awaiting T3. |
> | T5 | Schedule CFO follow-up (Thu 10 AM) | **Blocked** | No calendar integration available + missing CFO email/timezone. Provided copy-paste invite details. |
>
> ### T1: October AWS Spend Summary (`finance/aws-oct.csv`)
> - **Total Spend:** `$50,000.00`
> - **On-Demand EC2:** `$30,000.00` (60.0%)
> - **Other Services (RDS, S3, Data Transfer):** `$20,000.00` (40.0%)
>
> ### T2: Savings Plan Projection
> - **Eligible On-Demand EC2 Base:** `$30,000/mo` (`$360,000/yr`)
> - **40% Commitment Coverage:** `$12,000/mo` (`$144,000/yr`)
> - **Projected Savings at 28% Discount:** **`$3,360/mo`** or **`$40,320/year`**
> - *(Note: Applied strictly to the `$30,000/mo` On-Demand EC2 portion per your prompt, excluding non-EC2 spend.)*
>
> ### T3: Vendor SLA Review — Blocked
> - Attempted to read `legal/vendor-sla-2026.pdf` and scanned `legal/`—only `legal/nda-template.docx` is present. Upload or provide the path to the SLA PDF and I will immediately extract the credit tiers below 99.95%.
>
> ### T4: Draft Negotiation Email to AWS Rep
> *(Complete draft ready to send once the bracketed SLA detail from T3 is dropped in)*
> ...
>
> ### T5: CFO Calendar Invite — Action Required
> - I do not have calendar access in this environment, and your CFO's email and timezone weren't specified. Here is a ready-to-paste invite summary for **Thursday at 10:00 AM**:
>   - **Title:** AWS Vendor Review & Savings Plan Approval (`~$40.3k/yr savings`)
>   - **Agenda:** Review Oct spend (`$50k`), approve 40% EC2 1-yr Savings Plan, finalize SLA gap negotiation ask.

---

## 8. Anti-Patterns & Diagnostic Reference

If you catch yourself exhibiting any of these behaviors during execution, immediately invoke the corrective sub-skill:

| Anti-Pattern | Symptom | Root Cause | Immediate Correction |
|---|---|---|---|
| **Waterfall Drip** | Calling 1 read tool per turn across 6 turns for files already named in prompt. | Ignored Wave 1 batching. | Invoke `parallel-executor`; bundle all independent reads now. |
| **Hallucinated Completion** | Claiming "Tests pass" or "Checked the file" without having executed/read it. | Skipped `VERIFY` step in `verify-and-synthesize`. | Run actual verification tool, or honestly label as static inspection / unverified. |
| **All-or-Nothing Collapse** | Stopping the whole response to ask a clarifying question on Task 4 when Tasks 1–3 are completely clear. | Failed blast-radius isolation. | Invoke `fault-recovery`; execute Tasks 1–3 now, pause only Task 4. |
| **Cross-Task Bleed** | Writing formal legal prose in a casual Slack blurb because the previous task was a legal memo. | Missing `[T_n]` namespace boundaries. | Invoke `context-ledger`; explicitly re-read target task's local constraints before drafting. |
| **Silent Truncation** | Answering 4 of 5 user items and ending with a generic summary. | Missing intake ID assignment & post-flight audit. | Invoke `task-decomposer` + `verify-and-synthesize`; explicitly reconcile every ID. |
| **Rabbit-Hole Looping** | Spending 6 turns tweaking CSS or fighting one flaky mock while core tasks haven't started. | Missing `time-budget-governor`. | Park flaky secondary item, finish high-impact tasks first, return with remaining budget. |
| **Duplicate / Blind Retries** | Running the exact same failing shell command 3 times in a row. | Violated smart retry ladder. | Stop; inspect exact error stderr + environment state before issuing an adapted call. |
| **Over-Orchestration Bloat** | Printing a 20-row DAG table for "Give me 3 title ideas and fix this 2-line SQL query." | Violated Complexity Tiering (Section 3). | Downgrade to Tier 1; batch silently and deliver crisp, direct answers. |
