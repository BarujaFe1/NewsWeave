# NewsWeave

**Personalized news curation that turns information overload into a clear daily briefing.**

NewsWeave is a curated news product that collects articles from selected sources, normalizes and structures the data, removes redundancy, ranks stories by relevance, and delivers a personalized briefing designed to be fast, useful, and easy to scan.

The goal is not to build another generic news feed.  
The goal is to transform scattered information into a focused editorial experience tailored to the user’s interests.

---

## Why this project exists

Most people who follow the news regularly face the same problem: they spend too much time jumping between sources, too much time seeing the same story repeated, and too much time filtering noise before reaching signal.

NewsWeave was created to solve that problem with a product-oriented approach:
- the user chooses the sources;
- the user defines interests and priorities;
- the system collects the news;
- the data is cleaned and structured;
- the stories are ranked by relevance;
- the result is a personal briefing with the most useful headlines first.

This project exists both as a real product idea and as a portfolio case that demonstrates engineering maturity, product thinking, and applied data skills.

---

## What NewsWeave does

NewsWeave is designed to act as a **personal news briefing engine**.

At a high level, it will:
1. let the user configure preferred sources;
2. capture articles from those sources;
3. clean and normalize the incoming data;
4. detect duplication and near-duplicate coverage;
5. rank the items according to a user profile;
6. generate a concise briefing with the top stories;
7. preserve a history of previous briefings.

The output is not meant to feel like an infinite feed.  
It is meant to feel like a short, editorially organized briefing that helps the user understand what matters now.

---

## The problem it solves

Modern news consumption is fragmented.

A user who wants to stay informed often has to:
- open multiple websites;
- compare overlapping coverage;
- manually remove repetitive stories;
- switch between broad feeds and niche sources;
- spend more time scanning than reading.

That creates friction and weakens the quality of the reading experience.

NewsWeave addresses this by giving the user:
- control over sources;
- control over themes;
- a structured output format;
- a clearer definition of relevance;
- a faster path from raw news to useful briefing.

---

## Product thesis

NewsWeave is a product about **curation, relevance, and clarity**.

It assumes that the value is not just in collecting content, but in organizing it well enough that the user can trust the final output.

The central promise is simple:

> **Choose your sources and preferences, and receive a daily news briefing that is personalized, structured, and easy to understand.**

---

## What this project is not

To keep the scope strong and realistic, NewsWeave is **not**:

- a social network;
- a generic news portal;
- a full-scale crawler for the open web;
- a chat-based news assistant;
- an infinite-scroll feed;
- a mobile-native app in V1;
- a behavioral recommender system in the first version.

The first version is intentionally smaller so it can be finished, polished, and published.

---

## What this project aims to prove

This project is designed to demonstrate that I can build and think like a product-minded engineer.

Specifically, it should show that I can:
- turn a vague idea into a concrete product;
- define and protect an MVP scope;
- design a clean data flow;
- work with structured and semi-structured text data;
- create a meaningful ranking pipeline;
- build a backend/API that supports a real product;
- shape a user experience that feels intentional and premium;
- document a repository in a professional way;
- present a project clearly for GitHub, LinkedIn, and portfolio use.

---

## Planned capabilities

### MVP
- source selection and configuration;
- profile preferences and topic priorities;
- ingestion from a limited set of sources;
- parsing and normalization;
- duplicate detection;
- rule-based relevance ranking;
- generation of a top 10 briefing;
- additional useful headlines;
- briefing history.

### Later improvements
- source weighting controls;
- more detailed ranking explanations;
- exportable briefings;
- basic feedback loops;
- smarter topic clustering;
- richer personalization.

---

## Expected stack

### Frontend
- Next.js
- TypeScript
- Tailwind CSS

### Backend
- FastAPI
- Python
- SQLAlchemy
- Alembic

### Data
- PostgreSQL

### Ingestion and parsing
- feedparser
- trafilatura
- BeautifulSoup
- selectolax

### Supporting tools
- Docker Compose
- GitHub Actions
- Conventional Commits
- Markdown documentation

---

## Architecture overview

The architecture is intentionally simple.

```text
User preferences → API → ingestion jobs → parsing and cleaning → deduplication → ranking → briefing generation → UI
```

The core idea is to separate the system into a few clear responsibilities:
- the frontend handles experience and presentation;
- the backend handles product logic and data operations;
- the database stores sources, articles, rankings, and briefings;
- scripts handle ingestion, seed data, and operational tasks.

This keeps the project realistic, maintainable, and easy to explain.

---

## Repository structure

```text
newsweave/
├── frontend/
├── backend/
├── scripts/
├── data/
├── docs/
├── assets/
└── .github/
```

### `frontend/`
The user-facing web application.

### `backend/`
The API, ingestion logic, ranking logic, and persistent domain models.

### `scripts/`
Operational helpers, local automation, and data seeding.

### `data/`
Seed files, sample data, and demo fixtures.

### `docs/`
Product documentation, architecture, roadmap, and data model.

### `assets/`
Brand assets, screenshots, and material for presentation.

### `.github/`
Issue templates, pull request template, and CI workflows.

---

## Roadmap

### Phase 0 — Foundation
- finalize the product definition;
- create the repository structure;
- write the initial documentation;
- define the data model and API contract;
- create GitHub issues and milestones.

### Phase 1 — Technical baseline
- initialize the frontend;
- initialize the backend;
- configure PostgreSQL locally;
- create initial models and migrations;
- add the first CI checks.

### Phase 2 — Core flow
- create source management;
- define user preferences;
- ingest articles from selected sources;
- normalize and store news items;
- generate a first briefing.

### Phase 3 — Relevance and quality
- deduplicate articles;
- improve ranking rules;
- add explanation fields;
- add tests for core behavior;
- harden the ingestion flow.

### Phase 4 — Product polish
- improve the UI;
- add dark mode;
- refine spacing, typography, and hierarchy;
- add loading and empty states;
- create demo-ready screenshots.

### Phase 5 — Public release
- finalize documentation;
- prepare the public story;
- create a short demo video;
- publish the repository;
- share the project on LinkedIn and portfolio channels.

---

## Status

**Current status:** project definition and repository preparation.

At this stage, the focus is on:
- clarifying the MVP;
- locking the architecture;
- preparing the repo structure;
- writing the core documentation;
- avoiding premature implementation.

---

## What the project is meant to prove

NewsWeave is not only a functional app idea. It is a portfolio asset meant to prove that I can:

- think in product terms;
- design a sensible MVP;
- work with data pipelines;
- build and document a full-stack project;
- create a polished user experience;
- communicate technical decisions clearly;
- present a project in a way that recruiters can quickly understand.

---

## Getting started

The project will be organized to run locally with:

- Node.js for the frontend;
- Python for the backend;
- PostgreSQL for persistence;
- Docker Compose for local services.

Setup instructions will be added as implementation begins.

### Expected local workflow
```bash
