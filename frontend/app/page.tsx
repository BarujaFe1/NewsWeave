"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { ArrowRight } from "lucide-react";

export default function Home() {
  const router = useRouter();
  const [hasProfile, setHasProfile] = useState<boolean | null>(null);

  useEffect(() => {
    const userId = localStorage.getItem("newsweave_user_id");
    setHasProfile(!!userId);
  }, []);

  if (hasProfile === null) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-[#0A0A0A]" />
    );
  }

  if (hasProfile) {
    router.replace("/briefing");
    return null;
  }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-[#0A0A0A] px-6">
      <div className="text-center max-w-md">
        <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl mb-6"
          style={{ background: "rgba(10, 132, 255, 0.1)", border: "1px solid rgba(10, 132, 255, 0.2)" }}>
          <svg className="w-8 h-8 text-[#0A84FF]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </div>
        <h1 className="text-3xl font-bold text-[#F5F5F5] mb-3">NewsWeave</h1>
        <p className="text-[#A0A0A0] text-sm leading-relaxed mb-8">
          Seu briefing diário personalizado. Feito sob medida para você.
          <br />
          Responda 50 perguntas rápidas e comece.
        </p>
        <button
          onClick={() => router.push("/onboarding")}
          className="inline-flex items-center gap-2 px-6 py-3 rounded-2xl text-sm font-semibold transition-all duration-150 active:scale-95"
          style={{
            background: "#0A84FF",
            color: "#fff",
          }}
          onMouseEnter={(e) => { e.currentTarget.style.background = "#006FE0"; }}
          onMouseLeave={(e) => { e.currentTarget.style.background = "#0A84FF"; }}
        >
          Começar Quiz
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
}
