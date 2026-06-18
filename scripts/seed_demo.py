"""Populate the database with a deterministic demo dataset.

The seeded articles are synthetic (no network access) and recent (within the
48h recency window used by the ranker), so a recruiter can clone the repo,
run this script and see a populated briefing without hitting live RSS feeds.

Usage:
    python scripts/seed_demo.py            # add demo data (idempotent)
    python scripts/seed_demo.py --wipe     # remove demo data first, then add
    python scripts/seed_demo.py --with-demo-user  # also create/reuse a demo profile

The demo user id is printed so it can be used with scripts/test_flow.py or the
API directly. The normal frontend flow still works: a recruiter completes the
onboarding quiz (creating their own profile) and the seeded articles feed the
briefing — no ingestion required.
"""
import argparse
import hashlib
import os
import sys
from datetime import datetime, timedelta

_HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(_HERE, ".."))
sys.path.insert(0, os.path.join(_HERE, "..", "backend"))

_BACKEND_DB = os.path.abspath(os.path.join(_HERE, "..", "backend", "newsweave.db"))
os.environ.setdefault("DATABASE_URL", f"sqlite:///{_BACKEND_DB}")

from backend.app.database import SessionLocal, Base, engine
from backend.app.models.article import Article
from backend.app.models.user import User

DEMO_SOURCE_SUFFIX = " (DEMO)"
DEMO_USER_NAME = "Demo Assinante"


def _hash(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:16]


