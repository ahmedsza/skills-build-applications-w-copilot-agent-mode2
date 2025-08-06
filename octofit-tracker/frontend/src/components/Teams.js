import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/teams/?format=json')
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  console.log(teams);

  return (
    <div>
      <h1 className="text-center">Teams</h1>
      <table className="table table-hover">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {teams.map((team, index) => (
            <tr key={team.id || index}>
              <td>{team.id}</td>
              <td>{team.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Teams;
