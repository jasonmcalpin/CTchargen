export interface Character {
  name: string;
  upp: number[];
  upp_string: string;
  gender: string;
  race: string;
  age: number;
  career: string;
  rank: string;
  terms: number;
  skills: Record<string, number>;
  skills_string: string;
  weapons: string;
  armor: string;
  equipment: string;
  cash: number;
}

export interface CharacterGenerationRequest {
  num_characters: number;
  template: string;
  output_format: string;
  output_filename?: string;
  config_path?: string;
}

export interface CharacterGenerationResponse {
  characters: Character[];
  output_path?: string;
  template_used: string;
  format_used: string;
}

export interface TemplateListResponse {
  templates: string[];
  default_template: string;
}

export interface ConfigurationResponse {
  config: Record<string, any>;
}
