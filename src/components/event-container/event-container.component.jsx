import "./event-container.styles.css";

const EventContainer = ({ events }) => {
    // return <h1>Hello World! {events}</h1>
    

    <div className="event-container" key={events.id}>
        {events.map(({ eventName }) => {
            {console.log(`${eventName.eventName}`)}
            return (
                <h2>{eventName.eventName}</h2>
            );
        })}
    </div>
}

export default EventContainer;