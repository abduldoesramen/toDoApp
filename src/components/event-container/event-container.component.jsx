import "./event-container.styles.css";

const EventContainer = ({ events }) => {
    // return <h1>Hello World! {events}</h1>
    

    <div className="event-container" key={events.id}>
        return (
            {events.map(({ eventName }) => {
                {console.log(`${eventName}`)}
                    <h2>{eventName}</h2>
            })}
        )

    </div>
}

export default EventContainer;