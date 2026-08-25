
# Open-Source Analysis Lab (OSAL)

A curated, scored registry of in-country and expert open sources for regional and country analysis.
Every source is rated 1–5 on seven criteria so an analyst can judge quickly what it is worth.

**4,800+ sources across 195 countries** in nine regions — Asia, Caribbean, Eurasia, Europe, North &
Central America, North Africa & Middle East, Oceania, South America, and Sub-Saharan Africa. The United States is omitted from this dataset at this time. **382** of the sources are flagged as quantitative
datasets.

## The scoring rubric

Each source is scored 1–5 on seven independent criteria; the **composite** is their mean.

| Criterion | What it measures |
|---|---|
| Accuracy | How reliably its factual claims hold up against later confirmation |
| Uniqueness | How much it tells you that you could not get elsewhere |
| Timeliness | How quickly it publishes relative to events |
| Transparency | How openly it discloses funding, ownership, methods, and orientation |
| Verifiability | Whether it shows its evidence and cites primary sources |
| Accessibility | Practical usability: paywall, language, exportability |
| Analytical depth | Rigor and originality of interpretation |

Descriptive labels (not scored): **source type**, **perspective** (Independent, Independent (exile/external),
State media, State / official, Establishment, Pro-government, etc.), **language**, **channel**
(Website vs Social media) with **platform**, and a **dataset** flag for quantitative sources.

Full details are in `methodology.qmd`.

## Repository structure

```
_quarto.yml                        project + site config (navbar, sidebars)
index.qmd                          home — alphabetical country index with source/dataset counts
methodology.qmd                    scoring rubric + inclusion criteria
styles.scss                        house stylesheet (JMU theme)
data/sources.csv                   the single data backbone (every page reads from it)
tools/recompute.py                 recomputes the composite column
regions/<region>/<country>/        per-country pages
  index.qmd                        country overview (all-topic filterable table)
global/index.qmd                   cross-country shelf (placeholder)
preview/osal-preview.html          standalone visual preview (no build needed)
.github/workflows/publish.yml      GitHub Pages deploy workflow
```

Regions map to folders: `Eurasia → eurasia`, `Europe → europe`, `North Africa & Middle East → mena`,
`Asia → asia`, `Sub-Saharan Africa → sub-saharan-africa`, `South America → south-america`,
`North & Central America → north-central-america`, `Caribbean → caribbean`, `Oceania → oceania`.

## The data file

| Column | Notes |
|---|---|
| region, country, topic | topic ∈ Security / Economic / Political / Societal / General |
| name, url, language | language is free text, e.g. `RU/EN` |
| source_type | what it is (outlet, pollster, think tank, official…) |
| perspective | disclosure label, not a quality rating |
| channel, platform | `Website` or `Social media`; platform e.g. `Telegram`, `Substack` |
| is_dataset | `yes` marks a quantitative source (surfaces on the Datasets page) |
| accuracy, uniqueness, timeliness, transparency, verifiability, accessibility, depth | integers 1–5 |
| composite | mean of the seven (run `python tools/recompute.py` to regenerate) |
| notes | one-line analyst note (shown under the source name) |

To add a country, add rows to the CSV, then generate its pages (copy an existing country's six `.qmd`
files, or regenerate) and add it to the navbar/sidebar in `_quarto.yml`.


## A note on the scores

Scores are analyst judgments, not measurements — defensible and revisable. Outlets change ownership, get
shut down, relocate, or drift; a score should move when the underlying reality does. Treat the registry
as a living document.

=======
# OSAL
Open-Source Analytics Laboratory @ JMU

