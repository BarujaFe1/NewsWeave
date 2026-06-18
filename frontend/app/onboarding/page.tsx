"use client";

import { useState, useEffect, useCallback } from "react";
import { useRouter } from "next/navigation";
import QuizCard from "@/components/QuizCard";
import ProgressBar from "@/components/ProgressBar";
import { UserProfile, defaultProfile } from "@/lib/profile";
import { submitProfile } from "@/lib/api";

interface Question {
  id: number;
  text: string;
  field: keyof UserProfile;
  valueIfTrue: any;
  valueIfFalse: any;
}

const QUESTIONS: Question[] = [
  // BLOCO 1 — FUTEBOL & ESPORTES (1-8)
  { id: 1, text: "Você acompanha futebol regularmente?", field: "follow_football", valueIfTrue: true, valueIfFalse: false },
  { id: 2, text: "Você torce para o Corinthians?", field: "football_team", valueIfTrue: "Corinthians", valueIfFalse: null },
  { id: 3, text: "Quer notícias de bastidores, contratações e tretas do seu time?", field: "follow_football", valueIfTrue: true, valueIfFalse: false },
  { id: 4, text: "Acompanha o tênis brasileiro (ex: João Fonseca)?", field: "follow_tennis", valueIfTrue: true, valueIfFalse: false },
  { id: 5, text: "Acompanha Fórmula 1?", field: "follow_formula1", valueIfTrue: true, valueIfFalse: false },
  { id: 6, text: "Acompanha e-sports (CBLOL, League of Legends, CS2)?", field: "follow_esports", valueIfTrue: true, valueIfFalse: false },
  { id: 7, text: "Acompanha esportes americanos (NBA, NFL)?", field: "follow_tennis", valueIfTrue: true, valueIfFalse: false },
  { id: 8, text: "Quer saber quando times rivais passam vergonha?", field: "follow_football", valueIfTrue: true, valueIfFalse: false },

  // BLOCO 2 — POLÍTICA & BRASÍLIA (9-15)
  { id: 9, text: "Você acompanha política brasileira de perto?", field: "follow_brasilia", valueIfTrue: true, valueIfFalse: false },
  { id: 10, text: "Tem interesse em atualizações do STF e embates jurídicos?", field: "follow_stf", valueIfTrue: true, valueIfFalse: false },
  { id: 11, text: "Gosta de análises com viés liberal/conservador?", field: "political_lean", valueIfTrue: "right", valueIfFalse: "center" },
  { id: 12, text: "Quer saber sobre CPIs, escândalos e 'circo de Brasília'?", field: "follow_brasilia", valueIfTrue: true, valueIfFalse: false },
  { id: 13, text: "Acompanha política internacional (EUA, Europa, Oriente Médio)?", field: "follow_brasilia", valueIfTrue: true, valueIfFalse: false },
  { id: 14, text: "Tem interesse em política econômica (fiscal, câmbio, BC)?", field: "follow_economy", valueIfTrue: true, valueIfFalse: false },
  { id: 15, text: "Quer análises ácidas e irônicas sobre a classe política?", field: "political_lean", valueIfTrue: "right", valueIfFalse: "left" },

  // BLOCO 3 — MERCADO & FINANÇAS (16-24)
  { id: 16, text: "Você é investidor (qualquer nível)?", field: "investor_profile", valueIfTrue: "moderate", valueIfFalse: "conservative" },
  { id: 17, text: "Acompanha o mercado de ações (B3, NYSE)?", field: "follow_stocks", valueIfTrue: true, valueIfFalse: false },
  { id: 18, text: "Tem interesse em criptomoedas?", field: "follow_crypto", valueIfTrue: true, valueIfFalse: false },
  { id: 19, text: "Gosta de altcoins, memecoins e narrativas de alto risco (degen)?", field: "investor_profile", valueIfTrue: "degen", valueIfFalse: "moderate" },
  { id: 20, text: "Acompanha macro-economia (juros, inflação, dólar)?", field: "follow_macro", valueIfTrue: true, valueIfFalse: false },
  { id: 21, text: "Tem interesse em BioTech e empresas de saúde/longevidade?", field: "follow_biotech", valueIfTrue: true, valueIfFalse: false },
  { id: 22, text: "Acompanha fusões e aquisições (M&A) no Brasil e no mundo?", field: "follow_macro", valueIfTrue: true, valueIfFalse: false },
  { id: 23, text: "Investe ou tem interesse em FIIs (Fundos Imobiliários)?", field: "follow_reits", valueIfTrue: true, valueIfFalse: false },
  { id: 24, text: "Quer análises de small caps e empresas de crescimento?", field: "follow_stocks", valueIfTrue: true, valueIfFalse: false },

  // BLOCO 4 — TECNOLOGIA & IA (25-31)
  { id: 25, text: "Você se considera entusiasta de tecnologia?", field: "tech_enthusiast", valueIfTrue: true, valueIfFalse: false },
  { id: 26, text: "Acompanha lançamentos de hardware (GPU, CPU, smartphones)?", field: "follow_smartphones", valueIfTrue: true, valueIfFalse: false },
  { id: 27, text: "Tem interesse em Inteligência Artificial e seus impactos?", field: "follow_ai", valueIfTrue: true, valueIfFalse: false },
  { id: 28, text: "Acompanha startups e o ecossistema de venture capital?", field: "follow_startups", valueIfTrue: true, valueIfFalse: false },
  { id: 29, text: "Quer saber sobre novos modelos de IA (Claude, GPT, Gemini)?", field: "follow_ai", valueIfTrue: true, valueIfFalse: false },
  { id: 30, text: "Tem interesse em segurança digital e privacidade?", field: "tech_enthusiast", valueIfTrue: true, valueIfFalse: false },
  { id: 31, text: "Acompanha o mercado de dobráveis e wearables?", field: "follow_smartphones", valueIfTrue: true, valueIfFalse: false },

  // BLOCO 5 — GAMES (32-37)
  { id: 32, text: "Você joga videogame regularmente?", field: "follows_fps", valueIfTrue: true, valueIfFalse: false },
  { id: 33, text: "Acompanha notícias e vazamentos de GTA VI com intensidade detetivesca?", field: "follows_gta", valueIfTrue: true, valueIfFalse: false },
  { id: 34, text: "Joga ou acompanha League of Legends / CBLOL?", field: "follows_lol", valueIfTrue: true, valueIfFalse: false },
  { id: 35, text: "Tem interesse em FPS (CS2, Valorant, Call of Duty)?", field: "follows_fps", valueIfTrue: true, valueIfFalse: false },
  { id: 36, text: "Curte RPGs e world-building (Elden Ring, Baldur's Gate)?", field: "follows_rpg", valueIfTrue: true, valueIfFalse: false },
  { id: 37, text: "Acompanha a indústria de jogos (lançamentos, publishers, M&A)?", field: "follows_gta", valueIfTrue: true, valueIfFalse: false },

  // BLOCO 6 — ESTILO DE VIDA & SAÚDE (38-43)
  { id: 38, text: "Você tem interesse em longevidade, biohacking e otimização da saúde?", field: "biohacker", valueIfTrue: true, valueIfFalse: false },
  { id: 39, text: "Acompanha pesquisas de nutrição e suplementação?", field: "follow_nutrition", valueIfTrue: true, valueIfFalse: false },
  { id: 40, text: "Tem interesse em saúde mental e bem-estar?", field: "follow_longevity", valueIfTrue: true, valueIfFalse: false },
  { id: 41, text: "Acompanha novidades em exercício físico e performance?", field: "follow_fitness", valueIfTrue: true, valueIfFalse: false },
  { id: 42, text: "Tem interesse em cronobiologia, sono e ritmo circadiano?", field: "biohacker", valueIfTrue: true, valueIfFalse: false },
  { id: 43, text: "Quer saber sobre novos estudos de medicamentos (Ozempic, GLP-1)?", field: "follow_biotech", valueIfTrue: true, valueIfFalse: false },

  // BLOCO 7 — CULTURA & ENTRETENIMENTO (44-48)
  { id: 44, text: "Acompanha lançamentos de streaming (séries, filmes)?", field: "follow_streaming", valueIfTrue: true, valueIfFalse: false },
  { id: 45, text: "Tem interesse em música (lançamentos, tendências)?", field: "follow_music_news", valueIfTrue: true, valueIfFalse: false },
  { id: 46, text: "Acompanha cultura pop e internet (memes, virais)?", field: "follow_culture", valueIfTrue: true, valueIfFalse: false },
  { id: 47, text: "Quer notícias sobre livros, podcasts e educação?", field: "follow_culture", valueIfTrue: true, valueIfFalse: false },
  { id: 48, text: "Tem interesse em arte, design e arquitetura?", field: "follow_culture", valueIfTrue: true, valueIfFalse: false },

  // BLOCO 8 — PERFIL DA NEWSLETTER (49-50)
  { id: 49, text: "Você prefere um tom mais descontraído, com gírias e emojis?", field: "tone_preference", valueIfTrue: "casual", valueIfFalse: "formal" },
  { id: 50, text: "Gostaria de receber uma citação estoica (Sêneca, Marco Aurélio) no briefing?", field: "stoic_quotes", valueIfTrue: true, valueIfFalse: false },
];

