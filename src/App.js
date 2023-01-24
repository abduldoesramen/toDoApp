import Button from "@mui/material/Button";

const App = () => {
  const currList = [
    {
      id: "1",
      eventName: "Do the dishes",
    },
    {
      id: "2",
      eventName: "Take out the trash",
    },
    {
      id: "3",
      eventName: "Vacuum the floor",
    },
    {
      id: "4",
      eventName: "Scrub the bathroom",
    },
  ];

  return (
    <div className="list-container">
      <div className="card-list-container">
        <div className="card-container">
          {currList.map(({ eventName }) => (
            <h2>{eventName}</h2>
          ))}
        </div>
      </div>
      <Button variant="contained">Add To List</Button>
    </div>
  );
};

export default App;
