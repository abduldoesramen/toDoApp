import "./event-container.styles.css";

const EventContainer = ({ events }) => {
    return (
            <div className="event-container" key={events.id}>
                {events.map(({eventName, id}) => {
                    return <h1 key={id}>{`${id}. ${eventName}`}</h1>
                })}
            </div>
    )
}

export default EventContainer;