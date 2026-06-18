"use client";

import { motion, AnimatePresence } from "framer-motion";

interface QuizCardProps {
  question: string;
  questionNumber: number;
  totalQuestions: number;
  onAnswer: (answer: boolean) => void;
  animating: boolean;
}

export default function QuizCard({
  question,
  questionNumber,
  totalQuestions,
  onAnswer,
  animating,
}: QuizCardProps) {
  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={questionNumber}
        initial={{ opacity: 0, x: 40 }}
        animate={{ opacity: 1, x: 0 }}
        exit={{ opacity: 0, x: -40 }}
        transition={{ duration: 0.2, ease: "easeOut" }}
        className="flex flex-col items-center justify-center min-h-screen px-6 py-12"
      >
        <div className="w-full max-w-lg mx-auto">
          <p className="text-[#A0A0A0] text-sm font-mono mb-6 text-center">
            {String(questionNumber + 1).padStart(2, "0")}/{String(totalQuestions).padStart(2, "0")}
          </p>

          <div
            className="rounded-3xl p-8 md:p-10 text-center"
            style={{
              background: "rgba(255, 255, 255, 0.04)",
              backdropFilter: "blur(20px)",
              WebkitBackdropFilter: "blur(20px)",
              border: "1px solid rgba(255, 255, 255, 0.08)",
            }}
          >
            <h2 className="text-xl md:text-2xl font-semibold leading-relaxed text-[#F5F5F5] mb-10">
              {question}
            </h2>

            <div className="flex gap-4 justify-center">
              <button
                onClick={() => onAnswer(true)}
                disabled={animating}
                className="flex-1 max-w-[160px] py-4 px-6 rounded-2xl text-lg font-semibold transition-all duration-150 active:scale-95 disabled:opacity-40"
                style={{
                  background: "rgba(48, 209, 88, 0.12)",
                  color: "#30D158",
                  border: "1px solid rgba(48, 209, 88, 0.2)",
                }}
                onMouseEnter={(e) => {
                  e.currentTarget.style.background = "rgba(48, 209, 88, 0.2)";
                }}
                onMouseLeave={(e) => {
                  e.currentTarget.style.background = "rgba(48, 209, 88, 0.12)";
                }}
                aria-label="Sim"
              >
                SIM
              </button>
              <button
                onClick={() => onAnswer(false)}
                disabled={animating}
                className="flex-1 max-w-[160px] py-4 px-6 rounded-2xl text-lg font-semibold transition-all duration-150 active:scale-95 disabled:opacity-40"
                style={{
                  background: "rgba(255, 69, 58, 0.12)",
                  color: "#FF453A",
                  border: "1px solid rgba(255, 69, 58, 0.2)",
                }}
                onMouseEnter={(e) => {
                  e.currentTarget.style.background = "rgba(255, 69, 58, 0.2)";
                }}
                onMouseLeave={(e) => {
                  e.currentTarget.style.background = "rgba(255, 69, 58, 0.12)";
                }}
                aria-label="Não"
              >
                NÃO
              </button>
            </div>
          </div>

          <p className="text-center mt-6 text-xs text-[#A0A0A0]">
            Use as teclas <kbd className="px-1.5 py-0.5 rounded bg-[#1C1C1E] text-[#F5F5F5] font-mono text-[11px]">S</kbd> e{" "}
            <kbd className="px-1.5 py-0.5 rounded bg-[#1C1C1E] text-[#F5F5F5] font-mono text-[11px]">N</kbd> para responder
          </p>
        </div>
      </motion.div>
    </AnimatePresence>
  );
}
