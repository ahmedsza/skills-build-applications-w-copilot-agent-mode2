import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/activity/?format=json')
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  console.log(activities);

  return (
    <div>
      <h1 className="text-center">Activities</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {activities.map((activity, index) => (
            <tr key={activity.id || index}>
              <td>{activity.id}</td>
              <td>{activity.name ? JSON.parse(activity.name.replace(/'/g, '"')).join(', ') : 'No data'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Activities;
