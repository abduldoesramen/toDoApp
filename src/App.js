import React, { useEffect, useState } from 'react'
import { Fragment } from 'react'
import EventContainer from './components/event-container/event-container.component'
import EventCard from './components/event-card/event-card.component'
import EventAddButton from './components/event-add-button/event-add-button.component'

const App = () => {
  const [value, setValue] = useState('')
  const [events, setEvents] = useState([
    {
      id: '1',
      eventName: 'Do the dishes',
    },
    {
      id: '2',
      eventName: 'Take out the trash',
    },
    {
      id: '3',
      eventName: 'Vacuum the floor',
    },
    {
      id: '4',
      eventName: 'Scrub the bathroom',
    },
  ])

  const handleChange = (eventData) => {
    setValue(eventData.target.value)
  }

  const handleNewEvent = () => {
    if (value) {
      const updateEvents = [
        ...events,
        {
          // Note: This is NOT unique if adding/deleting Events
          id: `${events.length + 1}`,
          eventName: value,
        },
      ]
      setEvents(updateEvents)
      setValue('')
    }
  }

  const handleDelEvent = (id) => {
    var tempEvents = [...events]
    var tempIndex = tempEvents.findIndex((element) => element.id === id)
    if (tempIndex !== -1) {
      tempEvents.splice(tempIndex, 1)
      setEvents(tempEvents)
    }
  }

  const handleChangeKeyPress = (eventData) => {
    if (eventData.keyCode === 13) {
      handleNewEvent()
    }
  }

  return (
    <Fragment>
      <EventContainer events={events} handleDelEvent={handleDelEvent} />
      <EventCard
        value={value}
        handleChange={handleChange}
        handleChangeKeyPress={handleChangeKeyPress}
      />
      <EventAddButton handleNewEvent={handleNewEvent} />
    </Fragment>
  )
}

export default App
