export default function SkeletonBriefing() {
  return (
    <div className="max-w-2xl mx-auto px-4 py-8 animate-pulse">
      <div className="h-8 w-48 bg-[#1C1C1E] rounded-lg mb-2" />
      <div className="h-4 w-32 bg-[#1C1C1E] rounded mb-8" />
      <div className="h-6 w-40 bg-[#1C1C1E] rounded mb-4" />
      {Array.from({ length: 5 }).map((_, i) => (
        <div
          key={i}
          className="rounded-2xl p-5 mb-3"
          style={{ background: "rgba(255, 255, 255, 0.04)" }}
        >
          <div className="flex gap-2 mb-3">
            <div className="h-5 w-16 bg-[#1C1C1E] rounded-full" />
            <div className="h-5 w-20 bg-[#1C1C1E] rounded-full" />
          </div>
          <div className="h-5 w-full bg-[#1C1C1E] rounded mb-2" />
          <div className="h-4 w-3/4 bg-[#1C1C1E] rounded mb-2" />
          <div className="h-4 w-1/2 bg-[#1C1C1E] rounded" />
        </div>
      ))}
    </div>
  );
}
