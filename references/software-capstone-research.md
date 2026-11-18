# Software, Information Systems, and IT Capstone Research

## 1. Product versus research contribution

A working application is an engineering artifact. A research study must also justify why the problem matters, what is not adequately known or solved, what design knowledge or empirical evidence the project contributes, and how the artifact or intervention is evaluated.

A strong capstone can contribute through:

- A context-specific design evaluated against documented user needs.
- A tested workflow or service model.
- An adaptation of an existing approach to a materially different constraint.
- Empirical evidence about usability, adoption, accessibility, performance, or process outcomes.
- A validated prototype or design principle with stated limits.

Do not claim novelty because the exact same application name was not found.

## 2. Requirements engineering traceability

Build a traceability chain:

`Stakeholder evidence → User need → Requirement ID → Design component → Implementation → Test case → Result → Research objective`

Classify requirements as functional, usability, performance, reliability, security/privacy, accessibility, interoperability, legal/policy, operational, or maintenance-related.

Each requirement should have:

- Unique ID.
- Source/stakeholder and evidence.
- Clear statement with one primary obligation.
- Priority and rationale.
- Acceptance criterion that can be verified.
- Dependencies and constraints.
- Design/implementation reference.
- Test case and result.

Avoid vague requirements such as “the system must be user-friendly” unless broken into measurable criteria.

## 3. Architecture and implementation planning

Evaluate the design against actual conditions:

- User roles and permissions.
- Data classification and privacy.
- Authentication and session management.
- Authorization and least privilege.
- Input validation and abuse cases.
- Auditability and error handling.
- Data integrity, backup, and recovery.
- Network availability and offline/low-bandwidth needs.
- Device/browser compatibility.
- Accessibility and language.
- Deployment, maintenance, and operating cost.
- Integration constraints and data ownership.

For each architectural choice, record alternatives, trade-offs, and rationale. Do not claim a system is secure merely because it uses authentication or encryption.

## 4. Development approach

Select an iterative, incremental, plan-driven, agile, prototyping, or design-science approach based on requirement uncertainty, stakeholder availability, team capability, and institutional expectations. Describe the actual work performed. Do not name Scrum or Agile unless ceremonies, roles, planning, and iteration practices were meaningfully used.

A development method is not the same as the research method. Explain how development activities generate the artifact and how the research evaluates it.

## 5. Evaluation architecture

Choose evaluation dimensions from the study objectives and intended use.

| Dimension | Possible evidence | Example caution |
|---|---|---|
| Functional suitability | Requirements-based tests, task completion | Passing selected tests does not prove all functionality |
| Usability | Task success, time, errors, validated questionnaires, interviews | Satisfaction alone is not full usability |
| Performance | Response time, throughput, resource use under defined load | State environment, hardware, network, and workload |
| Reliability | Failure rates, recovery, repeated test runs | A short demo cannot establish long-term reliability |
| Security | Threat modeling, code review, controlled testing, configuration audit | Do not claim security certification without formal evidence |
| Accessibility | Standards-based audit and user testing | Automated checks alone are insufficient |
| Adoption/acceptance | Behavioral evidence, validated constructs, interviews | Intention to use is not actual sustained use |
| Process outcome | Before/after or comparative process data | Confounding and design limitations affect causal claims |

Define measures, instruments, test conditions, thresholds, sample, and analysis before evaluation.

## 6. Test planning

Include, as appropriate:

- Unit tests for isolated logic.
- Integration tests across components/services.
- System tests against requirements.
- User acceptance tests using defined tasks and roles.
- Compatibility tests across devices/browsers.
- Performance/load tests under stated conditions.
- Security and privacy checks, with safe authorized scope.
- Backup, restore, and failure-recovery tests.
- Accessibility checks and assistive-technology review.

For each test, define ID, objective, preconditions, test data, steps, expected result, actual result, status, evidence, tester, date, and defect reference. Never invent actual results.

## 7. User evaluation and sampling

Define eligible users and their relationship to the system. Distinguish intended users, experts, administrators, and incidental participants. Select participants according to the evaluation question and approved protocol. Avoid recruiting only developers or close friends when actual target users are needed.

If using a usability questionnaire or acceptance scale, verify source, permissions, scoring, construct coverage, and suitability for the local population. Translate/adapt carefully and document revalidation needs.

## 8. Community and public-service systems

For systems handling barangay, local-government, incident, resident, or service-request information, explicitly examine:

- Data minimization and purpose limitation.
- Role-based access and segregation of duties.
- Confidentiality of complainants and vulnerable people.
- Location and contact data exposure.
- Audit trail and accountability.
- False, abusive, duplicate, or malicious reports.
- Escalation and emergency-response boundaries.
- Retention, disclosure, and correction procedures.
- Connectivity gaps, accessibility, and digital exclusion.
- Human review and appeal/recourse.

Do not imply that a digital reporting system replaces emergency services, due process, or official response procedures. Obtain relevant permissions before using real resident or incident data.

## 9. Claims control

Use language proportional to the evaluation:

- “Implemented” when code/artifact exists.
- “Passed the specified test cases” when test evidence exists.
- “Participants rated…” when survey evidence exists.
- “Was associated with…” for supported observational associations.
- “Improved…” only when comparison design and evidence justify improvement.
- “Caused…” only when the design supports causal inference.

Document test environment and limitations so readers understand what the results do and do not establish.
