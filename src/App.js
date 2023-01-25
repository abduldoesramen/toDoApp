import React, { useEffect, useState } from "react";
import { Fragment } from "react";
import Button from "@mui/material/Button";
import { TextField } from "@mui/material/";
import EventContainer from "./components/event-container/event-container.component";

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
      ...events,
      {
        id: "1",
        eventName: value,
      },
    ];
    setEvents(updateEvents);
    setValue("");
  };

  return (
    <Fragment>
      <div className="event-container">
        {events.map(({ eventName }) => (
          <h2>{eventName}</h2>
        ))}
      </div>
      <EventContainer events={events} />

      <div className="event-card">
        <TextField
          value={value}
          id="outlined-basic"
          label="Enter event"
          variant="outlined"
          onChange={handleChange}
        />
      </div>
      <div className="event-add-button">
        <Button variant="contained" onClick={handleNewEvent}>
          Add To List
        </Button>
      </div>
    </Fragment>
  );
};

export default App;
