# Secure Software Delivery — DevSecOps Operating Model

A single-file, interactive reference model for securing a software delivery pipeline, published at
**[devsecops.cyberassure.uk](https://devsecops.cyberassure.uk/)**.

It answers three questions that usually get answered separately, and badly: *what controls does a
delivery pipeline need*, *where in the process do they actually sit*, and *which of them is the one
currently holding everything else up*.

Framework alignment: **NCSC CAF v4.0**, **GOV.UK Secure by Design** (10 principles, 10 lifecycle
stages), **OWASP ASVS / SAMM**, **GovS 007**.

---

## What's in it

Three views, each a tab:

| View | What it shows |
|---|---|
| **Operating model** | 8 security domains of the SDLC, a 39-cell toolchain plane, the 8-phase pipeline mapped to the Secure by Design stages, and 8 pipeline gates with their block/warn thresholds |
| **BPMN — pipeline process** | The same pipeline as a BPMN process model: 5 lanes, 23 shapes, 8 gateways, plus 2 pools for governance and the SOC. 9 traceable scenarios (clean run, secret blocked at push, critical CVE with no fix, and so on) |
| **Dependency model** | The pipeline as a fault tree. 6 AND branches over a shared governance spine, each node carrying an as-is and a to-be coverage-weighted effectiveness score, its owner, its state, and its monitoring metrics, KRIs and KCIs |

Every element opens a detail panel: what the control is, the control detail, the risk if it is not
implemented, and the framework references.

## Deploying it

The page is one self-contained HTML file. No build step, no dependencies, no analytics, no external
requests at runtime.

```
/
├── index.html    # the whole thing
└── og.png        # 1200×630 social preview
```

Drop both at the web root of `devsecops.cyberassure.uk` and it works. `og.png` must sit next to
`index.html` unless you change the two `og:image` / `twitter:image` URLs in `<head>` — Open Graph
images have to be absolute URLs, so unlike the favicon they can't be inlined.

Works equally well opened from `file://`, which is the easiest way to preview a change.

## Editing it

All content lives in a handful of plain JavaScript objects near the top of the `<script>` block.
Nothing is templated or generated; edit the data and reload.

| Object | Drives |
|---|---|
| `ATTRS` | The business attribute chips |
| `STAGES` | The Secure by Design lifecycle stage labels |
| `D.domains` | The 8 security domain cards |
| `D.planes` | The toolchain plane — three labelled rows of cells |
| `D.phases` | PLAN → MONITOR, the pipeline spine |
| `D.gates` | The pipeline gates and their thresholds |
| `BN` / `BE` / `BSCEN` | BPMN nodes, edges and traceable scenarios |
| `DEP` | The dependency tree: nodes, AND/OR gates, children, scores |
| `DEPM` | Per-node monitoring metrics, KRIs and KCIs |

Each element takes the same shape: `t` title, `s` subtitle, `v` colour group, `sev` severity,
`p` what it is, `c` control detail, `r` risk if absent, `refs` framework references.

Dependency nodes add `c` criticality, `own` ownership (`INT` internal, `EXT` external, `SHR`
shared), `p` as-is score, `p2` to-be score, `st` state (`live` / `partial` / `pilot` / `planned`),
and an optional `note` explaining why it scores what it does.

Colour groups are capability-based, not vendor-based: `scm`, `cicd`, `quality`, `appsec`, `dast`,
`cloud`, `inhouse`, `peer`. Adding a group means adding a `--<name>-f/-s/-t` triple to `:root`, a
`.v-<name>` rule, and an entry to the legend array.

## Two things to read it correctly

**The numbers are illustrative.** Every score, threshold and severity is an opening position drafted
to be argued with, not a measurement of any real estate. They exist so that a baselining conversation
starts from a concrete proposal rather than a blank page. Replace them with your own before quoting
them at anyone.

**Tools are named by capability.** Source control, CI/CD orchestration, code quality, SAST, SCA,
DAST, secrets management, infrastructure as code, and a public cloud platform treated as AWS, Azure
or GCP interchangeably. Vendor names appear only as illustrative examples — substitute your own.

One naming trap worth carrying over whatever your stack: at least one major vendor uses "SCA" for
its *static analyser* rather than for software composition analysis. Say which you mean.

## Accessibility and print

Interactive cells are real buttons and diagram shapes carry `role="button"` with `tabindex`, so
everything is keyboard reachable and has a visible focus ring. Opening a detail panel moves focus
to its close button and closing restores it to where you were; `Escape` closes. Diagrams carry descriptive `aria-label`s. Animated scenario
tracing honours `prefers-reduced-motion`. Printing expands every tab and detail panel so the whole
model comes out as one document.

## Provenance

Written by **Jonathan Silvester** ([LinkedIn](https://www.linkedin.com/in/jonsilvester)) and
published under the [cyberassure.uk](https://cyberassure.uk) brand.

Generic by design: it describes a pattern, not an organisation. No employer's estate, procedures,
tooling decisions or assurance position are represented here.
