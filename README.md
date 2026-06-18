<div align="center">
  <img src="./icon.png" alt="NewsWeave Logo" width="120" height="120" />

  <h1>NewsWeave</h1>

  <p><strong>Curadoria personalizada de notícias que transforma excesso de informação em briefing diário claro</strong></p>
  <p><strong>Personalized news curation that turns information overload into a clear daily briefing</strong></p>

  <p>
    <a href="#pt-br">PT-BR</a> •
    <a href="#en">English</a> •
    <a href="#stack--tecnologias">Stack</a> •
    <a href="#arquitetura--architecture">Arquitetura</a> •
    <a href="#quick-start--início-rápido">Quick Start</a> •
    <a href="#autor--author">Autor</a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/status-MVP%20local%20demo-0f766e.svg" alt="Status MVP local demo" />
    <img src="https://img.shields.io/badge/scope-MVP%20focused-1f2937.svg" alt="MVP focused" />
    <img src="https://img.shields.io/badge/frontend-Next.js-black.svg?logo=next.js&logoColor=white" alt="Next.js" />
    <img src="https://img.shields.io/badge/backend-FastAPI-009688.svg?logo=fastapi&logoColor=white" alt="FastAPI" />
    <img src="https://img.shields.io/badge/database-SQLite-003B57.svg?logo=sqlite&logoColor=white" alt="SQLite" />
    <img src="https://img.shields.io/badge/license-MIT-111827.svg" alt="MIT License" />
  </p>

  <p>
    <a href="https://barujafe.vercel.app/"><strong>🌐 Portfólio</strong></a> •
    <a href="https://github.com/BarujaFe1"><strong>🐙 GitHub</strong></a> •
    <a href="https://www.linkedin.com/in/barujafe/"><strong>💼 LinkedIn</strong></a>
  </p>
</div>

---

<a id="pt-br"></a>

## 🇧🇷 PT-BR

## 📰 Visão geral

**NewsWeave** é um produto de curadoria personalizada de notícias criado para transformar excesso de informação em um briefing diário claro, útil e fácil de escanear.

A proposta não é criar mais um feed genérico. O objetivo é transformar informações espalhadas em uma experiência editorial focada, adaptada aos interesses e prioridades do usuário.

O sistema coleta artigos de fontes selecionadas, normaliza e estrutura os dados, remove redundâncias, ranqueia histórias por relevância e entrega um briefing personalizado com as notícias mais importantes primeiro.

> **Objetivo:** permitir que o usuário escolha fontes e preferências para receber um briefing diário estruturado, personalizado e confiável.

---

## 🎯 Problema que resolve

Quem acompanha notícias com frequência enfrenta sempre o mesmo problema: tempo demais pulando entre fontes, tempo demais vendo a mesma história repetida e tempo demais filtrando ruído antes de chegar ao sinal.

O consumo moderno de notícias é fragmentado. Um usuário que quer se manter informado muitas vezes precisa:

- abrir vários sites;
- comparar coberturas sobre o mesmo assunto;
- remover manualmente histórias repetidas;
- alternar entre fontes amplas e nichadas;
- gastar mais tempo escaneando do que lendo;
- decidir sozinho o que realmente importa.

O **NewsWeave** reduz esse atrito ao dar ao usuário:

- controle sobre fontes;
- controle sobre temas;
- formato de saída estruturado;
- definição mais clara de relevância;
- caminho mais rápido entre notícia bruta e briefing útil.

---

## 💡 Tese do produto

NewsWeave é um produto sobre **curadoria, relevância e clareza**.

Ele parte da ideia de que o valor não está apenas em coletar conteúdo, mas em organizá-lo bem o suficiente para que o usuário confie no resultado final.

A promessa central é simples:

> **Escolha suas fontes e preferências. Receba um briefing diário personalizado, estruturado e fácil de entender.**

---

## ✨ O que o NewsWeave faz

O NewsWeave foi desenhado para atuar como um **motor pessoal de briefing de notícias**.

Em alto nível, ele deve:

1. permitir que o usuário configure fontes preferidas;
2. capturar artigos dessas fontes;
3. limpar e normalizar os dados recebidos;
4. detectar duplicação e cobertura quase duplicada;
5. ranquear itens de acordo com um perfil de interesse;
6. gerar um briefing conciso com as principais histórias;
7. preservar histórico de briefings anteriores.

