import React, { useEffect, useState } from "react";
import { Fragment } from "react";
import Button from "@mui/material/Button";
import EventContainer from "./components/event-container/event-container.component";
import EventCard from "./components/event-card/event-card.component";

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
    if (value) {
      const updateEvents = [
        ...events,
        {
          // Note: This is NOT unique if adding/deleting Events
          id: `${events.length + 1}`,
          eventName: value,
        },
      ];
      setEvents(updateEvents);
      setValue("");
    }
  };

  return (
    <Fragment>
      <EventContainer events={events} />
      <EventCard value={value} handleChange={handleChange} />
      <div className="event-add-button">
        <Button variant="contained" onClick={handleNewEvent}>
          Add To List
        </Button>
      </div>
    </Fragment>
  );
};

export default App;
