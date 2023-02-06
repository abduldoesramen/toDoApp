import React, { useState } from "react";
import { Fragment } from "react";
import EventAddButton from "../../components/event-add-button/event-add-button.component";
import EventCard from "../../components/event-card/event-card.component";
import EventContainer from "../../components/event-container/event-container.component";
import EventTranslateButton from "../../components/event-translate-button/event-translate-button.component";
import Grid from "@mui/material/Grid";

const Home = () => {
  const [value, setValue] = useState("");
  // By default, initial language is English
  const [language, setLanguage] = useState("English");
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
          id: `${events.length}`,
          eventName: value,
        },
      ];
      setEvents(updateEvents);
      setValue("");
    }
  };

  const handleTranslate = () => {
    if (language === "English") {
      setLanguage("Japanese");
    } else {
      setLanguage("English");
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
      <Grid container alignItems="center" justify="center" direction="column">
        <Grid item>
          <h1>To Do App</h1>
        </Grid>
        <EventContainer events={events} handleDelEvent={handleDelEvent} />
        <EventCard
          value={value}
          handleChange={handleChange}
          handleChangeKeyPress={handleChangeKeyPress}
        />
        <Grid item marginTop={2} marginBottom={2}>
          <EventAddButton handleNewEvent={handleNewEvent} />
        </Grid>
        <EventTranslateButton
          handleTranslate={handleTranslate}
          language={language}
        />
      </Grid>
    </Fragment>
  );
};

export default Home;