O resultado não deve parecer um feed infinito. Deve parecer um briefing curto, editorialmente organizado e feito para ajudar o usuário a entender o que importa agora.

---

## ✅ O que entra no MVP

A primeira versão será intencionalmente menor, para ser terminável, polida e publicável.

### MVP inclui

- Seleção e configuração de fontes.
- Preferências de perfil e prioridades de tópicos.
- Ingestão a partir de um conjunto limitado de fontes.
- Parsing e normalização de artigos.
- Detecção de duplicatas.
- Ranking de relevância baseado em regras.
- Geração de briefing top 10.
- Manchetes adicionais úteis.
- Histórico de briefings.

### MVP não inclui

- Rede social.
- Portal genérico de notícias.
- Crawler amplo para toda a web.
- Assistente de notícias baseado em chat.
- Feed infinito.
- App mobile nativo na V1.
- Sistema comportamental avançado de recomendação.
- Personalização pesada com ML na primeira versão.

---

## 🧠 O que este projeto quer provar

NewsWeave foi desenhado para demonstrar que é possível pensar e construir como um engenheiro orientado a produto.

O projeto deve mostrar capacidade de:

- transformar uma ideia vaga em produto concreto;
- definir e proteger escopo de MVP;
- desenhar um fluxo de dados limpo;
- trabalhar com dados textuais estruturados e semiestruturados;
- criar um pipeline de ranking significativo;
- construir backend/API que sustente um produto real;
- moldar uma experiência de usuário intencional e premium;
- documentar um repositório de forma profissional;
- apresentar o projeto com clareza para GitHub, LinkedIn e portfólio.

---

<a id="en"></a>

## 🇺🇸 English

## 📰 Overview

**NewsWeave** is a personalized news curation product created to turn information overload into a clear, useful and easy-to-scan daily briefing.

The goal is not to build another generic news feed. The goal is to transform scattered information into a focused editorial experience tailored to the user's interests and priorities.

The system collects articles from selected sources, normalizes and structures the data, removes redundancy, ranks stories by relevance and delivers a personalized briefing with the most important stories first.

> **Goal:** let users choose sources and preferences, then receive a structured, personalized and reliable daily briefing.

---

## 🎯 Problem solved

Most people who follow news regularly face the same problem: too much time jumping between sources, too much time seeing the same story repeated and too much time filtering noise before reaching signal.

Modern news consumption is fragmented. A user who wants to stay informed often has to:

- open multiple websites;
- compare overlapping coverage;
- manually remove repetitive stories;
- switch between broad feeds and niche sources;
- spend more time scanning than reading;
- decide alone what actually matters.

**NewsWeave** reduces this friction by giving the user:

- control over sources;
- control over themes;
- a structured output format;
- a clearer definition of relevance;
- a faster path from raw news to useful briefing.

---

## 💡 Product thesis

NewsWeave is a product about **curation, relevance and clarity**.

It assumes that the value is not just in collecting content, but in organizing it well enough that the user can trust the final output.

The central promise is simple:

> **Choose your sources and preferences. Receive a daily news briefing that is personalized, structured and easy to understand.**

---

## ✨ What NewsWeave does

NewsWeave is designed to act as a **personal news briefing engine**.

At a high level, it should:

1. let the user configure preferred sources;
2. capture articles from those sources;
3. clean and normalize incoming data;
4. detect duplicate and near-duplicate coverage;
5. rank items according to an interest profile;
6. generate a concise briefing with the top stories;
7. preserve a history of previous briefings.

The output is not meant to feel like an infinite feed. It is meant to feel like a short, editorially organized briefing that helps the user understand what matters now.

---

## ✅ What goes into the MVP

The first version is intentionally smaller so it can be finished, polished and published.

### MVP includes

- Source selection and configuration.
- Profile preferences and topic priorities.
- Ingestion from a limited set of sources.
- Article parsing and normalization.
- Duplicate detection.
- Rule-based relevance ranking.
- Top 10 briefing generation.
- Additional useful headlines.
- Briefing history.

### MVP does not include

- Social network.
- Generic news portal.
- Full-scale crawler for the open web.
- Chat-based news assistant.
- Infinite-scroll feed.
- Native mobile app in V1.
- Advanced behavioral recommender system.
- Heavy ML-based personalization in the first version.

