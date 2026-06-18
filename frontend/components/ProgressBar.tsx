"use client";

interface ProgressBarProps {
  current: number;
  total: number;
}

export default function ProgressBar({ current, total }: ProgressBarProps) {
  const pct = ((current + 1) / total) * 100;

  return (
    <div className="fixed top-0 left-0 right-0 z-50 h-[3px] bg-[#1C1C1E]">
      <div
        className="h-full bg-[#0A84FF] transition-all duration-200 ease-out"
        style={{ width: `${pct}%` }}
      />
    </div>
  );
}
