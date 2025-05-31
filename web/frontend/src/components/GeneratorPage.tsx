import { useState, useEffect } from 'react';
import { generateCharacters, getTemplates } from '../utils/api';
import { Character, CharacterGenerationRequest } from '../types/character';
import CharacterDisplay from './CharacterDisplay';

const GeneratorPage = () => {
  const [numCharacters, setNumCharacters] = useState(1);
  const [template, setTemplate] = useState('text');
  const [outputFormat, setOutputFormat] = useState('txt');
  const [outputFilename, setOutputFilename] = useState('');
  const [templates, setTemplates] = useState<string[]>([]);
  // We use defaultTemplate to initialize the template when templates are loaded
  const [defaultTemplate, setDefaultTemplate] = useState('text');
  const [characters, setCharacters] = useState<Character[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Fetch available templates
    const fetchTemplates = async () => {
      try {
        const response = await getTemplates();
        setTemplates(response.templates);
        setDefaultTemplate(response.default_template);
        setTemplate(response.default_template);
      } catch (err) {
        setError('Failed to load templates');
        console.error(err);
      }
    };

    fetchTemplates();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);

    try {
      const request: CharacterGenerationRequest = {
        num_characters: numCharacters,
        template,
        output_format: outputFormat,
        output_filename: outputFilename || undefined,
      };

      const response = await generateCharacters(request);
      setCharacters(response.characters);
    } catch (err) {
      setError('Failed to generate characters');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="space-y-8">
      <section>
        <h1 className="text-3xl font-bold mb-4">Character Generator</h1>
        <p className="text-gray-700">
          Generate characters for Classic Traveller by configuring the options below.
        </p>
      </section>

      <section className="card">
        <h2 className="text-xl font-semibold mb-4">Generation Options</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="numCharacters" className="block text-sm font-medium text-gray-700 mb-1">
              Number of Characters
            </label>
            <input
              type="number"
              id="numCharacters"
              min="1"
              max="100"
              value={numCharacters}
              onChange={(e) => setNumCharacters(parseInt(e.target.value))}
              className="input w-full"
            />
          </div>

          <div>
            <label htmlFor="template" className="block text-sm font-medium text-gray-700 mb-1">
              Template
            </label>
            <select
              id="template"
              value={template}
              onChange={(e) => setTemplate(e.target.value)}
              className="select w-full"
            >
              {templates.map((t) => (
                <option key={t} value={t}>
                  {t}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label htmlFor="outputFormat" className="block text-sm font-medium text-gray-700 mb-1">
              Output Format
            </label>
            <select
              id="outputFormat"
              value={outputFormat}
              onChange={(e) => setOutputFormat(e.target.value)}
              className="select w-full"
            >
              <option value="txt">Text (.txt)</option>
              <option value="md">Markdown (.md)</option>
              <option value="html">HTML (.html)</option>
            </select>
          </div>

          <div>
            <label htmlFor="outputFilename" className="block text-sm font-medium text-gray-700 mb-1">
              Output Filename (optional)
            </label>
            <input
              type="text"
              id="outputFilename"
              value={outputFilename}
              onChange={(e) => setOutputFilename(e.target.value)}
              placeholder="Leave blank for default"
              className="input w-full"
            />
          </div>

          <div className="pt-2">
            <button
              type="submit"
              className="btn btn-primary w-full"
              disabled={isLoading}
            >
              {isLoading ? 'Generating...' : 'Generate Characters'}
            </button>
          </div>
        </form>
      </section>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
          {error}
        </div>
      )}

      {characters.length > 0 && (
        <section>
          <h2 className="text-xl font-semibold mb-4">Generated Characters</h2>
          <div className="space-y-4">
            {characters.map((character, index) => (
              <CharacterDisplay key={index} character={character} />
            ))}
          </div>
        </section>
      )}
    </div>
  );
};

export default GeneratorPage;