---

## 🧠 What this project is meant to prove

NewsWeave is designed to demonstrate product-minded engineering.

It should show the ability to:

- turn a vague idea into a concrete product;
- define and protect an MVP scope;
- design a clean data flow;
- work with structured and semi-structured text data;
- create a meaningful ranking pipeline;
- build a backend/API that supports a real product;
- shape an intentional and premium user experience;
- document a repository professionally;
- present the project clearly for GitHub, LinkedIn and portfolio use.

---

<a id="stack--tecnologias"></a>

## 🛠️ Stack / Tecnologias

### Frontend (implementado)

- **Next.js 16** (App Router)
- **React 19**
- **TypeScript** (strict)
- **Tailwind CSS v4**
- **framer-motion**, **lucide-react**

### Backend (implementado)

- **FastAPI**
- **Python 3.12**
- **SQLAlchemy 2.0**
- **feedparser** (RSS fetching + metadata parsing)
- **python-Levenshtein** (similaridade de headline para deduplicação)
- **Pydantic v2** (schemas de request/response)

### Data (implementado)

- **SQLite** (em arquivo, auto-criado via `Base.metadata.create_all`)

### Planejado, ainda não implementado

- **PostgreSQL** como alvo de deploy (o código já abstrai a URL via `DATABASE_URL`).
- **Alembic** migrations (dependência instalada; o schema hoje sobe via `create_all`).
- **trafilatura / BeautifulSoup / selectolax** para parsing de corpo do artigo (o MVP ingere só metadados RSS + snippets de resumo).
- **Docker Compose** e **GitHub Actions** (CI) fora do escopo da demo local atual.

### Supporting tools

- **Conventional Commits**
- **Markdown documentation**

---

<a id="arquitetura--architecture"></a>

## 🏗️ Arquitetura / Architecture

The architecture is intentionally simple and explainable.

```txt
User preferences
   ↓
API
   ↓
Ingestion jobs
   ↓
Parsing and cleaning
   ↓
Deduplication
   ↓
Ranking
   ↓
Briefing generation
   ↓
UI
```

### Responsabilidades / Responsibilities

| Layer | Responsibility |
|---|---|
| Frontend | Experience, presentation, preference screens and briefing UI |
| Backend | Product logic, API, ingestion orchestration and data operations |
| Database | Sources, articles, preferences, rankings and briefings |
| Scripts | Ingestion helpers, seed data and operational tasks |
| Docs | Product decisions, architecture, roadmap and case study material |

This keeps the project realistic, maintainable and easy to explain.

---

## 🔄 Data Flow / Fluxo de dados

```txt
Selected Sources
   ↓
RSS / Article Fetching
   ↓
Parsing
   ↓
Cleaning
   ↓
Normalization
   ↓
Duplicate Detection
   ↓
Relevance Ranking
   ↓
Briefing Builder
   ↓
Dashboard / Briefing UI
```

---

## 🧬 Modelo de dados / Data model

### Entidades implementadas

- `users` — perfil local (~50 campos de preferência usados pelas regras de ranking).
- `articles` — itens ingeridos via RSS (title, link, source, summary, category, published_at, content_hash).
- `briefings` — snapshot diário persistido (top_articles, radar_bullets, stoic_quote, armazenados como JSON).

### Entidades planejadas (ainda não implementadas)

- `sources`;
- `source_categories`;
- `user_preferences` (como tabela separada);
- `topics`;
- `article_topics`;
- `briefing_items` (como tabela separada);
- `ingestion_runs` (auditoria de runs / rastreamento de falhas).

### Article fields

- title;
- source;
- author, when available;
- original URL;
- normalized URL;
- published date;
- extracted summary;
- cleaned text snippet;
- topic tags;
- duplicate group;
- relevance score;
- collected date.

### Briefing fields

- date;
- profile snapshot;
- top stories;
- additional headlines;
- ranking explanations;
- source coverage;
- generated at.

---

## 🧠 Ranking approach / Abordagem de ranking

The first version uses rule-based relevance ranking.

Signals may include:

- topic match with user preferences;
- source priority;
- recency;
- duplicate coverage count;
- keyword matches;
- article completeness;
- manual source weight;
- category priority.

The goal is not to pretend to be magical. The goal is to produce a ranking that is understandable, testable and good enough for a strong MVP.

---