DEMO_ARTICLES: list[tuple[str, str, str, str, int]] = [
    ("economia", "InfoMoney" + DEMO_SOURCE_SUFFIX, "Bitcoin rompe barreira dos US$ 100 mil com entrada de fundos institucionais", "A capitalização do mercado de cripto atingiu novo recorde após a aprovação de ETFs spot; analistas veem ciclo alcista sustentado.", 2),
    ("economia", "Bloomberg Linea" + DEMO_SOURCE_SUFFIX, "Ethereum ganha 12% após atualização de rede reduzir taxas de transação", "O hard fork melhora a escalabilidade da camada 2 e reacende o interesse de investidores degen em altcoins.", 5),
    ("economia", "Investing.com" + DEMO_SOURCE_SUFFIX, "BC mantém Selic em 10,75% e sinaliza paciência ante incerteza fiscal", "Copom reforça que próximo passo depende de expectativas de inflação e câmbio; dólar fecha estável.", 8),
    ("economia", "InfoMoney" + DEMO_SOURCE_SUFFIX, "FII de tijolo: dividendos rendem 0,9% no mês e setor imobiliário aquece", "Fundos Imobiliários ligados a galpões logísticos lideram captação no trimestre.", 14),
    ("economia", "Bloomberg Linea" + DEMO_SOURCE_SUFFIX, "Solana lidera altcoins com alta de 30% e memecoin dispara volume", "Narrativa degen volta a movimentar o mercado de cripto após listagem em nova exchange.", 28),
    ("politica", "CNN Brasil" + DEMO_SOURCE_SUFFIX, "STF forma maioria para manter prisão de investigado por golpe", "Os ministros encerram o julgamento nesta semana; decisão tem repercussão imediata no Congresso.", 3),
    ("politica", "O Antagonista" + DEMO_SOURCE_SUFFIX, "Supremo debate limite de poderes e CPI avança em relatório", "A tensão entre Poderes domina a pauta de Brasília; mercado fiscal mantém cautela.", 9),
    ("politica", "Folha Poder" + DEMO_SOURCE_SUFFIX, "Câmara aprova arcabouço fiscal e envia para análise do Senado", "A regra de gastos cola faixa de convergência antes do aperto fiscal de 2027.", 20),
    ("tech", "Canaltech" + DEMO_SOURCE_SUFFIX, "Nova geração de modelos de IA chega: GPT e Claude disputam liderança em raciocínio", "Benchmarks de machine learning mostram saltos em matemática e programação; Gemini atualiza context window.", 1),
    ("tech", "Olhar Digital" + DEMO_SOURCE_SUFFIX, "Inteligência Artificial embarcada transforma a experiência em smartphones", "Fabricantes apostam em IA on-device para privacidade e latência; compelling use case para o consumidor.", 6),
    ("tech", "Tecnoblog" + DEMO_SOURCE_SUFFIX, "Startups de IA generativa captam US$ 2 bi em série B recordes", "Ecossistema de venture capital no Brasil acelera; novo Claude 5 chega ao mercado corporativo.", 11),
    ("tech", "Canaltech" + DEMO_SOURCE_SUFFIX, "Quebra-cabeça de chips: como a escalada da IA pressiona a cadeia de semicondutores", "GPU de última geração lidera encomendas; machine learning impulsiona capex das fábricas.", 16),
    ("tech", "Olhar Digital" + DEMO_SOURCE_SUFFIX, "Review: o smartphone com IA que traduz chamadas em tempo real", "Dispositivo aposta em inteligência artificial offline; preço fica competitivo em pré-venda.", 32),
    ("games", "IGN Brasil" + DEMO_SOURCE_SUFFIX, "Rockstar confirma trailer final de GTA VI antes do lançamento de 2026", "Rumores apontam mapa expandido nas cidades de Vice City; GTA 6 lidera wishlists globais.", 2),
    ("games", "GameSpot" + DEMO_SOURCE_SUFFIX, "CBLOL: final aposta em LoL redefine o classificatório do League of Legends", "Times prometem alta para fase final; organização traz reforço sul-americano.", 7),
    ("games", "IGN Brasil" + DEMO_SOURCE_SUFFIX, "Valorant abre vaga para torneio mundial e CS2 revela operador polêmico", "Counter-Strike prepara major; temporada de Call of Duty confirma passagem pelo Brasil.", 12),
    ("games", "GameSpot" + DEMO_SOURCE_SUFFIX, "Elden Ring ganha DLC e Baldur's Gate 3 adia sequência de RPG", "World-building premiado retorna ao hype; turn-based RPG mantém base de fãs ativa.", 18),
    ("games", "IGN Brasil" + DEMO_SOURCE_SUFFIX, "Indústria de publishers acelera M&A em jogos AA", "Fusões e aquisições reshaping no ecossistema de games; estúdios brasileiros no radar.", 36),
    ("esportes", "GE Globo" + DEMO_SOURCE_SUFFIX, "Corinthians vence clássico e Yuri Alberto balança as redes no fim", "O time entra na zona da Libertadores com a vitória em casa; Timão empolga.", 4),
    ("esportes", "GE Globo" + DEMO_SOURCE_SUFFIX, "Mosqueto: contratação do meio-campo anima torcida do Corinthians", "Garro vem para completar o passe em transições; bastidores aceleram a renovação do clube.", 10),
    ("esportes", "UOL Esporte" + DEMO_SOURCE_SUFFIX, "Tenista brasileiro João Fonseca avança e Fórmula 1 confirma GP em novo circuito", "Brasil reúne boas notícias no tênis e nacategoria; temporada de e-sports abre vagas.", 15),
    ("esportes", "UOL Esporte" + DEMO_SOURCE_SUFFIX, "Futebol: janela abre com times rivais em fase de ajuste", "Mercado da bola ainda cauteloso; Copa do Brasil chega em fase decisiva.", 22),
    ("mundo", "BBC Brasil" + DEMO_SOURCE_SUFFIX, "Conferência global discute regulação de IA e segurança de TestBed", "Países redigem marco sobre modelos de IA; tensões geoeconômicas dominam agenda.", 5),
    ("mundo", "Reuters" + DEMO_SOURCE_SUFFIX, "Mercado global atento ao petróleo e à transição energética", "Cúpula debate metas de emissões; Ásia lidera produção de chips para IA.", 13),
    ("mundo", "BBC Brasil" + DEMO_SOURCE_SUFFIX, "Eleições na Europa sinalizam virada à direita e reformas fiscais", "Bloco prepara revisão de política industrial para competir em IA e semicondutores.", 24),
    ("saude", "Veja Saúde" + DEMO_SOURCE_SUFFIX, "Ozempic e GLP-1 mantêm peso em longo prazo, aponta novo estudo de longevidade", "A perda sustentada anima o nicho de biohacking e repagina protocolos de saúde.", 6),
    ("saude", "UOL VivaBem" + DEMO_SOURCE_SUFFIX, "Rotina de biohacking: sono, cronobiologia e suplementação para longevidade", "Especialistas listam Integra de hábitos; novos suplementos prometem performance.", 17),
    ("saude", "Veja Saúde" + DEMO_SOURCE_SUFFIX, "Protocolo de nutrição focado em longevidade ganha adeptos", "Dieta flexitariana associada a menor risco cardiometabólico; estudo é amplo.", 26),
    ("saude", "Saúde Abril" + DEMO_SOURCE_SUFFIX, "Exercício físico e circadiano: como cronobiologia melhora o sono", "Pesquisadores afirmam que o bom treinamento é o remédio barato para a insônia.", 33),
    ("local_sp", "São Carlos Agora" + DEMO_SOURCE_SUFFIX, "São Carlos sedia congresso de BioTech com startups e universidades", "Cidade aposta no setor de saúde e longevidade; acordos de inovação são assinados.", 19),
    ("local_sp", "São Carlos Agora" + DEMO_SOURCE_SUFFIX, "Cultura pop toma as ruas de São Carlos com mostra de cinema", "Festival tem programação gratuita; destaque para arte, design e arquitetura local.", 40),
]


