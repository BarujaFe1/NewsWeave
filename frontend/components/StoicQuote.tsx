interface StoicQuoteProps {
  quote: string;
}

export default function StoicQuote({ quote }: StoicQuoteProps) {
  return (
    <div
      className="rounded-2xl p-5 text-center"
      style={{
        background: "rgba(255, 255, 255, 0.03)",
        border: "1px solid rgba(255, 255, 255, 0.06)",
      }}
    >
      <svg
        className="w-5 h-5 mx-auto mb-2 opacity-30"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.5"
      >
        <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
      <p className="text-sm text-[#A0A0A0] italic leading-relaxed">&ldquo;{quote}&rdquo;</p>
    </div>
  );
}