export default function OnboardingPage() {
  const router = useRouter();
  const [profile, setProfile] = useState<UserProfile>(defaultProfile());
  const [current, setCurrent] = useState(0);
  const [animating, setAnimating] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  const handleAnswer = useCallback(
    async (answer: boolean) => {
      if (animating) return;
      setAnimating(true);

      const q = QUESTIONS[current];
      const value = answer ? q.valueIfTrue : q.valueIfFalse;

      setProfile((prev) => ({ ...prev, [q.field]: value }));

      setTimeout(() => {
        setAnimating(false);
        if (current < QUESTIONS.length - 1) {
          setCurrent((c) => c + 1);
        } else {
          finishProfile();
        }
      }, 200);
    },
    [current, animating]
  );

  useEffect(() => {
    const handleKey = (e: KeyboardEvent) => {
      if (e.key === "s" || e.key === "S") handleAnswer(true);
      if (e.key === "n" || e.key === "N") handleAnswer(false);
    };
    window.addEventListener("keydown", handleKey);
    return () => window.removeEventListener("keydown", handleKey);
  }, [handleAnswer]);

  async function finishProfile() {
    setSubmitting(true);
    try {
      const profileToSend = { ...profile };
      if (profileToSend.tone_preference !== "casual" && profileToSend.tone_preference !== "formal") {
        profileToSend.tone_preference = "casual";
      }
      const result = await submitProfile(profileToSend);
      localStorage.setItem("newsweave_user_id", String(result.id));
      router.replace("/briefing");
    } catch (err) {
      console.error("Erro ao salvar perfil:", err);
      setSubmitting(false);
    }
  }

  if (submitting) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-[#0A0A0A]">
        <div className="text-center">
          <div className="w-8 h-8 border-2 border-[#0A84FF] border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-[#A0A0A0] text-sm">Montando seu perfil...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#0A0A0A]">
      <ProgressBar current={current} total={QUESTIONS.length} />
      <QuizCard
        question={QUESTIONS[current].text}
        questionNumber={current}
        totalQuestions={QUESTIONS.length}
        onAnswer={handleAnswer}
        animating={animating}
      />
    </div>
  );
}
