import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/workouts/?format=json')
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  console.log(workouts);

  return (
    <div>
      <h1 className="text-center">Workouts</h1>
      <table className="table table-sm">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Exercises</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map((workout, index) => (
            <tr key={workout.workout_id || index}>
              <td>{workout.id}</td>
              <td>{workout.name}</td>
              <td>{JSON.parse(workout.exercises.replace(/'/g, '"')).join(', ')}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div>{JSON.stringify(workouts)}</div>
    </div>
  );
};

export default Workouts;
