export interface UserProfile {
  location: string;
  religion: string | null;
  music_taste: string[];
  football_team: string | null;
  follow_football: boolean;
  follow_tennis: boolean;
  follow_formula1: boolean;
  follow_esports: boolean;
  political_lean: "right" | "left" | "center" | "none";
  follow_brasilia: boolean;
  follow_stf: boolean;
  follow_economy: boolean;
  investor_profile: "conservative" | "moderate" | "aggressive" | "degen";
  follow_crypto: boolean;
  follow_stocks: boolean;
  follow_macro: boolean;
  follow_biotech: boolean;
  follow_reits: boolean;
  tech_enthusiast: boolean;
  pc_gamer: boolean;
  follow_ai: boolean;
  follow_startups: boolean;
  follow_smartphones: boolean;
  follows_gta: boolean;
  follows_lol: boolean;
  follows_fps: boolean;
  follows_rpg: boolean;
  biohacker: boolean;
  follow_longevity: boolean;
  follow_nutrition: boolean;
  follow_fitness: boolean;
  tone_preference: "formal" | "casual" | "ironic" | "data-driven";
  use_emojis: boolean;
  use_gifs: boolean;
  stoic_quotes: boolean;
  language: "pt-BR" | "en-US";
  city: string | null;
  follow_local_news: boolean;
  follow_science: boolean;
  follow_environment: boolean;
  follow_crime: boolean;
  follow_culture: boolean;
  follow_streaming: boolean;
  follow_movies: boolean;
  follow_music_news: boolean;
}

export function defaultProfile(): UserProfile {
  return {
    location: "",
    religion: null,
    music_taste: [],
    football_team: null,
    follow_football: false,
    follow_tennis: false,
    follow_formula1: false,
    follow_esports: false,
    political_lean: "none",
    follow_brasilia: false,
    follow_stf: false,
    follow_economy: false,
    investor_profile: "conservative",
    follow_crypto: false,
    follow_stocks: false,
    follow_macro: false,
    follow_biotech: false,
    follow_reits: false,
    tech_enthusiast: false,
    pc_gamer: false,
    follow_ai: false,
    follow_startups: false,
    follow_smartphones: false,
    follows_gta: false,
    follows_lol: false,
    follows_fps: false,
    follows_rpg: false,
    biohacker: false,
    follow_longevity: false,
    follow_nutrition: false,
    follow_fitness: false,
    tone_preference: "casual",
    use_emojis: true,
    use_gifs: false,
    stoic_quotes: false,
    language: "pt-BR",
    city: null,
    follow_local_news: false,
    follow_science: false,
    follow_environment: false,
    follow_crime: false,
    follow_culture: false,
    follow_streaming: false,
    follow_movies: false,
    follow_music_news: false,
  };
}
