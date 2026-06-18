"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { getBriefing, triggerIngest } from "@/lib/api";
import BriefingCard from "@/components/BriefingCard";
import TagBadge from "@/components/TagBadge";
import StoicQuote from "@/components/StoicQuote";
import SkeletonBriefing from "@/components/SkeletonBriefing";
import { Sparkles, RefreshCw, ExternalLink } from "lucide-react";

interface BriefingData {
  greeting: string;
  date: string;
  stoic_quote: string | null;
  top_15: {
    rank: number;
    title: string;
    link: string;
    summary: string;
    category: string;
    source: string;
    relevance_score: number;
  }[];
  radar: {
    title: string;
    link: string;
    category: string;
  }[];
}

export default function BriefingPage() {
  const router = useRouter();
  const [briefing, setBriefing] = useState<BriefingData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [ingesting, setIngesting] = useState(false);

  useEffect(() => {
    const userId = localStorage.getItem("newsweave_user_id");
    if (!userId) {
      router.replace("/");
      return;
    }
    loadBriefing(Number(userId));
  }, []);

  async function loadBriefing(userId: number) {
    setLoading(true);
    setError(null);
    try {
      const data = await getBriefing(userId);
      setBriefing(data);
    } catch {
      setError("Nenhum briefing disponível ainda. Clique em 'Buscar Notícias' para gerar.");
    } finally {
      setLoading(false);
    }
  }

  async function handleIngest() {
    const userId = localStorage.getItem("newsweave_user_id");
    if (!userId) return;
    setIngesting(true);
    try {
      await triggerIngest();
      await loadBriefing(Number(userId));
    } catch {
      setError("Erro ao buscar notícias. Tente novamente.");
    } finally {
      setIngesting(false);
    }
  }

  function handleReset() {
    localStorage.removeItem("newsweave_user_id");
    router.replace("/");
  }

  if (loading) return <SkeletonBriefing />;

  if (error && !briefing) {
    return (
      <div className="min-h-screen bg-[#0A0A0A] flex flex-col items-center justify-center px-6">
        <div
          className="rounded-3xl p-8 max-w-md w-full text-center"
          style={{
            background: "rgba(255, 255, 255, 0.04)",
            border: "1px solid rgba(255, 255, 255, 0.08)",
          }}
        >
          <Sparkles className="w-10 h-10 text-[#FF9F0A] mx-auto mb-4" />
          <h2 className="text-xl font-semibold text-[#F5F5F5] mb-2">Nenhum briefing ainda</h2>
          <p className="text-sm text-[#A0A0A0] mb-6">{error}</p>
          <button
            onClick={handleIngest}
            disabled={ingesting}
            className="inline-flex items-center gap-2 px-5 py-3 rounded-2xl text-sm font-semibold transition-all disabled:opacity-40"
            style={{ background: "#0A84FF", color: "#fff" }}
          >
            <RefreshCw className={`w-4 h-4 ${ingesting ? "animate-spin" : ""}`} />
            {ingesting ? "Buscando..." : "Buscar Notícias"}
          </button>
        </div>
      </div>
    );
  }

  if (!briefing) return null;

  const dateObj = new Date(briefing.date);
  const dateStr = dateObj.toLocaleDateString("pt-BR", {
    weekday: "long",
    day: "numeric",
    month: "long",
  });

  function groupRadarByCategory() {
    const b = briefing!;
    const groups: Record<string, typeof b.radar> = {};
    for (const item of b.radar) {
      const cat = item.category || "outros";
      if (!groups[cat]) groups[cat] = [];
      if (groups[cat].length < 8) groups[cat].push(item);
    }
    return groups;
  }

  return (
    <div className="min-h-screen bg-[#0A0A0A]">
      <div className="max-w-2xl mx-auto px-4 py-8">
        {/* Header */}
        <div className="mb-8">
          <div className="flex items-center justify-between mb-1">
            <h1 className="text-2xl font-bold text-[#F5F5F5]">
              ☀️ {briefing.greeting}
            </h1>
            <button
              onClick={handleReset}
              className="text-xs text-[#666] hover:text-[#A0A0A0] transition-colors"
            >
              Novo perfil
            </button>
          </div>
          <p className="text-sm text-[#A0A0A0] capitalize">{dateStr}</p>
        </div>

        {/* Stoic Quote */}
        {briefing.stoic_quote && (
          <div className="mb-8">
            <StoicQuote quote={briefing.stoic_quote} />
          </div>
        )}

        {/* Action bar */}
        <div className="flex items-center gap-3 mb-6">
          <button
            onClick={handleIngest}
            disabled={ingesting}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-medium transition-all disabled:opacity-40"
            style={{
              background: "rgba(10, 132, 255, 0.1)",
              color: "#0A84FF",
              border: "1px solid rgba(10, 132, 255, 0.2)",
            }}
          >
            <RefreshCw className={`w-3.5 h-3.5 ${ingesting ? "animate-spin" : ""}`} />
            {ingesting ? "Atualizando..." : "Atualizar notícias"}
          </button>
        </div>

        {/* Top 15 */}
        <section className="mb-10">
          <h2 className="text-lg font-semibold text-[#F5F5F5] mb-4 flex items-center gap-2">
            <span className="text-[#FF9F0A]">🔥</span> TOP 15 DO DIA
          </h2>
          <div className="space-y-3">
            {briefing.top_15.map((article) => (
              <BriefingCard
                key={`${article.rank}-${article.link}`}
                rank={article.rank}
                tags={[article.category || "outros"]}
                title={article.title}
                context={article.summary || ""}
                source={article.source || ""}
                link={article.link}
                relevanceScore={article.relevance_score}
              />
            ))}
          </div>
        </section>

        {/* Radar */}
        <section className="mb-10">
          <h2 className="text-lg font-semibold text-[#F5F5F5] mb-4 flex items-center gap-2">
            <span className="text-[#0A84FF]">📡</span> RADAR RÁPIDO
          </h2>
          <div className="space-y-4">
            {Object.entries(groupRadarByCategory()).map(([category, items]) => (
              <div key={category}>
                <div className="flex items-center gap-2 mb-2">
                  <TagBadge label={category} />
                  <span className="text-xs text-[#666]">{items.length} notícias</span>
                </div>
                <ul className="space-y-1.5">
                  {items.map((item, i) => (
                    <li key={i}>
                      <a
                        href={item.link}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="flex items-start gap-2 text-sm text-[#A0A0A0] hover:text-[#F5F5F5] transition-colors py-1"
                      >
                        <span className="text-[#666] mt-1">•</span>
                        <span className="flex-1">{item.title}</span>
                        <ExternalLink className="w-3 h-3 mt-0.5 shrink-0 opacity-40" />
                      </a>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </section>

        {/* Footer */}
        <footer className="text-center py-8 border-t border-[rgba(255,255,255,0.06)]">
          <p className="text-xs text-[#666]">
            NewsWeave — Briefing personalizado gerado com base no seu perfil
          </p>
        </footer>
      </div>
    </div>
  );
}
