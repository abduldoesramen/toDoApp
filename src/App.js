import React, { useEffect, useState } from "react";
import { Fragment } from "react";
import EventContainer from "./components/event-container/event-container.component";
import EventCard from "./components/event-card/event-card.component";
import EventAddButton from "./components/event-add-button/event-add-button.component";
import EventTranslateButton from "./components/event-translate-button/event-translate-button.component";

const App = () => {
  const [value, setValue] = useState("");
  const [events, setEvents] = useState([
    {
      id: "0",
      eventName: "Do the dishes",
    },
    {
      id: "1",
      eventName: "Take out the trash",
    },
    {
      id: "2",
      eventName: "Vacuum the floor",
    },
    {
      id: "3",
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
          id: `${events.length}`,
          eventName: value,
        },
      ];
      setEvents(updateEvents);
      setValue("");
    }
  };

  const handleDelEvent = (id) => {
    // Array definitions
    var tempEvents = [...events];
    var nonDecrementEvents;
    // Index to be deleted
    var tempIndex = tempEvents.findIndex((element) => element.id === id);
    if (tempIndex !== -1) {
      // Events array for values to remain the same
      nonDecrementEvents = events.splice(0, tempIndex);
      // Events array for events.id to decrement
      tempEvents.splice(0, tempIndex + 1);
      for (const element of tempEvents) {
        if (element.id) {
          element.id = element.id - 1;
        }
      }
      // Concat both arrays in order to render updated, unique ids
      setEvents(nonDecrementEvents.concat(tempEvents));
    }
  };

  const handleChangeKeyPress = (eventData) => {
    if (eventData.keyCode === 13) {
      handleNewEvent();
    }
  };

  return (
    <Fragment>
      <EventContainer events={events} handleDelEvent={handleDelEvent} />
      <EventCard
        value={value}
        handleChange={handleChange}
        handleChangeKeyPress={handleChangeKeyPress}
      />
      <EventAddButton handleNewEvent={handleNewEvent} />
      <EventTranslateButton handleNewEvent={handleNewEvent} />
    </Fragment>
  );
};

export default App;
