import axios from 'axios';
import { 
  CharacterGenerationRequest, 
  CharacterGenerationResponse,
  TemplateListResponse,
  ConfigurationResponse
} from '../types/character';

const API_URL = '/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const generateCharacters = async (request: CharacterGenerationRequest): Promise<CharacterGenerationResponse> => {
  const response = await api.post<CharacterGenerationResponse>('/characters/generate', request);
  return response.data;
};

export const getTemplates = async (): Promise<TemplateListResponse> => {
  const response = await api.get<TemplateListResponse>('/characters/templates');
  return response.data;
};

export const getConfiguration = async (): Promise<ConfigurationResponse> => {
  const response = await api.get<ConfigurationResponse>('/characters/config');
  return response.data;
};

export default api;
