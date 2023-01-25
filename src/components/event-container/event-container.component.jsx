import "./event-container.styles.css";

const EventContainer = ({ events }) => {
    return (
        <div className="event-container" key={events.id}>
            {events.map(({eventName}) => {
                return <h2>{eventName}</h2>
            })}
        </div>
    )
}

export default EventContainer;