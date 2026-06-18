import { UserProfile } from "./profile";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8001";

export async function submitProfile(profile: UserProfile): Promise<{ id: number }> {
  const res = await fetch(`${API_URL}/api/profile`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(profile),
  });
  if (!res.ok) throw new Error("Erro ao salvar perfil");
  return res.json();
}

export async function getProfile(userId: number): Promise<UserProfile> {
  const res = await fetch(`${API_URL}/api/profile/${userId}`);
  if (!res.ok) throw new Error("Perfil não encontrado");
  return res.json();
}

export async function getBriefing(userId: number) {
  const res = await fetch(`${API_URL}/api/briefing/today?user_id=${userId}`);
  if (!res.ok) throw new Error("Erro ao carregar briefing");
  return res.json();
}

export async function triggerIngest() {
  const res = await fetch(`${API_URL}/api/ingest`, { method: "POST" });
  if (!res.ok) throw new Error("Erro na ingestão");
  return res.json();
}