## 🧹 Deduplication / Deduplicação

The MVP uses pragmatic deduplication:

- normalized URLs;
- title normalization;
- source-aware comparison;
- similarity on headlines;
- duplicate group assignment.

The goal is to reduce repeated coverage without overengineering a full semantic clustering system too early.

---

## 📁 Repository structure / Estrutura do repositório

```
newsweave/
├── backend/
│   ├── app/
│   │   ├── main.py            # FastAPI app + CORS + create_all
│   │   ├── database.py        # SQLAlchemy engine + session
│   │   ├── models/            # article.py, briefing.py, user.py
│   │   ├── routers/           # profile, ingest, briefing
│   │   └── services/          # ingestor, deduplicator, ranker, generator
│   ├── alembic/               # scaffolded (migrations pending)
│   ├── newsweave.db           # SQLite (gitignored)
│   └── requirements.txt
├── frontend/
│   ├── app/                   # routes: / , /onboarding , /briefing
│   ├── components/            # BriefingCard, QuizCard, ProgressBar, ...
│   ├── lib/                   # api.ts, profile.ts
│   ├── public/
│   └── package.json
├── data/
│   └── sources.json           # 19 feeds RSS em 8 categorias
├── scripts/
│   ├── run_ingest.ps1
│   ├── seed_sources.py
│   └── test_flow.py
├── .env.example
├── .gitignore
├── start.bat                  # sobe backend (8001) + frontend (3000) + browser
├── LICENSE
├── README.md
└── icon.png
```

Planejado (ainda não no repositório): `docs/`, `assets/`, `.github/` (CI),
`docker-compose.yml`, `CHANGELOG.md`, `CONTRIBUTING.md`, `backend/tests/` e um
`alembic.ini` com migrations reais. O README será atualizado conforme estes entrarem.

---

## 🗺️ Roadmap

### Phase 0 — Foundation &#10003; (done — definition, repo, data model draft)

- [ ] Finalize product definition.
- [ ] Create repository structure.
- [ ] Write initial documentation.
- [ ] Define data model and API contract.
- [ ] Create GitHub issues and milestones.

### Phase 1 — Technical baseline &#10003; (done — SQLite instead of PostgreSQL; migrations/CI pending)

- [ ] Initialize frontend.
- [ ] Initialize backend.
- [ ] Configure PostgreSQL locally.
- [ ] Create initial models and migrations.
- [ ] Add first CI checks.

### Phase 2 — Core flow &#10003; (working — ingest from `data/sources.json`, profile, ranking, briefing)

- [ ] Create source management.
- [ ] Define user preferences.
- [ ] Ingest articles from selected sources.
- [ ] Normalize and store news items.
- [ ] Generate first briefing.

### Phase 3 — Relevance and quality (partial — dedup + ranking rules exist; explanations/tests/ingestion hardening pending)

- [ ] Deduplicate articles.
- [ ] Improve ranking rules.
- [ ] Add explanation fields.
- [ ] Add tests for core behavior.
- [ ] Harden ingestion flow.

### Phase 4 — Product polish (partial — dark UI, loading/empty states done; screenshots pending)

- [ ] Improve UI.
- [ ] Add dark mode.
- [ ] Refine spacing, typography and hierarchy.
- [ ] Add loading and empty states.
- [ ] Create demo-ready screenshots.

### Phase 5 — Public release (in progress — repository being made public now)

- [ ] Finalize documentation.
- [ ] Prepare public story.
- [ ] Create short demo video.
- [ ] Publish repository.
- [ ] Share on LinkedIn and portfolio channels.

---

## 📌 Status

**Current status:** MVP technical implementation — local demo available.

The end-to-end loop works: a profile is created via the onboarding quiz, RSS
feeds are ingested, headlines are deduplicated and ranked against the user
preferences, and a persisted daily briefing (top headlines + radar) is rendered
in the Next.js UI.

What is in place:

- FastAPI backend with `profile`, `ingest`, `briefing` and `health` endpoints;
- SQLite persistence (auto-created via `Base.metadata.create_all`);
- Rule-based ranking + Levenshtein-based deduplication;
- Next.js 16 dark-mode briefing UI (landing, onboarding quiz, briefing).

What is next (kept out of this commit intentionally):

- Alembic migrations, automated tests, CI, Docker, public screenshots and the
  `docs/` folder described above as planned.

