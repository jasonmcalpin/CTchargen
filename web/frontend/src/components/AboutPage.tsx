const AboutPage = () => {
  return (
    <div className="space-y-8">
      <section>
        <h1 className="text-3xl font-bold mb-4">About CTchargen</h1>
        <p className="text-lg text-gray-700 mb-4">
          CTchargen is a character generator for the Classic Traveller role-playing game system.
          It allows you to quickly generate characters with all the necessary stats, skills, and equipment.
        </p>
        <p className="text-lg text-gray-700">
          This tool was created to streamline the character creation process for Classic Traveller,
          making it easier for game masters and players to create characters for their campaigns.
        </p>
      </section>

      <section>
        <h2 className="text-2xl font-semibold mb-3">Features</h2>
        <ul className="list-disc list-inside space-y-2 text-gray-700">
          <li>Generate complete characters with UPP, skills, and equipment</li>
          <li>Export characters in various formats (text, markdown, etc.)</li>
          <li>Customize the generation process with different templates</li>
          <li>Generate multiple characters at once</li>
          <li>Web interface for easy access</li>
          <li>API for integration with other tools</li>
        </ul>
      </section>

      <section>
        <h2 className="text-2xl font-semibold mb-3">How It Works</h2>
        <p className="text-gray-700 mb-3">
          CTchargen uses the character generation rules from the Classic Traveller system to create
          characters. The process includes:
        </p>
        <ol className="list-decimal list-inside space-y-2 text-gray-700">
          <li>Generating Universal Personality Profile (UPP) characteristics</li>
          <li>Determining career path and terms of service</li>
          <li>Acquiring skills based on career and terms</li>
          <li>Generating appropriate equipment and cash</li>
          <li>Creating a character name based on phonetic rules</li>
        </ol>
      </section>

      <section>
        <h2 className="text-2xl font-semibold mb-3">Technologies Used</h2>
        <ul className="list-disc list-inside space-y-2 text-gray-700">
          <li>Backend: Python with FastAPI</li>
          <li>Frontend: React with TypeScript</li>
          <li>Styling: Tailwind CSS</li>
          <li>Character Generation: Custom Python modules</li>
        </ul>
      </section>
    </div>
  );
};

export default AboutPage;
