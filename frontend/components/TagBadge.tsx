interface TagBadgeProps {
  label: string;
}

const TAG_COLORS: Record<string, { text: string; border: string }> = {
  TIMÃO: { text: "#0A84FF", border: "#0A84FF22" },
  BASTIDORES: { text: "#0A84FF", border: "#0A84FF22" },
  MERCADO: { text: "#30D158", border: "#30D15822" },
  TECH: { text: "#FF9F0A", border: "#FF9F0A22" },
  "POLÍTICA": { text: "#FF453A", border: "#FF453A22" },
  CRYPTO: { text: "#BF5AF2", border: "#BF5AF222" },
  GAMES: { text: "#64D2FF", border: "#64D2FF22" },
  MUNDO: { text: "#FF6961", border: "#FF696122" },
  SAÚDE: { text: "#30D158", border: "#30D15822" },
  ESPORTES: { text: "#0A84FF", border: "#0A84FF22" },
  ECONOMIA: { text: "#30D158", border: "#30D15822" },
  CIÊNCIA: { text: "#FF9F0A", border: "#FF9F0A22" },
};

function normalize(label: string): string {
  return label
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toUpperCase();
}

export default function TagBadge({ label }: TagBadgeProps) {
  const key = normalize(label);
  const colors = TAG_COLORS[key] ?? { text: "#A0A0A0", border: "#A0A0A022" };

  return (
    <span
      className="inline-flex items-center px-2.5 py-0.5 rounded-full text-[11px] font-medium leading-5 tracking-wide uppercase"
      style={{
        backgroundColor: "#1C1C1E",
        color: colors.text,
        border: `1px solid ${colors.border}`,
      }}
    >
      {label}
    </span>
  );
}
