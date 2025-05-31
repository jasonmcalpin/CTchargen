import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div className="space-y-8">
      <section className="text-center py-12">
        <h1 className="text-4xl font-bold mb-4">Classic Traveller Character Generator</h1>
        <p className="text-xl text-gray-600 max-w-3xl mx-auto">
          Generate characters for the Classic Traveller RPG system with ease.
          Create, customize, and export your characters in various formats.
        </p>
        <div className="mt-8">
          <Link to="/generator" className="btn btn-primary text-lg px-6 py-3">
            Generate Characters
          </Link>
        </div>
      </section>

      <section className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="card">
          <h2 className="text-xl font-semibold mb-3">Fast Generation</h2>
          <p className="text-gray-600">
            Generate complete characters in seconds, with all the necessary stats, skills, and equipment.
          </p>
        </div>
        <div className="card">
          <h2 className="text-xl font-semibold mb-3">Multiple Formats</h2>
          <p className="text-gray-600">
            Export your characters in various formats, including plain text, markdown, and more.
          </p>
        </div>
        <div className="card">
          <h2 className="text-xl font-semibold mb-3">Customizable</h2>
          <p className="text-gray-600">
            Customize the generation process with various options and templates.
          </p>
        </div>
      </section>

      <section className="bg-gray-100 p-8 rounded-lg">
        <h2 className="text-2xl font-semibold mb-4">Getting Started</h2>
        <ol className="list-decimal list-inside space-y-2 text-gray-700">
          <li>Go to the <Link to="/generator" className="text-primary-600 hover:underline">Generator</Link> page</li>
          <li>Select the number of characters to generate</li>
          <li>Choose your preferred output format and template</li>
          <li>Click "Generate" to create your characters</li>
          <li>View, download, or copy your generated characters</li>
        </ol>
      </section>
    </div>
  );
};

export default HomePage;
