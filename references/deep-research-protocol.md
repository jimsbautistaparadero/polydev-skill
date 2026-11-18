# Deep Research and Literature Discovery Protocol

## Purpose

Produce a transparent, repeatable evidence search that is deep enough for the study's purpose. The objective is not to collect the largest number of citations. It is to find, verify, compare, and synthesize the evidence needed to justify the problem, gap, framework, methods, and design decisions.

## 1. Decompose the study into researchable concepts

Start from the draft research questions and claims. For each, list:

- Core concept and synonyms.
- Alternate terminology used by different disciplines.
- Related constructs and controlled vocabulary where relevant.
- Target population, context, and geography.
- Intervention/system/process, if applicable.
- Outcomes, evaluation criteria, or dependent variables.
- Likely study designs and source types.

Build a concept table before searching. Avoid searching only the proposed project title; this tends to retrieve near-duplicate systems and miss theory, methods, and contrary findings.

## 2. Search in deliberate passes

### Pass A — Orientation and terminology

Find authoritative overviews, review papers, handbooks, and domain standards. Use them to discover terminology, seminal authors, common methods, and relevant databases. Do not rely on overview pages for detailed empirical claims.

### Pass B — Foundational theory and seminal research

Identify original theory papers, foundational models, validated instruments, seminal empirical studies, and the earliest influential work where historically relevant. Explain why older literature remains foundational rather than treating age alone as quality.

### Pass C — Recent empirical evidence

Search a recent window appropriate to the field and topic. A default 5–10-year window can be a starting point, not an absolute rule. Retain older sources when they establish theory, methods, standards, or historical context. Include very recent papers only after verifying publication status and metadata.

### Pass D — Local, regional, and population context

Search for studies and official statistics relevant to the actual jurisdiction, population, sector, organization, language, or deployment environment. Do not assume global findings generalize to a local setting.

### Pass E — Methods and measurement

Search for methodological sources, sampling approaches, analysis methods, instrument validation studies, and comparable evaluation protocols. Prefer original validation papers and authoritative method references.

### Pass F — Comparable interventions or systems

Search beyond identical product names. Compare workflows, user groups, data structures, deployment environments, governance, accessibility, and evaluation criteria. Include unsuccessful or limited implementations where available.

### Pass G — Contradictory evidence and boundary conditions

Deliberately search for null results, critical evaluations, unintended effects, security failures, usability barriers, or evidence that weakens the proposed rationale. Do not construct a one-sided literature review.

## 3. Search venues by domain

Choose venues based on the subject, not by prestige alone.

- Computing and information systems: IEEE Xplore, ACM Digital Library, Scopus/Web of Science where available, SpringerLink, ScienceDirect, arXiv for preprints (clearly labeled), institutional repositories, standards bodies.
- Education: ERIC, education journals, government education datasets, institutional repositories.
- Health: PubMed/MEDLINE, Cochrane Library where relevant, clinical guidelines, public-health agencies.
- Social sciences and public administration: discipline-specific journals, government repositories, policy research institutes, official statistical agencies.
- Cross-disciplinary discovery: Google Scholar, OpenAlex, Crossref, Semantic Scholar, DOAJ, CORE, university repositories.
- Law, policy, and regulation: official legislation databases, courts, government agencies, regulators, and authoritative legal commentary.

These are candidate venues, not a claim that every source is indexed or peer-reviewed. Record exactly where each source was found and verify the publication venue separately.

## 4. Construct search strings

Use Boolean operators and phrase searching. Adapt syntax to each database.

Example pattern:

`("community incident reporting" OR "citizen report*" OR "public service request*") AND ("information system" OR platform OR application) AND (usability OR adoption OR response time OR evaluation)`

For each query, record:

- Exact query string.
- Database or website.
- Search date.
- Year/language/document filters.
- Result count when shown.
- Screening status and notes.

Do not claim an exact result count if the database did not expose one.

## 5. Screening rules

Write inclusion/exclusion criteria before screening where practical. Typical criteria include:

- Direct relevance to the research question or a defined construct.
- Clear publication identity and accessible metadata.
- Appropriate source type for the claim being made.
- Study context, population, and method sufficiently described.
- Publication date within the selected window, except justified foundational sources.
- Language and full-text availability constraints, disclosed explicitly.

Exclude or downgrade sources with unverifiable authorship, unclear publication venue, promotional bias, missing methods, irrelevant context, duplicate records, or unsupported claims. Never exclude a source merely because its results disagree with the expected outcome.

## 6. Snowballing

Use backward citation searching (references cited by a relevant source) and forward citation searching (later sources citing it). Record the seed source and direction. Snowballing supplements database searches; it does not replace a documented search strategy.

## 7. Source extraction

For every included source, extract only information actually present in the source:

- Verified bibliographic identity.
- Research purpose/questions.
- Theory/framework.
- Context, population, sample, and period.
- Design and data sources.
- Instrument/procedure.
- Analysis method.
- Findings, including direction and uncertainty if reported.
- Author-stated limitations.
- Additional limitations noticed by the reviewer, clearly distinguished from author-stated limitations.
- Relevance to the current study.
- Evidence location (page, section, table, figure, DOI/URL).
- Full-text, abstract-only, or metadata-only access status.

If a detail is not reported, enter `not reported`; do not infer it.

## 8. Synthesis method

Organize the synthesis by themes or research questions, not source-by-source summaries. For each theme:

1. State the theme precisely.
2. Compare converging findings.
3. Explain differences in population, setting, method, definitions, or measurement.
4. Identify contradictory or null results.
5. Assess methodological strengths and limitations.
6. Explain what the evidence supports and what remains uncertain.
7. Link the theme to the current study's framework, method, or scope.

Use a synthesis matrix and evidence map. Avoid counting papers as if every study contributes equally; assess relevance and quality.

## 9. Gap development

A candidate gap must be specific and evidence-backed. Possible forms:

- **Empirical gap:** an outcome or relationship remains insufficiently examined.
- **Context gap:** existing results come from materially different institutional, geographic, cultural, or operational settings.
- **Population gap:** a relevant population is underrepresented.
- **Method gap:** existing methods cannot answer a specific question or have recurring limitations.
- **Theory gap:** theories or constructs are inconsistent, incomplete, or insufficiently tested.
- **Implementation gap:** known recommendations are not translated into practice or systems.
- **Evaluation gap:** proposed systems or interventions are reported without adequate evaluation.

A context gap alone may justify local evaluation or adaptation, but it does not automatically prove a globally novel contribution. State the boundary of the search and the precise basis for the gap.

## 10. Expected research outputs

At the end of deep research, produce:

- Search protocol and search log.
- Screening criteria and included/excluded records where feasible.
- Verified bibliography.
- Evidence matrix.
- Theme-by-theme synthesis.
- Research gap statement with supporting and limiting evidence.
- Concept/theory map.
- Implications for research questions, method, and system requirements.
- Search limitations and unresolved questions.

## 11. Search stop rules

Do not stop merely because several similar papers have been found. Stop when the planned search passes are completed, all research questions have sufficient evidence coverage, key seminal and recent sources are identified, contradictory evidence has been considered, citation chasing yields diminishing returns, and the remaining gaps are documented. For a formal systematic or scoping review, follow the protocol and reporting standard appropriate to that review rather than this informal stopping rule.