def is_demo_article(a: Article) -> bool:
    return bool(a.source and a.source.endswith(DEMO_SOURCE_SUFFIX))


def is_demo_user(u: User) -> bool:
    return u.name == DEMO_USER_NAME


def wipe_demo(db) -> tuple[int, int]:
    n_art = db.query(Article).filter(Article.source.like(f"%{DEMO_SOURCE_SUFFIX}")).delete(synchronize_session=False)
    n_usr = db.query(User).filter(User.name == DEMO_USER_NAME).delete(synchronize_session=False)
    db.commit()
    return n_art, n_usr


def seed_articles(db) -> int:
    now = datetime.now()
    added = 0
    for category, source, title, summary, hours_ago in DEMO_ARTICLES:
        link = f"https://demo.newsweave.local/{category}/{_hash(title)}.html"
        if db.query(Article).filter(Article.link == link).first():
            continue
        published = now - timedelta(hours=hours_ago)
        db.add(Article(
            title=title,
            link=link,
            source=source,
            summary=summary,
            category=category,
            published_at=published,
            content_hash=_hash(title + summary[:200]),
        ))
        added += 1
    db.commit()
    return added


def seed_demo_user(db) -> int:
    existing = db.query(User).filter(User.name == DEMO_USER_NAME).first()
    if existing:
        return existing.id
    demo = User(
        name=DEMO_USER_NAME,
        location="São Carlos",
        football_team="Corinthians",
        follow_football=True,
        follow_tennis=True,
        follow_formula1=True,
        follow_esports=True,
        follow_brasilia=True,
        follow_stf=True,
        follow_economy=True,
        investor_profile="moderate",
        follow_crypto=True,
        follow_stocks=True,
        follow_macro=True,
        follow_biotech=True,
        follow_reits=True,
        tech_enthusiast=True,
        follow_ai=True,
        follow_startups=True,
        follow_smartphones=True,
        follows_gta=True,
        follows_lol=True,
        follows_fps=True,
        follows_rpg=True,
        biohacker=True,
        follow_longevity=True,
        follow_nutrition=True,
        follow_fitness=True,
        tone_preference="casual",
        use_emojis=True,
        stoic_quotes=True,
        language="pt-BR",
        city="São Carlos",
        follow_local_news=True,
        follow_culture=True,
        follow_streaming=True,
    )
    db.add(demo)
    db.commit()
    db.refresh(demo)
    return demo.id


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wipe", action="store_true", help="remove demo data before seeding")
    parser.add_argument("--with-demo-user", action="store_true", help="create/reuse a demo profile and print its id")
    args = parser.parse_args()

    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if args.wipe:
            n_art, n_usr = wipe_demo(db)
            print(f"Removed demo articles: {n_art}")
            if n_usr:
                print(f"Removed demo user(s): {n_usr}")

        added = seed_articles(db)
        total = db.query(Article).filter(Article.source.like(f"%{DEMO_SOURCE_SUFFIX}")).count()
        print(f"Demo articles added: {added} (total demo articles now: {total})")

        cats = sorted({c[0] for c in db.query(Article.category).filter(Article.source.like(f"%{DEMO_SOURCE_SUFFIX}")).all() if c[0]})
        print(f"Demo categories: {', '.join(cats)}")

        if args.with_demo_user:
            uid = seed_demo_user(db)
            print(f"Demo user id: {uid}")
            print(f"Use it with: scripts/test_flow.py (set BASE) or curl http://localhost:8001/api/briefing/today?user_id={uid}")
        else:
            print("\nTip: re-run with --with-demo-user to also create a ready-to-use demo profile.")
        print("\nDemo data ready. Open the frontend, complete the onboarding quiz, and the briefing")
        print("will render from the seeded articles — no RSS ingestion required.")
    finally:
        db.close()


if __name__ == "__main__":
    main()