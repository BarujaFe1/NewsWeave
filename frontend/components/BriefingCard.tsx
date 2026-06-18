"use client";

import TagBadge from "./TagBadge";

interface BriefingCardProps {
  rank: number;
  tags: string[];
  title: string;
  context: string;
  source: string;
  link: string;
  relevanceScore: number;
}

export default function BriefingCard({
  rank,
  tags,
  title,
  context,
  source,
  link,
  relevanceScore,
}: BriefingCardProps) {
  return (
    <article
      className="rounded-2xl p-5 transition-all duration-200"
      style={{
        background: "rgba(255, 255, 255, 0.04)",
        border: "1px solid rgba(255, 255, 255, 0.08)",
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.background = "rgba(255, 255, 255, 0.07)";
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.background = "rgba(255, 255, 255, 0.04)";
      }}
    >
      <div className="flex items-start gap-4">
        <span className="text-[#A0A0A0] text-xs font-mono mt-1 min-w-[24px]">
          {String(rank).padStart(2, "0")}
        </span>
        <div className="flex-1 min-w-0">
          <div className="flex flex-wrap gap-1.5 mb-2.5">
            {tags.map((tag) => (
              <TagBadge key={tag} label={tag} />
            ))}
          </div>
          <h3 className="text-[17px] font-semibold leading-snug text-[#F5F5F5] mb-2">
            {title}
          </h3>
          <p className="text-sm text-[#A0A0A0] leading-relaxed mb-3 line-clamp-3">
            {context}
          </p>
          <div className="flex items-center justify-between text-xs text-[#666]">
            <span>{source}</span>
            <div className="flex items-center gap-3">
              <span className="text-[#0A84FF] text-[11px]">
                {relevanceScore}% relevante
              </span>
              <a
                href={link}
                target="_blank"
                rel="noopener noreferrer"
                className="text-[#0A84FF] hover:underline"
                aria-label={`Ler artigo: ${title}`}
              >
                Ler ↗
              </a>
            </div>
          </div>
        </div>
      </div>
    </article>
  );
}
