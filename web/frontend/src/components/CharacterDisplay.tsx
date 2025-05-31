import { Character } from '../types/character';

interface CharacterDisplayProps {
  character: Character;
}

const CharacterDisplay = ({ character }: CharacterDisplayProps) => {
  return (
    <div className="card">
      <div className="flex flex-col md:flex-row md:justify-between md:items-start gap-4">
        <div>
          <h3 className="text-xl font-bold mb-2">{character.name}</h3>
          <div className="mb-2">
            <span className="font-medium">UPP:</span> {character.upp_string}
          </div>
          <div className="mb-2">
            <span className="font-medium">Gender:</span> {character.gender}
          </div>
          <div className="mb-2">
            <span className="font-medium">Race:</span> {character.race}
          </div>
          <div className="mb-2">
            <span className="font-medium">Age:</span> {character.age}
          </div>
          <div className="mb-2">
            <span className="font-medium">Career:</span> {character.career}
          </div>
          <div className="mb-2">
            <span className="font-medium">Rank:</span> {character.rank}
          </div>
          <div className="mb-2">
            <span className="font-medium">Terms:</span> {character.terms}
          </div>
        </div>

        <div className="flex-1">
          <div className="mb-4">
            <h4 className="font-medium mb-1">Skills</h4>
            <p className="text-gray-700">{character.skills_string}</p>
          </div>

          <div className="mb-4">
            <h4 className="font-medium mb-1">Weapons</h4>
            <p className="text-gray-700">{character.weapons || 'None'}</p>
          </div>

          <div className="mb-4">
            <h4 className="font-medium mb-1">Armor</h4>
            <p className="text-gray-700">{character.armor || 'None'}</p>
          </div>

          <div className="mb-4">
            <h4 className="font-medium mb-1">Equipment</h4>
            <p className="text-gray-700">{character.equipment || 'None'}</p>
          </div>

          <div>
            <h4 className="font-medium mb-1">Cash</h4>
            <p className="text-gray-700">{character.cash} Credits</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CharacterDisplay;
