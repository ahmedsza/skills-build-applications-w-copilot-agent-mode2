import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/users/?format=json')
      .then(response => response.json())
      .then(data => setUsers(data))
      .catch(error => console.error('Error fetching users:', error));
  }, []);

  console.log(users);

  return (
    <div>
      <h1 className="text-center">Users</h1>
      <table className="table table-dark">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user, index) => (
            <tr key={user.id || index}>
              <td>{user.id}</td>
              <td>{user.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Users;