---

<a id="quick-start--início-rápido"></a>

## 🚀 Quick Start / Início rápido

Requirements: **Python 3.12+** and **Node.js 18+** (the repo was built with
Python 3.12.10 and Node 24). The backend uses **SQLite**, so there is no external
database to provision — the DB file is auto-created on first run.

### Option A — one command (Windows)

`start.bat` at the repo root launches the backend on port **8001** and the
frontend on port **3000**, then opens the browser:

```bat
start.bat
```

### Option B — manual (two terminals)

Backend (terminal 1):

```bash
git clone https://github.com/BarujaFe1/NewsWeave.git
cd NewsWeave/backend

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python -m uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload
```

The SQLite schema is auto-created on startup via `Base.metadata.create_all` —
no migration step is needed for the V1 local demo.

Frontend (terminal 2):

```bash
cd NewsWeave/frontend
npm install
npm run dev
```

Local access:

```txt
Frontend:  http://localhost:3000
Backend:   http://localhost:8001
API Docs:  http://localhost:8001/docs
```

Environment variables: the backend reads `DATABASE_URL` (defaults to
`sqlite:///./newsweave.db`) and the frontend reads `NEXT_PUBLIC_API_URL`
(defaults to `http://localhost:8001`). See `.env.example`.

First run: open the frontend, complete the onboarding quiz, and on the briefing
screen click **"Buscar Notícias"** to trigger RSS ingestion. The first ingestion
takes a few seconds as the configured feeds are parsed.

### Offline demo (no RSS ingestion)

To evaluate the product without hitting live RSS feeds (e.g. a cold demo on a
recruiter's machine), seed the SQLite database with a deterministic, recent
synthetic dataset:

```bash
python scripts/seed_demo.py --with-demo-user
```

This inserts ~30 articles across all 8 categories (all published within the
ranker's 48h window) and optionally creates a demo profile. After seeding,
just complete the onboarding quiz in the frontend — the briefing is generated
from the seeded articles, no ingestion required. Run `--wipe` to remove the
demo data. See `python scripts/seed_demo.py --help`.

To inspect the configured RSS feeds without ingesting, use
`python scripts/seed_sources.py`.

---

## 📸 Demo and screenshots / Demo e screenshots

The V1 should include screenshots that prove the product is real:

- onboarding or source setup;
- preference configuration;
- generated daily briefing;
- article detail;
- briefing history;
- API documentation;
- ingestion logs or pipeline status.

---

## ⚠️ Known risks / Riscos conhecidos

- Source layout changes.
- Inconsistent RSS metadata.
- Duplicate or near-duplicate stories.
- Ranking rules becoming too complex too early.
- Scope creep toward a generic news portal.
- Temptation to add chat or recommendation features before the MVP is stable.

The project strategy is to keep the MVP focused, explainable and publishable.

---

## 💼 Portfolio value / Valor para portfólio

NewsWeave is designed to work well as:

- GitHub project;
- LinkedIn post;
- portfolio case study;
- technical interview conversation;
- product thinking example;
- full-stack data pipeline example.

It demonstrates:

- product strategy;
- MVP scoping;
- data pipeline design;
- backend/API design;
- user experience;
- documentation quality.

---

## 🤝 Contributing / Contribuição

Contributions are welcome, especially around:

- ingestion reliability;
- article parsing;
- deduplication;
- ranking explanations;
- dashboard UX;
- documentation.

Recommended flow:

```bash
git checkout -b feature/your-feature
git commit -m "feat: describe your change"
git push origin feature/your-feature
```

Then open a Pull Request.

---

<a id="autor--author"></a>

## 👤 Autor / Author

Developed by **Felipe Baruja**.

- **Portfolio:** [https://barujafe.vercel.app/](https://barujafe.vercel.app/)
- **GitHub:** [github.com/BarujaFe1](https://github.com/BarujaFe1)
- **LinkedIn:** [linkedin.com/in/barujafe](https://www.linkedin.com/in/barujafe/)

---

## 📄 License / Licença

MIT License.

See [LICENSE](./LICENSE) for details.

---

<div align="center">
  <p><strong>NewsWeave</strong></p>
  <p>Scattered information in. Clear daily briefing out.</p>
  <p><em>Informação espalhada entra. Briefing diário claro sai.</em></p>
</div>
