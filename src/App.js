import React, { useEffect, useState } from "react";
import Button from "@mui/material/Button";
import { TextField } from "@mui/material/";

const App = () => {
  const [value, setValue] = useState("");
  const [events, setEvents] = useState([
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
  ]);

  const handleChange = (eventData) => {
    setValue(eventData.target.value);
  };

  const handleNewEvent = () => {
    const updateEvents = [
      {
        id: "1",
        eventName: "test",
      },
    ];
    setEvents((events) => [events, updateEvents]);
    console.log(`${events}`);
  };

  useEffect(() => {
    setEvents(events);
  }, [events]);

  return (
    <div className="list-container">
      <div className="card-container">
        {events.map(({ eventName, id }) => (
          <h2>
            {id}: {eventName}
          </h2>
        ))}
      </div>
      <div>
        <TextField
          value={value}
          id="outlined-basic"
          label="Enter event"
          variant="outlined"
          onChange={handleChange}
        />
      </div>
      <div>
        <Button variant="contained" onClick={handleNewEvent}>
          Add To List
        </Button>
      </div>
    </div>
  );
};

export default App;
