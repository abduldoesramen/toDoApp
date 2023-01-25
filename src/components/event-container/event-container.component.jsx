import "./event-container.styles.css";

const EventContainer = ({ events }) => {
    return (
        <div className="event-container" key={events.id}>
            {events.map(({eventName, id}) => {
                return <h2 key={id}>{`${id}. ${eventName}`}</h2>
            })}
        </div>
    )
}

export default EventContainer;